#-*-coding:utf-8-*-
import hashlib
import hmac
import base64
#from config import *
import urllib.request

class Tools(object):
    @classmethod
    def flattening_dict(cls,param,targetKey=''):
        '''扁平化dict类型的param''' 
        target = {}
        for k,v in param.items():
            if isinstance()

        return target
                
       
    @classmethod    
    def create_url_with_signStr(cls,key,dict_data,module=None):
        '''
        cloudapi的请求进行鉴权，获取Signature参数
        yunapi鉴权，传入字典类型的data，返回包含加密的signature的字符串
        :param dict_data:
        :return:
        '''
        dic_sort_data_list = sorted(dict_data.keys())
        request_str = ''
        for index,itm in enumerate(dic_sort_data_list,start=1):
            if isinstance(dict_data[itm],str):
                value = dict_data[itm]
            else:
                value = str(dict_data[itm])
            if index < len(dic_sort_data_list):
                request_str = request_str+itm+'='+value+'&'
            else:
                request_str = request_str+itm+'='+value
        #获取POST请求的signature
        if module:
            module_url = 'POST'+module+'.tencentcloudapi.com/?'
        else:
            module_url = 'POSTvpc.tencentcloudapi.com/?'
        print(module_url)
        signature = Tools.sign_str(key,module_url+request_str,hashlib.sha1)
        signature_parse = urllib.parse.quote(str(signature,'utf-8'))
        return request_str+'&Signature='+signature_parse

    @classmethod
    def sign_str(cls,secret_key,str,hash_method):
        hmac_str = hmac.new(secret_key.encode('utf-8'),str.encode('utf-8'),hash_method).digest()
        print(hmac_str)
        return base64.b64encode(hmac_str)




if __name__ == '__main__':
    param = {
            'Action' : 'DescribeInstances',
            'InstanceIds.0' : 'ins-09dx96dg',
            'Limit' : 20,
            'Nonce' : 11886,
            'Offset' : 0,
            'Version': '2017-03-12',
            'Region' : 'ap-guangzhou',
            'SecretId' : 'AKIDz8krbsJ5yKBZQpn74WFkmLPx3EXAMPLE',
            'Timestamp' : 1465185768
    }
    result = Tools.create_url_with_signStr(SECRET_KEY,param)
    print(result)
