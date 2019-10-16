#-*-coding:utf-8-*-
import time
import random

USER_APPID = '1254277469'
USER_UIN = '100001332514'

TVPC_URL = '.oss.vpc.tencentyun.com:8080/tvpc/api'
REGION = ['gz','bj']

QC_SECRET_KEY = 'ZyFMI4fHoBPUPB4rUwGsJbjfQ0PeilhT'
QC_SECRET_ID  = 'AKID6KPPFvynyxlOp5lJE0c4MSQGvOgnsUAk'


PARAM = {
    "Action": "RegisterInstancesFromForwardLBFourthListeners",
    "loadBalancerId": "lb-b72dk3n0",
    "Region":"gz",
    "backends": [
    {
        "port": 6666,
        "instanceId": "ins-5pytqz5s",
        "listenerId": "lbl-mdk35218",
        "weight": 10
    }
    ],
    "Timestamp":int(time.time()),
    "Nonce":random.randint(10000,99999)
}
