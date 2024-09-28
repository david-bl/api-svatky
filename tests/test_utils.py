import pytest
import app.utils as utils
from datetime import datetime

# Test YEAR constant
YEAR = datetime.now().year

# Testy pro get_formated_data
def test_get_formated_data():
    result = utils.get_formated_data('Jan', 1, 1)
    assert result['names'] == ['Jan']
    assert result['date_name'] == '1. Ledna'
    assert result['date_format_cz'] == f'1. 1. {YEAR}'
    assert result['date_format_iso'] == f'{YEAR}-01-01'
    assert result['day_name'] == 'Pondělí'  # 1. ledna 2024 je Pondělí
    assert result['week'] == 1
    assert isinstance(result['timestamp'], float)
    assert result['day_in_year'] == 1

# Testy pro get_datetime_from_day_in_year
def test_get_datetime_from_day_in_year():
    result = utils.get_datetime_from_day_in_year(1)
    assert result.year == YEAR
    assert result.month == 1
    assert result.day == 1

    result = utils.get_datetime_from_day_in_year(365)
    assert result.year == YEAR
    assert result.month == 12
    assert result.day == 30  # Assuming non-leap year

# Testy pro get_datetime_from_input
def test_get_datetime_from_input():
    # Test pro formát "dd.mm."
    result = utils.get_datetime_from_input("01.01.")
    assert result.year == YEAR
    assert result.month == 1
    assert result.day == 1

    # Test pro formát "mm-dd"
    result = utils.get_datetime_from_input("01-01")
    assert result.year == YEAR
    assert result.month == 1
    assert result.day == 1

    # Test pro formát "yyyy-mm-dd"
    result = utils.get_datetime_from_input("2024-01-01")
    assert result.year == 2024
    assert result.month == 1
    assert result.day == 1

    # Test pro neplatný formát
    result = utils.get_datetime_from_input("invalid")
    assert result is None

# Testy pro get_date_range_from_week
def test_get_date_range_from_week():
    result = utils.get_date_range_from_week(1, YEAR)
    assert result[0].year == YEAR
    assert result[0].month == 1
    assert result[0].day == 1
    assert result[1].year == YEAR
    assert result[1].month == 1
    assert result[1].day == 7

    # Test pro neplatný týden
    result = utils.get_date_range_from_week(55, YEAR)
    assert result == (None, None)

# Testy pro day_name
def test_day_name():
    assert utils.day_name(0) == 'Pondělí'
    assert utils.day_name(6) == 'Neděle'
    assert utils.day_name(7) == ''  # Neplatný den

# Testy pro month_name
def test_month_name():
    assert utils.month_name(1) == 'Ledna'
    assert utils.month_name(12) == 'Prosince'
    assert utils.month_name(13) == ''  # Neplatný měsíc

if __name__ == '__main__':
    pytest.main()
