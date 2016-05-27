#coding:utf-8

from basecheck import BaseCheck
from ...tools.encrypt import Encrypt
import json


class NewUserCheck(BaseCheck):
    def __init__(self, url, datafile='check.xlsx', sheet_name='sheet0', ifsign=1, userid=None):
        BaseCheck.__init__(self, url, datafile, sheet_name, ifsign)
        self.userid = userid

    def _typehandle(self):
        params = dict()
        for key in self.types.keys():
            if self.case[key] == 'null':
                params[key] = None
            elif self.case[key] == '26':
                params[key] = self.userid
            else:
                if self.types[key] == 'int':
                    try:
                        params[key] = int(self.case[key])
                    except ValueError:
                        params[key] = self.case[key]
                elif self.types[key] == 'str':
                    params[key] = self.case[key]
                elif self.types[key] == 'password':
                    params[key] = Encrypt().encrypt(self.case[key], 'SHA1')
                elif self.types[key] == 'best':
                    try:
                        params[key] = Encrypt(pwd_key=self.case[key]).encrypt(self.case['BEST_user_id'], 'MD5')
                    except KeyError:
                        raise KeyError('Did not find key "BEST_user_id",check your data file!')
        return params

    def docase3(self):
        results = list()
        from ..common.merchantadd import MerchantAdd
        for self.case in self.cases:
            params = self._typehandle()
            if self.ifsign == 1:
                params['sign'] = Encrypt().sign(params)

            params_json = json.dumps(params)
            response = self._header().post(self.url, params_json)
            result = dict()
            result['index'] = self.cases.index(self.case) + 1
            result['params'] = params_json
            result['response'] = response.content
            result['code'] = self.case['code']
            results.append(result)

            status = json.loads(MerchantAdd(self.userid).getbasicstatus())['p_status']
            if status == 3:
                MerchantAdd(self.userid).approveapply(5)
        return results