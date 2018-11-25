#from tvpc_interface import TVPC
import random
from Tools import *
from request_handle import HttpUtil
from config import *
import time
import json
import copy

#1.先describe一下VPN
#2.选出vpn状态不为6的


class YUNAPI(object):
    '''
    def __init__(self):
        self.param = {
        "Noce" : random.randint(10000,99999),
        "SecretId" : QC_SECRET_ID,
        "Timestamp" : int(time.time()),
        "Version" : "2017-03-12"
        }
    '''
    def _YunApiHandle(self,param):
        data_str_with_signature = Tools.create_url_with_signStr(QC_SECRET_KEY, param)
        response = HttpUtil.application_form(data_str_with_signature)
        response_json = json.loads(str(response,'utf-8'))
        return response_json

    def DescribeVpnGateways(self,Offset=None,Limit=None,Region=None):
        param = {
                'Action' : 'DescribeVpnGateways',
                'Limit' : 20 if Limit==None else Limit,
                'Nonce' : random.randint(10000,99999),
                'Offset' : 0,
                'Version': '2017-03-12',
                'Region' : 'ap-guangzhou' if Region==None else Region,
                'SecretId' : QC_SECRET_ID,
                'Timestamp' : int(time.time())
        }
        return self._YunApiHandle(param)


    def DescribeAddresses(self,region=None):
        param = {
                "Action":"DescribeAddresses",
                "Version":"2017-03-12",
                "Region":"ap-guangzhou" if region==None else region,
                "Offset":0,
                "SecretId":SECRET_ID,
                "Timestamp":int(time.time()),
                "Nonce":random.randint(10000,99999)
        }
        return self._YunApiHandle(param)
        '''
        data_str_with_signature = Tools.create_url_with_signStr(SECRET_KEY, param)
        response = HttpUtil.application_form(data_str_with_signature)
        response_json = json.loads(str(response,'utf-8'))
        print(type(response_json))
        return response_json
        '''


    def DescribeZones(self,region=None):
        param = {
            "Action":"DescribeZones",
            "Version":"2017-03-12",
            "Region":"ap-guangzhou" if region==None else region,
            "SecretId":SECRET_ID,
            "Timestamp":int(time.time()),
            "Nonce":random.randint(10000,99999)
        }
        data_str_with_signature = Tools.create_url_with_signStr(SECRET_KEY, param,module='cvm')
        response = HttpUtil.application_form(data_str_with_signature,module='cvm')
        response_json = json.loads(str(response,'utf-8'))
        print(type(response_json))
        return response_json


if __name__ == '__main__':
    '''
    param = {
            'Action' : 'DescribeVpnGateways',
            'Limit' : 20,
            'Nonce' : random.randint(10000,99999),
            'Offset' : 0,
            'Version': '2017-03-12',
            'Region' : 'ap-guangzhou' if region==None else region,
            'SecretId' : SECRET_ID,
            'Timestamp' : int(time.time())
    }
    data_str_with_signature = Tools.create_url_with_signStr(SECRET_KEY,param)
    
    s = HttpUtil.application_form(data_str_with_signature)
    #tmp = 'Action=DescribeVpnGateways&Limit=20&Nonce=11886&Offset=0&Region=ap-guangzhou&SecretId=AKIDDKnIcpaklcHk1DbOJPPPGvQjuuTyqQNB&Timestamp=1465185768&Version=2017-03-12&Signature=3WeCVXnoaioHQpt8qOJlHiLCoRE%3d'
    #s = HttpUtil.application_form(tmp)
    print(data_str_with_signature)
    print(s)
    '''
    print(YUNAPI().DescribeVpnGateways('ap-chengdu'))
    print(YUNAPI().DescribeAddresses('ap-chengdu'))
    print(YUNAPI().DescribeZones('ap-jinan-ec'))
