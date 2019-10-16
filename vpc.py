#-*-coding:utf-8-*-
from yunapi_interface import YUNAPI


if __name__ == '__main__':
   #print( YUNAPI().DescribeVpnGateways('ap-singapore'))
   list = ['ap-guangzhou','ap-shanghai','ap-hongkong','na-toronto','ap-shanghai-fsi','ap-beijing','ap-singapore','ap-shenzhen-fsi','na-siliconvalley','ap-chengdu','eu-frankfurt','ap-seoul','ap-mumbai','na-ashburn','ap-chongqing','ap-bangkok','eu-moscow','ap-tokyo'] 
   for region in list:
       print( YUNAPI().DescribeZones(region))
   #print( YUNAPI().RegisterInstancesFromForwardLBFourthListeners())
