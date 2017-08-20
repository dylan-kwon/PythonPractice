# coding=utf-8

import MySQLdb
from flask import Flask, request, jsonify

from dbModule import db_connect

apii = Flask(__name__)


@apii.route('/api/country/<country_id>/', methods=['GET'])
def api_country_id(country_id):
    result_json = dict()
    result_data = dict()

    conn = db_connect()
    curs = conn.cursor(MySQLdb.cursors.DictCursor)
    curs.execute('set names utf8')

    ver = request.headers.get('ver', None)
    device = request.headers.get('device', None)
    revision = request.headers.get('revision', None)
    service_type = request.headers.get('service_type', None)
    token = request.headers.get('token', None)

    if token is None:
        result_json['result_code'] = 210
        result_json['result_msg'] = '토큰이 없습니다.'

        conn.close()

        return jsonify(result_json)

    if request.method == 'GET':
        try:
            sql = '''
                SELECT
                  *
                FROM
                  country
                WHERE
                  id = %s
            ''' % int(country_id)

            curs.execute(sql)

        except (MySQLdb.Error, MySQLdb.Warning, TypeError) as e:
            print e
            result_json['result_code'] = 210
            result_json['result_msg'] = '실패했습니다.'

        else:
            result_db_country = curs.fetchone()

            if result_db_country is None:
                result_json['result_code'] = 210
                result_json['result_msg'] = '없는 국가입니다.'

            result_data['country'] = result_db_country
            result_json['result_data'] = result_data

            result_json['result_code'] = 200
            result_json['result_msg'] = '성공했습니다.'

        finally:
            conn.close()
            return jsonify(result_json)


@apii.route('/api/country/', methods=['POST'])
def api_country():
    result_json = dict()
    result_data = dict()

    conn = db_connect()
    curs = conn.cursor(MySQLdb.cursors.DictCursor)
    curs.execute('set names utf8')

    ver = request.headers.get('ver', None)
    device = request.headers.get('device', None)
    revision = request.headers.get('revision', None)
    service_type = request.headers.get('service_type', None)
    token = request.headers.get('token', None)

    if token is None:
        result_json['result_code'] = 210
        result_json['result_msg'] = '토큰이 없어요.'

        conn.close()

        return jsonify(result_json)

    if request.method == 'POST':
        try:
            country_name = request.form.get('country_name', None)
            language = request.form.get('language', None)

            sql = '''
                INSERT
                INTO
                  country (country_name, language)
                VALUES
                  ('%s', '%s')
            ''' % (country_name, language)

            curs.execute(sql)

        except (MySQLdb.Error, MySQLdb.Warning, TypeError) as e:
            print e
            result_json['result_code'] = 210
            result_json['result_msg'] = '국가 등록을 실패했어요.'

        else:
            conn.commit()

            result_json['result_code'] = 200
            result_json['result_msg'] = '국가 등록을 성공했어요.'

        finally:
            conn.close()
            return jsonify(result_json)


if __name__ == '__main__':
    apii.run(host='0.0.0.0', port=5000, debug=True)
    # api.run(debug=True)
