#! /usr/bin/python
# -*- coding: utf-8 -*-s

import sqlite3
from wsgiref.simple_server import make_server
from cgi import escape
#from html import escape
from urlparse import parse_qs
#from urllib.parse import parse_qs

data_structure = [
    [{'name': 'Краснодарский край',
     'cities': ['Краснодар', 'Кропоткин', 'Славянск']}],

    [{'name':'Ростовская область',
     'cities': ['Ростов', 'Шахты', 'Батайск']}],

    [{'name': 'Ставропольский край',
     'cities': ['Ставрополь', 'Пятигорск', 'Кисловодск']}]
]


def inspect_db():

    connect_to_db = sqlite3.connect('web3.sqlite3')

    cursor_obj = connect_to_db.cursor()

    with open('sql_script.sql', 'r') as sql_script_file:
        sql_script_str = ''.join(sql_script_file.readlines())
    

    cursor_obj.executescript(sql_script_str)

    i = 1
    for region in data_structure:
        try:
            sql_str = 'INSERT INTO regions (region_id, region_name) VALUES (%d,"%s")' % (i, region[0]['name'])
            cursor_obj.execute(sql_str)

        except sqlite3.IntegrityError:
            pass

        for city in region[0]['cities']:
            try:
                cursor_obj.execute('''INSERT INTO cities(region_id, city) VALUES(%d,"%s")''' % (i, city))
            except sqlite3.IntegrityError:
                pass
        i += 1

    connect_to_db.commit()
    cursor_obj.close()
    connect_to_db.close()

def get_html():
    with open('index.html', 'r') as html_file:
        html_str = ''.join(html_file.readlines())

    return html_str


def web3_app(environ, start_response):
    if environ['PATH_INFO'] == '/comment':

        inspect_db()

        try:
            request_body_size = int(environ.get('CONTENT_LENGTH', 0))
        except ValueError:
            request_body_size = 0

        request_body = environ['wsgi.input'].read(request_body_size)
        req_values = parse_qs(request_body)

        first_name = req_values.get('first_name', [''])[0]
        first_name = escape(first_name)
        second_name = req_values.get('second_name', [''])[0]
        second_name = escape(second_name)
        patronymic = req_values.get('patronymic', [''])[0]
        patronymic = escape(patronymic)
        region = req_values.get('region', [''])[0]
        region = escape(region)
        city = req_values.get('city', [''])[0]
        city = escape(city)
        phone = req_values.get('phone', [''])[0]
        phone = escape(phone)
        email = req_values.get('email', [''])[0]
        email = escape(email)
        comment = req_values.get('comment', [''])[0]
        comment= escape(comment)

        html = get_html()
        body = html % {
            'first_name': first_name,
            'second_name': second_name,
            'patronymic': patronymic,
            'region': region,
            'city': city,
            'phone': phone,
            'email': email,
            'comment': comment
        }

        status = '200 OK'
        response_headers = [
            ('Content-Type', 'text/html'),
            ('Content-Length', str(len(body)))
        ]
        start_response(status, response_headers)
        return [body]

if __name__ == '__main__':
    # Instantiate the server
    httpd = make_server ('localhost', 8051, web3_app)
    httpd.serve_forever()


