source = {'a': {'b': 1, 'c': 2}, 'd': {'e': 3, 'f': {'g': 4}}}
target = {}
def flatmap(srcDic, targetKey=''):
    for k, v in srcDic.items():
        if isinstance(v, dict):
            flatmap(v, targetKey=targetKey + k + '.')
        else:
            target[targetKey + k] = v
if __name__ == '__main__':
    flatmap(source)
    print(target)
