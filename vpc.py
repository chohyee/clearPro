#from tvpc_interface import TVPC
import random
from Tools import *
from request_handle import HttpUtil
from config import *
import time
import json

#1.先describe一下VPN
#2.选出vpn状态不为6的


class YUNAPI(object):

    def DescribeVpnGateways(self,region=None):
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
        data_str_with_signature = Tools.create_url_with_signStr(SECRET_KEY, param)
        response = HttpUtil.application_form(data_str_with_signature)
        response_json = json.loads(str(response,'utf-8')) #将返回结果从二进制转换为str类型在转为json格式
        print(type(response_json))
        return response_json


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
        data_str_with_signature = Tools.create_url_with_signStr(SECRET_KEY, param)
        response = HttpUtil.application_form(data_str_with_signature)
        response_json = json.loads(str(response,'utf-8'))
        print(type(response_json))
        return response_json


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
