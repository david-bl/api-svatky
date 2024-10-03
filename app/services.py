from flask import jsonify
from app.db import get_db
from app import utils
from datetime import datetime


# Endpoint /name/<arg>
def get_data_by_name(name):
    query = '''SELECT strftime('%d', "date") as d, 
    strftime('%m', "date") as m, "name", "date"
    FROM "data" WHERE LOWER("name") = LOWER(?)'''

    data = select_db_data(query, (name,))
    response = res_with_data(data)

    return response


# Endpoint /date/<arg>
def get_data_by_date(date):
    query = '''SELECT strftime('%d', "date") as d, 
    strftime('%m', "date") as m, "name", "date"
    FROM "data" WHERE "date" = ?'''

    dt = utils.get_datetime_from_input(date)

    if dt is None:
        return res_not_found_data()

    data = select_db_data(query, (dt.strftime("%Y-%m-%d"),))
    response = res_with_data(data)

    return response


# Endpoint /day/<arg>
def get_data_by_day(day):
    query = '''SELECT strftime('%d', "date") as d, 
    strftime('%m', "date") as m, "name", "date"
    FROM "data" WHERE "date" = ?'''

    dt = utils.get_datetime_from_day_in_year(day)

    data = select_db_data(query, (dt.strftime("%Y-%m-%d"),))
    response = res_with_data(data)

    return response


# Endpoint /week/<arg>
def get_data_by_week(week):
    query = '''SELECT strftime('%d', "date") as d, 
    strftime('%m', "date") as m, "name", "date"
    FROM "data" WHERE "date" BETWEEN ? AND ?  
    ORDER BY "date" ASC'''

    (date1, date2) = utils.get_date_range_from_week(week)

    if date1 is None or date2 is None:
        return res_not_found_data()

    date1 = date1.strftime("%Y-%m-%d")
    date2 = date2.strftime("%Y-%m-%d")

    data = select_db_data(query, (date1, date2))
    response = res_with_data(data)

    return response


# Endpoint /month/<arg>
def get_data_by_month(month):
    query = '''SELECT strftime('%d', "date") as d, 
    strftime('%m', "date") as m, "name", "date"
    FROM "data" WHERE strftime('%m', "date") = ? 
    ORDER BY "date" ASC'''

    data = select_db_data(query, (str('%02d' % month),))
    response = res_with_data(data)

    return response


# Endpoint /all
def get_all():
    query = '''SELECT strftime('%d', "date") as d, 
    strftime('%m', "date") as m, "date", "name" 
    FROM "data" ORDER BY "date" ASC'''

    data = select_db_data(query)
    response = res_with_data(data)

    return response


# Endpoint /today
def get_today():
    query = '''SELECT strftime('%d', "date") as d, 
    strftime('%m', "date") as m, "date", "name" 
    FROM "data" WHERE "date" = ? 
    ORDER BY "date" ASC'''

    today = datetime.now().date()

    data = select_db_data(query, (today,))
    response = res_with_data(data)

    return response


def select_db_data(query, args=()):
    data = {}
    result = get_db().execute(query, args).fetchall()

    for res in result:
        name = res['name']
        key = str(res['date'])
        day = int(res['d'])
        month = int(res['m'])

        if key in data:
            data[key]['names'].append(name)
        else:
            data[key] = utils.get_formated_data(name, day, month)

    return data


def res_with_data(data):
    if not data:
        return res_not_found_data()

    response = {
        'msg': 'success',
        'data': data
    }

    return jsonify(response)


def res_not_found_data(do_jsonify=True):
    ret = {'msg': 'data not found'}

    if do_jsonify:
        return jsonify(ret)

    return ret


def res_not_found_endpoint():
    return jsonify({'msg': '404 - endpoint not found. Check /apidocs'})
