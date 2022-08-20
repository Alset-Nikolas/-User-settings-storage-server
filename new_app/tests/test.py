import requests

BASE_URL = 'http://127.0.0.1:5000'


def create_full_url(user_name, param_name, type):
    return f'/api/parameters/{user_name}/{param_name}/{type}'


def test_get_user0_param1():
    '''Установим параметр пользователю param1=1(int)'''
    set_param_url = BASE_URL + create_full_url(user_name='user_0', param_name='param_1', type='int')
    params = {'value': 1}
    resp = requests.post(set_param_url, json=params)
    assert resp.status_code == 200, f'post request code = {resp.status_code}!= 200'


def test_check_user0_param1():
    '''Проверим появился ли параметр param1=1(int)'''
    check_param_url = BASE_URL + create_full_url(user_name='user_0', param_name='param_1', type='int')
    check_param = requests.get(check_param_url)
    assert check_param.status_code == 200, f'get request code = {check_param.status_code}!= 200'
    response = check_param.json()
    assert len(response) == 1, f'response={response}, len={len(response)}'
    param = response[0]
    assert param['type'] == 'int' and param['name'] == 'param_1' and param['value'] == 1, f'param={param}'


def test_update_user0_param1():
    '''Поменяет параметр param1=1(int) на 10 (int) и проверим'''
    set_param_url = BASE_URL + create_full_url(user_name='user_0', param_name='param_1', type='int')
    params = {'value': 10}
    resp = requests.post(set_param_url, json=params)
    assert resp.status_code == 200, f'post request code = {resp.status_code}!= 200'

    check_param_url = BASE_URL + create_full_url(user_name='user_0', param_name='param_1', type='int')
    check_param = requests.get(check_param_url)
    assert check_param.status_code == 200, f'get request code = {check_param.status_code}!= 200'
    response = check_param.json()
    assert len(response) == 1, f'response={response}, len={len(response)}'
    param = response[0]
    assert param['type'] == 'int' and param['name'] == 'param_1' and param['value'] == 10, f'param={param}'


def test_get_user0_param2():
    '''Установим параметр2 пользователю param2=a(str)'''
    set_param_url = BASE_URL + create_full_url(user_name='user_0', param_name='param_2', type='str')
    params = {'value': 'a'}
    resp = requests.post(set_param_url, json=params)
    assert resp.status_code == 200, f'post request code = {resp.status_code}!= 200'


def test_check_user0_param2():
    '''Проверим появился ли параметр param2=a(str)'''
    check_param_url = BASE_URL + create_full_url(user_name='user_0', param_name='param_2', type='str')
    check_param = requests.get(check_param_url)
    assert check_param.status_code == 200, f'get request code = {check_param.status_code}!= 200'
    response = check_param.json()
    assert len(response) == 1, f'response={response}, len={len(response)}'
    param = response[0]
    assert param['type'] == 'str' and param['name'] == 'param_2' and param['value'] == 'a', f'param={param}'


def test_get_bad_type_user0_param3():
    set_param_url = BASE_URL + create_full_url(user_name='user_0', param_name='param_3', type='str')
    params = {'value': 1}
    resp = requests.post(set_param_url, json=params)
    assert resp.status_code == 400, f'post request code = {resp.status_code}!= 200'


def request_post_value(value):
    set_param_url = BASE_URL + create_full_url(user_name='user_0', param_name='param_3', type='int')
    params = {'value': value}
    resp = requests.post(set_param_url, json=params)
    return resp.status_code


def test_get_bad_type_user0_param3_2():
    code1 = request_post_value('1')
    assert code1 == 400, f'post request code => {code1} != 400'
    code2 = request_post_value(None)
    assert code2 == 400, f'post request code => {code2} != 400'
    code3 = request_post_value('')
    assert code3 == 400, f'post request code => {code3} != 400'


def test_get_param_no_exist_user():
    ''' Параметры устанавливаются только для существующих юзеров.'''
    set_param_url = BASE_URL + create_full_url(user_name='user_9999', param_name='param_1', type='int')
    params = {'value': 1}
    resp = requests.post(set_param_url, json=params)
    assert resp.status_code == 400, f'status code => {resp.status_code}!= 400'


def test_get_no_exist_param_user():
    ''' При отсутствии подходящего параметра – пустой список.'''
    set_param_url = BASE_URL + create_full_url(user_name='user_0', param_name='param_zero', type='int')
    resp = requests.get(set_param_url)
    assert resp.status_code == 200, f'status code => {resp.status_code}!= 400'
    assert resp.json() == [], f'{resp.json()} != []'


def create_user_url(user_name):
    return f'/api/parameters/{user_name}'


def test_get_params_user0():
    ''' Проверим параметры нашего пользователя '''
    get_params_url = BASE_URL + create_user_url(user_name='user_0')
    resp = requests.get(get_params_url)
    assert resp.status_code == 200, f'status code => {resp.status_code}!= 400'
    response = resp.json()
    assert len(response) == 2, f'{len(response)} != 2'
    assert response == [{'type': 'int', 'name': 'param_1', 'value': 10},
                        {'type': 'str', 'name': 'param_2', 'value': 'a'}]


def test_get_noparams_user1():
    ''' Проверим параметры нашего пользователя '''
    get_params_url = BASE_URL + create_user_url(user_name='user_1')
    resp = requests.get(get_params_url)
    assert resp.status_code == 200, f'status code => {resp.status_code}!= 400'
    response = resp.json()
    assert len(response) == 0, f'{len(response)} != 0'
    assert response == []


def create_new_param(name, type, value):
    return {"operation": "SetParam",
            "name": name,
            "type": type,
            "value": value
            }


def test_gets_params_user3():
    ''' Проверим: Установка параметров через JSON-API  '''
    print('test_gets_params_user3', 'param1')
    set_param_url = BASE_URL + create_user_url(user_name='user_3')
    params = {'Query': [create_new_param('param1', 'int', 1)]}
    resp = requests.post(set_param_url, json=params)
    assert resp.status_code == 200, f'post request code = {resp.status_code}!= 200'
    response=resp.json()
    assert 'Results' in response, f'Results not in {response}'
    res = response['Results']
    assert len(res) == 1, f'{len(res)} != 1'
    assert res[0] == {'name': 'param1', 'type': 'int', 'value': 1, 'status': 'Ok', 'operation': 'SetParam'}

def test_gets_update_pdarams_user3():
    ''' Проверим: Установка параметров через JSON-API  '''
    test_gets_params_user3()
    set_param_url = BASE_URL + create_user_url(user_name='user_3')
    params = {'Query': [create_new_param('param2', 'str', 'asd')]}
    resp = requests.post(set_param_url, json=params)
    assert resp.status_code == 200, f'post request code = {resp.status_code}!= 200'
    response = resp.json()
    assert 'Results' in response, f'Results not in {response}'
    res = response['Results']
    assert len(res)==1, f'{len(res)} != 1'
    item = res[0]
    assert item['status'] == 'Ok' and item['value'] == 'asd' and item['type'] == 'str'

    resp = requests.get(set_param_url)
    assert resp.status_code==200
    items = resp.json()
    assert len(items)==2



