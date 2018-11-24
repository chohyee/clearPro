'''
生成数据:[{"pip": "10.1.0.1", "pport": 9999}, {"pip": "10.1.0.2", "pport": 9999}],其中n表示个数
'''
def func(n):
    res = []
    i = 1
    while i < n:
        param = {"pip": "10.1.0.%s"%i,"pport": 9999}
        #print(param)
        i = i+1
        res.append(param)
    return str(res).replace("'",'"')

if __name__ == "__main__":
    print(func(100))
    

