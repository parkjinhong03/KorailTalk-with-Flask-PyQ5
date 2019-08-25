from flask_restful import reqparse
import pymysql
from DB.connect import db_connect

def post():
    '''
    id와 pw, pw_check을 받아서 회원을 등록시켜주는 Method
    :parameter: id, pw, pw_check
    :return: status code
    200 - 성공
    '''

    try:
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str)
        parser.add_argument('pw', type=str)
        parser.add_argument('pw_check', type=str)
        args = parser.parse_args()

        _userId = args['id']
        _userPw = args['pw']
        _userPw_check = args['pw_check']

        db, cursor = db_connect()

        return 'POST'

    except SyntaxError as e:
        return {'error':str(e)}