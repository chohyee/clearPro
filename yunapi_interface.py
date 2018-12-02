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
    def _YunApiHandle(self,param,module=None):
        if module:
            data_str_with_signature = Tools.create_url_with_signStr(QC_SECRET_KEY, param,module=module)
            response = HttpUtil.application_form(data_str_with_signature,module=module)
        else:
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

    def DescribeAddresses(self,Region=None):
        param = {
                "Action":"DescribeAddresses",
                "Version":"2017-03-12",
                "Region":"ap-guangzhou" if Region==None else Region,
                "Offset":0,
                "SecretId":QC_SECRET_ID,
                "Timestamp":int(time.time()),
                "Nonce":random.randint(10000,99999)
        }
        return self._YunApiHandle(param)

    def DescribeZones(self,Region=None):
        param = {
            "Action":"DescribeZones",
            "Version":"2017-03-12",
            "Region":"ap-guangzhou" if Region==None else Region,
            "SecretId":QC_SECRET_ID,
            "Timestamp":int(time.time()),
            "Nonce":random.randint(10000,99999)
        }
        return self._YunApiHandle(param,module='cvm')


if __name__ == '__main__':

    print(YUNAPI().DescribeVpnGateways('ap-chengdu'))
    print(YUNAPI().DescribeAddresses('ap-chengdu'))
    print(YUNAPI().DescribeZones('ap-jinan-ec'))
