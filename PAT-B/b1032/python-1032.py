'''
    @name      : b1032
    @version   : 20.0512
    @author    : zhangpeng96
    @test_time : 20'17"
    @pass_rate : p3 timeout
'''

'''
0 答案正确 23ms   2984 KB
1 答案正确 21ms   3024 KB
2 答案正确 21ms   2916 KB
3 运行超时 -- 0 KB
'''

def insert_dict(strs):
    key, value = strs.split()
    key, value = int(key), int(value)
    if dicts.get(key):
        dicts[key] += value
    else:
        dicts[key] = value

dicts = {}

# count = int('6')
count = int(input())
[insert_dict(input()) for _ in range(count)]

print('{} {}'.format(*max(dicts.items(), key = lambda x:x[1])))


