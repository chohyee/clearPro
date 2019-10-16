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

    def DescribeRegions(self):
        param = {
            "Action":"DescribeRegions",
            "Version":"2017-03-12",
            "SecretId":QC_SECRET_ID,
            "Timestamp":int(time.time()),
            "Nonce":random.randint(10000,99999)
        }
        return self._YunApiHandle(param,module='cvm')

    #clb-v2接口
    def RegisterInstancesFromForwardLBFourthListeners(self):
        param = PARAM
        print(param)
        return self._YunApiHandle(param,module='lb')
    
    #clb-v3
    def LBV3(self, params):
        return self._YunApiHandle(params, module='clb')
    def LBDES(self, request_id):
        param = {
            "Action":"DescribeTaskStatus",
            "Region":"ap-jinan-ec",
            "Version":"2018-03-17",
            "TaskId":request_id,
            "SecretId":QC_SECRET_ID,
            "Timestamp":int(time.time()),
            "Nonce":random.randint(10000,99999)
        }
        start_time = time.time()
        while time.time() - start_time < 1000:
            rsp = self._YunApiHandle(param, module='clb')
            print(rsp)
            status = rsp['Response'] ['Status']
            if status == 0:
                return
            elif status == 1:
                raise RuntimeError("request id exec failed : %s"%request_id)
            elif status ==2:
                time.sleep(2)
            else :
                raise RuntimeError("no expect status!")
        else:
            raise RuntimeError("in expect time not done!")
    
if __name__ == '__main__':

    #print(YUNAPI().DescribeVpnGateways('ap-chengdu'))
    #print(YUNAPI().DescribeAddresses('ap-chengdu'))
    #print(YUNAPI().DescribeZones('ap-jinan-ec'))
    #rsp = YUNAPI().DescribeRegions() #dict
    #for _ in rsp['Response']['RegionSet']:
    #    print(YUNAPI().DescribeZones(_['Region']), end='\n')
    #print(YUNAPI().CreateListener(params={
    #    "Action":"CreateListener",
    #    "Region":"ap-jinan-ec"
    #}))
    
    l4_num = 100
    l7_num = 100
    lb_id = "lb-b7bbn0gq"
    
    #创建监听器
    pa1 = {
    "Action":"CreateListener",
    "Region":"ap-jinan-ec",
    "Version":"2018-03-17",
    "LoadBalancerId":lb_id,
    #"Ports":[20],
    "Protocol":"TCP",
    "HealthCheck":{"HealthSwitch":1, "HttpCode":15},
    "Timestamp":int(time.time()),
    "Nonce":random.randint(10000,99999),
    "SecretId":QC_SECRET_ID
    }
    
    cvm1 = ["10.204.0.17","10.204.0.15","10.204.0.16","10.204.0.18","10.204.0.2","10.204.0.28","10.204.0.43","10.204.0.6","10.204.0.9","10.204.0.8"]
    cvm2 = ["10.204.0.14","10.204.0.21","10.204.0.25","10.204.0.26","10.204.0.33","10.204.0.36","10.204.0.37","10.204.0.40","10.204.0.42","10.204.0.46"]
    
    #绑定rs
    pa2 = {
    "Action":"RegisterTargets",
    "Region":"ap-jinan-ec",
    "Version":"2018-03-17",
    "Timestamp":int(time.time()),
    "Nonce":random.randint(10000,99999),
    "SecretId":QC_SECRET_ID,
    "LoadBalancerId":lb_id,
    #"ListenerId":None,
    #"Targets":None
    }
    
    #删除监听器
    pa3 = {
    "Action":"DeleteListener",
    "Region":"ap-jinan-ec",
    "Version":"2018-03-17",
    "Timestamp":int(time.time()),
    "Nonce":random.randint(10000,99999),
    "SecretId":QC_SECRET_ID,
    "LoadBalancerId":lb_id,
    "ListenerId":None
    }

    pa4 = {
    "Action":"DescribeListeners",
    "Region":"ap-jinan-ec",
    "Version":"2018-03-17",
    "Timestamp":int(time.time()),
    "Nonce":random.randint(10000,99999),
    "SecretId":QC_SECRET_ID,
    "LoadBalancerId":lb_id,
    "Protocol":None,
    "Port":None
    }



    ports_4 = list(range(10200,10250))
    pa1['Ports'] = ports_4
    rsp = YUNAPI().LBV3(pa1)
    print(rsp)
    YUNAPI().LBDES(request_id=rsp['Response']['RequestId'])
    listeners = rsp['Response']['ListenerIds']
    
    targets_list = []
    rsport = ports_4[0]
    cvm_ip_list = cvm1 + cvm2
    for lis in listeners:
        for cvm in cvm_ip_list:
            target = {"Port":rsport, "Type":"ENI","EniIp":cvm}
            targets_list.append(target)
        print(targets_list)
        pa2['Targets'] = targets_list
        pa2['ListenerId'] = lis
        tmp = YUNAPI().LBV3(pa2)
        YUNAPI().LBDES(request_id=tmp['Response']['RequestId'])
        targets_list = []
        rsport += 1
