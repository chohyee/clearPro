from yunapi_interface import *
from config import *

if __name__ == "__main__":    
    lb_id = "lb-b7bbn0gq"
    
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
     
    for port in list(range(10081,10100)):
        pa4['Protocol'] = 'TCP'
        pa4['Port'] = port
        lis_id = YUNAPI().LBV3(pa4)['Response']['Listeners'][0]['ListenerId']
        pa3['ListenerId'] = lis_id
        rsp = YUNAPI().LBDES(request_id=YUNAPI().LBV3(pa3)['Response']['RequestId'])
