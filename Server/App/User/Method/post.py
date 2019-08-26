from flask_restful import reqparse
import pymysql
from DB.connect import db_connect
from DB.User.id_exist import id_exist

def signup():
    '''
    id와 pw, pw_check을 받아서 회원을 등록시켜주는 POST Method
    :parameter: id, pw, pw_check
    :return: status code
    200 - 성공
    410 - 이미 사용중인 ID
    411 - 비밀번호 입력 오류
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


        sql = '''
            CREATE TABLE userlog (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id  TEXT NOT NULL,
                user_pw TEXT NOT NULL
            )'''

        try:
            cursor.execute(sql)
        except:
            pass

        if _userPw != _userPw_check:
            return {"message": "pw and pw_check do not match.", "code": 411}, 411

        if id_exist(db, cursor, _userId) == True:
            return {"message": "This ID is already in use.", "code": 410}, 410

        sql = f'INSERT INTO userlog (user_id, user_pw) VALUES("{_userId}", "{_userPw}")'
        cursor.execute(sql)

        db.commit()
        db.close()

        return {"message": "Your ID has been successfully registered!", "code": 200}, 200

    except SyntaxError as e:
        return {'error':str(e)}


def login():
    return  'login'