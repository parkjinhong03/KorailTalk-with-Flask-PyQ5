import requests
import json
from PyQt5.QtWidgets import *
from Layout.Login import user_token

class ClickFunc:
    def Login(self, _userID, _userPW):
        url = "http://10.156.147.138:5000/user"

        dic = {
            'func': 'login',
            'id': _userID,
            'pw': _userPW
        }

        res = requests.post(url=url, data=dic)
        status_code = res.status_code

        if status_code == 410:
            QMessageBox.about(self, 'Error', 'Please enter your ID again.')
        elif status_code == 411:
            QMessageBox.about(self, 'Error', 'Please enter your PASSWORD again.')
        elif status_code == 200:
            res_data = json.loads(res.text)
            user_token.access_token = res_data['access_token']
            QMessageBox.about(self, 'Complete', 'Login succeeded!')

    def Signup(self, _userID, _userPW, _userPWC):
        url = "http://10.156.147.138:5000/user"

        dict = {
            'func': 'signup',
            'id': _userID,
            'pw': _userPW,
            'pw_check': _userPWC
        }

        res = requests.post(url=url, data=dict)
        print(res.text)