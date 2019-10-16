#-*-coding:utf-8 -*-
import json
from urllib import request

class HttpUtil(object):
    @classmethod
    def application_json(cls, url, data_dict):
        #module:tvpc-post
        '''
        :param url:请求url
        :param data_dict:字典类型的参数
        :return:
        '''
        req = request.Request(url, bytes(json.dumps(data_dict), 'utf-8')) #self._data先转化为json格式的字符串，再字节化
        response = request.urlopen(req).read()
        return response

    @classmethod
    def application_form(cls,data_str,module=None):
        '''
        :param url:请求url
        :param data_str:字符串类型的参数
        :return:
        '''
        if module:
            if module == 'lb':
                module_url = 'https://'+module+'.api.qcloud.com/v2/index.php'
            else:
                module_url = 'https://'+module+'.tencentcloudapi.com/'
        else:
            module_url = 'https://vpc.tencentcloudapi.com/'
        #module_url = 'https://cvm.ap-shenzhen-fsi.tencentcloudapi.com/'    
        #module:cloudapi-post
        req = request.Request(module_url,bytes(data_str,'utf-8'))
        response = request.urlopen(req).read()
        return response

if __name__ == '__main__':

    tmp = 'Action=DescribeInstances&InstanceIds.0=ins-09dx96dg&Limit=20&Nonce=11886&Offset=0&Region=ap-guangzhou&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3EXAMPLE&Timestamp=1465185768&Version=2017-03-12&Signature=LK5weX2UNp/aVXL5CSPv8mKj+AM='
    #ata = {}
    print(HttpUtil.application_form(tmp))
