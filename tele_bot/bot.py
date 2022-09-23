import urllib.request
import json


def get_token(name_file):
    with open(name_file, 'r') as ft:
        my_token = ft.readline()
    return my_token


def get_base_uri():
    token = get_token('bot_token')
    base_uri = f'https://api.telegram.org/bot{token}/'
    return base_uri


def connect_bot(method):
    url = f'{get_base_uri()}{method}'
    conn = urllib.request.urlopen(url)
    return conn


def send_message(user_id, text):
    # text = text.encode('ascii')
    url = f'{get_base_uri()}SendMessage?chat_id={user_id}&text={text}'
    conn = urllib.request.urlopen(url)
    return 'OK'


def parse_json(json_in):
    id_user = json_in['result'][-1]['message']['from']['id']
    text = json_in['result'][-1]['message']['text']
    return [id_user, text]


bt = connect_bot('getUpdates').read()
json_obj = json.loads(bt)
print(json_obj)

info_user = parse_json(json_obj)
print(info_user)
print(send_message(info_user[0], info_user[1]))
