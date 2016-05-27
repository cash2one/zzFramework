# -*- coding: utf-8 -*-
from ...tools.random_gen import random_phone_number
from ...tools.read_xml import ReadXML
from ...tools.encrypt import Encrypt
import requests
import json
from ...tools.logger import log


class User:
    def __init__(self):
        r_phone = random_phone_number()
        self.mobile = self.username = self.password = r_phone
        self.url = ReadXML('zhigou.xml').get_url('AddUser')
        print self.mobile

    def signup(self):
        param = {
            "p_username": self.username,
            "p_mobile": self.mobile,
            "p_password": Encrypt().encrypt(self.username, 'SHA1')
        }
        param['sign'] = Encrypt().sign(param)
        print param
        session = requests.session()
        session.headers.update({'Content-Type': 'application/json'})
        params_json = json.dumps(param)
        response = session.post(self.url, params_json)
        log(response.content, 'add a new user', 'info')
        return json.loads(response.content)['p_userid']

