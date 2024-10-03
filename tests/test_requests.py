import pytest
from datetime import datetime


# Testing all routes and their status codes
@pytest.mark.parametrize(('endpoint', 'status'), (
    ('/', 302),
    ('/index', 302),
    ('/all', 200),
    ('/date/1.1.', 200),
    ('/name/david', 200),
    ('/day/12', 200),
    ('/month/1', 200),
    ('/week/50', 200),
    ('/whatever', 404),
))
def test_all_routes(client, endpoint, status):
    assert client.get(endpoint).status_code == status


# Testing /today
def test_get_all(client):
    response = client.get('/today')
    data = response.get_json()

    today = datetime.now()

    assert data['msg'] == 'success'
    assert today.date() in data['data']


# Testing /all
def test_get_all(client):
    response = client.get('/all')
    data = response.get_json()

    assert data['msg'] == 'success'
    assert len(data['data']) > 350
    assert '2024-08-08' in data['data']
    assert data['data']['2024-12-30']['names'][0] == 'David'


# Testing /name/<name>
def test_by_name_full(client):
    response = client.get('/name/david')
    data = response.get_json()

    assert data['msg'] == 'success'
    assert len(data['data']) == 1
    assert '2024-12-30' in data['data']
    assert data['data']['2024-12-30']['names'][0] == 'David'


# Testing /date/<date_format>
def test_by_date(client):
    response1 = client.get('/date/30.12.')
    response2 = client.get('/date/12-30')
    response3 = client.get('/date/2024-12-30')
    dataset = [
        response1.get_json(),
        response2.get_json(),
        response3.get_json(),
    ]

    for data in dataset:
        assert data['msg'] == 'success'
        assert len(data['data']) == 1
        assert '2024-12-30' in data['data']
        assert data['data']['2024-12-30']['names'][0] == 'David'

    response_false = client.get('/date/random-date')
    dataf = response_false.get_json()
    assert dataf['msg'] == 'data not found'


# Testing /day/<day_number>
@pytest.mark.parametrize(('day', 'name'), (
    (1, 'Nový rok'),
    (50, 'Oldřich'),
    (100, 'Dušan'),
    (200, 'Drahomír'),
    (300, 'Erik'),
))
def test_by_day(client, day, name):
    response = client.get(f'/day/{day}')
    data = response.get_json()

    assert data['msg'] == 'success'
    assert len(data['data']) == 1

    key = list(data['data'].keys())[0]
    assert data['data'][key]['names'][0] == name


# Testing /week/<week_number>
def test_get_week(client):
    response = client.get('/week/16')
    data = response.get_json()

    assert data['msg'] == 'success'
    assert len(data['data']) == 7

    response_false = client.get('/week/120')
    dataf = response_false.get_json()
    assert dataf['msg'] == 'data not found'


# Testing /month/<month_number>
def test_get_month(client):
    response = client.get('/month/3')
    data = response.get_json()

    assert data['msg'] == 'success'
    assert len(data['data']) == 31

    response2 = client.get('/month/4')
    data2 = response2.get_json()

    assert data2['msg'] == 'success'
    assert len(data2['data']) == 30
