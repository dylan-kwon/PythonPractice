# coding=utf-8

import MySQLdb
from flask import Flask, request, jsonify

from dbModule import db_connect

apii = Flask(__name__)


@apii.route('/api/user/')
def api_user():
    result_json = dict()
    result_data = dict()

    conn = db_connect()
    curs = conn.cursor(MySQLdb.cursors.DictCursor)
    curs.execute('set names utf8')

    ver = request.headers.get('ver', None)
    device = request.headers.get('device', None)
    revision = request.headers.get('revision', None)
    service_type = request.headers.get('service_type', None)
    token = request.headers.get('token')

    if token is None:
        result_json['result_code'] = 210
        result_json['result_msg'] = '토큰이 없어요.'

        conn.close()

        return jsonify(result_json)

    if request.method == 'GET':
        try:
            type = request.args.get('type', 0)

            sql = '''
                SELECT
                  u.id, u.name, u.phone,
                  IFNULL(u.country_id, 0) AS country_id,
                  IFNULL(u.power, 0) AS power,
                  c.country_name, c.language
                FROM
                  user AS u LEFT JOIN country AS c ON u.country_id = c.id 
                WHERE c.id = %s 
                ORDER BY c.id ASC
            ''' % int(type)

            curs.execute(sql)

        except (MySQLdb.Error, MySQLdb.Warning, TypeError) as e:
            print e
            result_json['result_code'] = 210
            result_json['result_msg'] = '조회를 실패했어요.'

        else:
            result_db_users = curs.fetchall()

            users = list()
            for db_user in result_db_users:
                user = dict()
                country = dict()

                user['id'] = db_user['id']
                user['name'] = db_user['name']
                user['phone'] = db_user['phone']
                user['power'] = db_user['power']

                country['id'] = db_user['country_id']
                country['name'] = db_user['country_name']
                country['language'] = db_user['language']

                user['country'] = country

                users.append(user)

            result_data['users'] = users
            result_json['result_data'] = result_data

            result_json['result_code'] = 200
            result_json['result_msg'] = '조회를 성공했어요'

        finally:
            conn.close()
            return jsonify(result_json)


@apii.route('/api/user/<user_id>/', methods=['GET', 'DELETE'])
def api_user_id(user_id):
    result_json = dict()
    result_data = dict()

    conn = db_connect()
    curs = conn.cursor(MySQLdb.cursors.DictCursor)
    curs.execute('set names utf8')

    ver = request.headers.get('ver', None)
    device = request.headers.get('device', None)
    revision = request.headers.get('revision', None)
    service_type = request.headers.get('service_type', None)
    token = request.headers.get('token')

    if token is None:
        result_json['result_code'] = 210
        result_json['result_msg'] = '토큰이 없어요'

        conn.close()

        return jsonify(result_json)

    if request.method == 'GET':
        try:
            sql = '''
                  SELECT
                    u.id, u.name, u.phone,
                    IFNULL(u.power, 0) AS power,
                    IFNULL(u.country_id, 0) AS country_id,
                    c.country_name, c.language
                  FROM 
                    user AS u LEFT JOIN country AS c ON u.country_id = c.id
                  WHERE 
                    u.id = %s
                ''' % int(user_id)

            curs.execute(sql)

        except (MySQLdb.Error, MySQLdb.Warning, TypeError) as e:
            print e
            result_json['result_code'] = 210
            result_json['result_msg'] = '유저 조회를 실패했어요'

        else:
            result_db_user = curs.fetchone()
            if result_db_user is None:
                result_json['result_code'] = 210
                result_json['result_msg'] = '유저가 없어요'
                return jsonify(result_json)

            user = dict()
            country = dict()

            user['id'] = result_db_user['id']
            user['name'] = result_db_user['name']
            user['phone'] = result_db_user['phone']
            user['power'] = result_db_user['power']

            country['id'] = result_db_user['country_id']
            country['name'] = result_db_user['country_name']
            country['language'] = result_db_user['language']

            user['country'] = country

            result_data['user'] = user
            result_json['result_data'] = result_data

            result_json['result_code'] = 200
            result_json['result_msg'] = '유저 조회를 성공했어요'

        finally:
            conn.close()
            return jsonify(result_json)

    elif request.method == 'DELETE':
        try:
            sql = '''
                DELETE
                FROM
                  user
                WHERE
                  id = %s
            ''' % int(user_id)

            curs.execute(sql)

        except (MySQLdb.Error, MySQLdb.Warning, TypeError) as e:
            print e
            result_json['result_code'] = 210
            result_json['result_msg'] = '유저 삭제를 실패했어요'

        else:
            conn.commit()

            result_json['result_code'] = 200
            result_json['result_msg'] = '유저 삭제를 성공했어요'

        finally:
            conn.close()
            return jsonify(result_json)


@apii.route('/api/user/join/', methods=['POST'])
def api_user_join():
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
        result_json['result_msg'] = '토큰이 없어요'

        conn.close()

        return jsonify(result_json)

    try:
        if request.method == 'POST':
            name = request.form.get('name', None)
            phone = request.form.get('phone', None)
            power = request.form.get('power', None)
            country_id = request.form.get('country_id', None)

            sql = '''
                INSERT 
                INTO 
                  user (name, phone, power, country_id)
                VALUES 
                  ('%s', '%s', %s, %s)
            ''' % (name, phone, int(power), int(country_id))

            curs.execute(sql)

    except (MySQLdb.Error, MySQLdb.Warning, TypeError, BaseException) as e:
        print e
        result_json['result_code'] = 210
        result_json['result_msg'] = '유저 등록을 실패했어요'

    else:
        conn.commit()

        result_json['result_code'] = 200
        result_json['result_msg'] = '유저 등록을 성공했어요'

    finally:
        conn.close()
        return jsonify(result_json)


@apii.route('/api/user/<user_id>/power/', methods=['PUT'])
def api_user_id_power(user_id):
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
        result_json['result_msg'] = '토큰이 없어요'

        conn.close()

        return jsonify(result_json)

    if request.method == 'PUT':
        try:
            power = request.form.get('power', None)

            sql = '''
                UPDATE
                  user
                SET
                  power = %s
                WHERE
                  id = %s
            ''' % (int(power), int(user_id))

            curs.execute(sql)

        except (MySQLdb.Error, MySQLdb.Warning, TypeError) as e:
            print e
            result_json['result_code'] = 210
            result_json['result_msg'] = '변경을 실패했어요.'

        else:
            conn.commit()

            result_json['result_code'] = 200
            result_json['result_msg'] = '변경을 성공했어요'

        finally:
            conn.close()
            return jsonify(result_json)


if __name__ == '__main__':
    apii.run(host='0.0.0.0', port=3000, debug=True)
    # api.run(debug=True)
