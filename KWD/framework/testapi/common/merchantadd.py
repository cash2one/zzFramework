#coding:utf-8
from ...tools.random_gen import random_string, random_phone_number, random_number_str
from ...tools.encrypt import Encrypt
import requests
import json
from ...tools.read_xml import ReadXML
import cx_Oracle
from ...tools.config import Config


class MerchantAdd:
    def __init__(self, userid):
        self.userid = userid
        self.session = requests.session()
        self.session.headers.update({'Content-Type': 'application/json'})
        self.best_id = '100000' + random_number_str(3)

    def _changebestid(self):
        self.best_id = '100000' + random_number_str(3)

    def _signandpost(self, param, name):
        sig = Encrypt().sign(param)
        param['sign'] = sig
        params_json = json.dumps(param)
        print params_json

        url = ReadXML('zhigou.xml').get_url(name)
        return self.session.post(url, params_json).content

    def _getmerchantid(self):
        con = cx_Oracle.connect(Config().get_oracle_connect())
        cur = con.cursor()
        cur.execute("select merchantid from user_merchant t where t.userid='{0}'".format(self.userid))
        return cur.fetchone()[0]

    def _getbestid(self):
        con = cx_Oracle.connect(Config().get_oracle_connect())
        cur = con.cursor()
        cur.execute("select bestid from u_bestbinding t where t.userid='{0}'".format(self.userid))
        try:
            return cur.fetchone()[0]
        except TypeError:
            print 'merchant did not bind a BEST id!'
            return None

    def addstep1(self):
        ran_str = random_string(15)
        param = {'p_userid': self.userid,
                  'p_enterpriseName': ran_str,
                  'p_enterpriseCode': ran_str,
                  'p_locationid': '110101',
                  'p_adress': ran_str,
                  'p_manageType': ran_str,
                  'p_referrer': 0,
                  'p_contacter': ran_str,
                  'p_contacterMobile': random_phone_number(),
                  'p_contacterEmail': ''
                 }
        return self._signandpost(param, 'AddStep1')

    def addstep2(self):
        param = {'p_userid': self.userid,
                 'p_attachcount': 6,
                 'p_attachlist': '1[,]attach/ceshi/1.jpg[,]20180102[,][;]'
                                 '2[,]attach/ceshi/4.jpg[,]20180203[,][;]'
                                 '3[,]attach/ceshi/4.jpg[,]20180203[,][;]'
                                 '4[,]attach/ceshi/4.jpg[,]20180203[,][;]'
                                 '5[,]attach/ceshi/4.jpg[,]20180203[,][;]'
                                 '6[,]attach/ceshi/4.jpg[,]20180203[,][;]'
                 }
        return self._signandpost(param, 'AddStep2')

    def addstep3(self):
        param = {'p_userid': self.userid,
                 'p_foundedtime': '20111111',
                 'p_registeredcapital': '',
                 'p_yearSalerroom': '',
                 'p_brand': '',
                 'p_ecinfo': '',
                 'p_offlineinfo': ''
                 }
        return self._signandpost(param, 'AddStep3')

    def bind(self):
        param = {'user_id': self.userid,
                 'user_name': random_string(15),
                 'user_type': '2',
                 'id_code': self.best_id,
                 'BEST_user_id': self.best_id,
                 'BEST_password': Encrypt(pwd_key='111111').encrypt(self.best_id, 'MD5')}
        res = self._signandpost(param, 'Bind')
        print res
        if res != '{}':
            self._changebestid()
            res = self.bind()
        return res

    def unbind(self):
        self.best_id = self._getbestid()
        param = {'user_id': self.userid,
                 'BEST_user_id': self.best_id,
                 'BEST_password': Encrypt(pwd_key='111111').encrypt(self.best_id, 'MD5')}
        return self._signandpost(param, 'UnBind')

    def openshop(self):
        param = {'p_userid': self.userid,
                 'p_shopname': random_string(15)}
        return self._signandpost(param, 'OpenShop')

    def getbasicstatus(self):
        param = {'p_userid': self.userid}
        return self._signandpost(param, 'GetBasicStatus')

    def getapplylist(self):
        param = {'p_userid': self.userid}
        return self._signandpost(param, 'GetApplyList')

    def approveapply(self, status):
        p_merchantid = self._getmerchantid()
        param = {'p_opid': 1,
                 'p_merchantid': p_merchantid,
                 'p_status': status,
                 'p_approvememo': random_string(15)}
        return self._signandpost(param, 'ApproveApply')

    def getbasicinfo(self):
        p_merchantid = self._getmerchantid()
        param = {'p_opid': 1,
                 'p_username': '',
                 'p_merchantid': p_merchantid,
                 'p_createtime': '10111111',
                 'p_mobile': '',
                 'p_status': 4,
                 'p_approvename': ''}
        return self._signandpost(param, 'GetBasicinfo')

