from datetime import datetime, timedelta


YEAR = datetime.now().year


def get_formated_data(name, day, month):
    dt = datetime(YEAR, month, day)

    return {
        'names':            [name],
        'date_name':        '%d. %s' % (day, month_name(month)),
        'date_format_cz':   '%d. %d. %d' % (day, month, YEAR),
        'date_format_iso':  '%d-%02d-%02d' % (YEAR, month, day),
        'day_name':         day_name(dt.weekday()),
        'week':             int(dt.strftime("%V")),
        'timestamp':        dt.timestamp(),
        'day_in_year':      dt.timetuple().tm_yday,
    }


def get_datetime_from_day_in_year(day):
    dt = datetime(YEAR, 1, 1) + timedelta(days=int(day - 1))
    return dt


def get_datetime_from_input(inp):
    '''types of input: "dd.mm.", "mm-dd", "yyyy-mm-dd"'''

    try:
        day, month = 0, 0

        # Handle format "dd.mm."
        if inp.find('.') != -1:
            inp = inp.split('.')
            if len(inp) >= 2:
                day = int(inp[0])
                month = int(inp[1])

        # Handle format "mm-dd" & "yyyy-mm-dd"
        elif inp.find('-') != -1:
            inp = inp.split('-')
            if len(inp) == 2:
                day = int(inp[1])
                month = int(inp[0])
            elif len(inp) == 3:
                day = int(inp[2])
                month = int(inp[1])

        dt = datetime(YEAR, month, day)
        return dt

    except Exception:
        return None


def get_date_range_from_week(p_week, p_year=YEAR):
    try:
        first = datetime.strptime(f'{p_year}-W{int(p_week)}-1', "%Y-W%W-%w").date()
        last = first + timedelta(days=6.9)
        return (first, last)
    except Exception:
        return (None, None)


def day_name(day):
    names = ['Pondělí', 'Úterý', 'Středa', 'Čtvrtek', 'Pátek', 'Sobota', 'Neděle']
    try:
        return names[int(day)]
    except Exception:
        return ''


def month_name(month):
    names = [
        'Ledna', 'Února', 'Března', 'Dubna', 
        'Května', 'Června', 'Července', 'Srpna', 
        'Září', 'Října', 'Listopadu', 'Prosince']
    try:
        return names[int(month - 1)]
    except Exception:
        return ''
