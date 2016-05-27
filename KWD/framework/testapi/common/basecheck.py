# -*- coding: utf-8 -*-
import requests
import json
from ...tools.read_xls import ReadXls
from ...tools.encrypt import Encrypt


class BaseCheck:

    def __init__(self, url, datafile='check.xlsx', sheet_name='sheet0', ifsign=1):
        self.url = url
        self.datafile = datafile
        self.sheet_name = sheet_name
        self.ifsign = ifsign
        self.cases = ReadXls(self.datafile, sheet_name=self.sheet_name).get_data()
        self.case = None
        self.types = self.cases.pop(0)

    def _typehandle(self):
        params = dict()
        for key in self.types.keys():
            if self.case[key] == 'null':
                params[key] = None
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

    def _header(self):
        session = requests.session()
        session.headers.update({'Content-Type': 'application/json'})
        return session

    def docase(self):
        results = list()
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
        return results

        # 下面这段用于获取信息后与数据库对比
        # if res.content != '{}' and ('errorMessage' not in res.content):
        #     from tools.path import REPORT_PATH
        #     report_file = REPORT_PATH + 'report.txt'
        #     with open(report_file, 'a') as rf:
        #         rf.write('url = {0}\ndata_file={1}\nsheet_name={2}\nparams={3}\nresponse={4}\n\n\n\n'.format(
        #             url, datafile, sheet_name, params_json, res.content))

        # 下面这段用于插入信息后的对比
        # if 'AddStep' in sheet_name:
        #     print ses.post('http://192.168.7.227:8080/zhigou/P_Merchant__GetApplyList', json.dumps(
        #         {"p_userid": 26, "sign": sign({"p_userid": 26})})).content

        # 下面这段用于step3执行后恢复状态，以能够继续执行下一条用例
        # a = ses.post('http://192.168.7.227:8080/zhigou/P_Merchant__GetApplyList', json.dumps(
        #     {"p_userid": 26, "sign": sign({"p_userid": 26})})).content
        # if json.loads(a)['p_status'] == 3:
        #     print json.loads(a)['step2']
        #     deny = {"p_opid": 1, "p_merchantid": 29, "p_status": 5, "p_approvememo": "deny"}
        #     deny['sign'] = sign(deny)
        #     ses.post('http://192.168.7.227:8080/zhigou/P_Merchant__ApproveApply', json.dumps(deny))
        #     print
