from flask import redirect, jsonify

from app import app, config_swag, services
from flasgger import swag_from


# index redirect to docs
@app.route('/')
@app.route('/index')
def index():
    return redirect('/apidocs'), 302


# All data
@app.route('/all', methods=('GET',))
@swag_from(config_swag.swag_route_all)
def all():
    return services.get_all()


# Today data
@app.route('/today', methods=('GET',))
@swag_from(config_swag.swag_route_today)
def today():
    return services.get_today()


# Tomorrow data
@app.route('/tomorrow', methods=('GET',))
@swag_from(config_swag.swag_route_tomorrow)
def tomorrow():
    return services.get_tomorrow()


# Find by name
@app.route('/name/<string:name>', methods=('GET',))
@swag_from(config_swag.swag_route_name)
def name(name):
    return services.get_data_by_name(name)


# Find by date
@app.route('/date/<string:date_format>', methods=('GET',))
@swag_from(config_swag.swag_route_date)
def date(date_format):
    return services.get_data_by_date(date_format)


# Find by day (in year)
@app.route('/day/<int:day_number>', methods=('GET',))
@swag_from(config_swag.swag_route_day)
def day(day_number):
    return services.get_data_by_day(day_number)


# Find by week
@app.route('/week/<int:week_number>', methods=('GET',))
@swag_from(config_swag.swag_route_week)
def week(week_number):
    return services.get_data_by_week(week_number)


# Find by month
@app.route('/month/<int:month_number>', methods=('GET',))
@swag_from(config_swag.swag_route_month)
def month(month_number):
    return services.get_data_by_month(month_number)


# Handle errors
@app.errorhandler(404)
def page_not_found(error):
    return services.res_not_found_endpoint(), 404

@app.errorhandler(429)
def rate_limit_error(error):
    return jsonify(msg='Too many requests. Try again later.'), 429
