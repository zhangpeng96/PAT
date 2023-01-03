from collections import Counter

def dep1(iters):
    return sum(set(iters)) * 2 - sum(iters)

def dep2(iters):
    single = []
    for value, times in Counter(iters).most_common()[::-1]:
        if times == 1:
            single += [value]
        else:
            break
    return single

'''
mydict={"a":1,"b":2,"c":3}
mydict_new=dict([val,key] for key,val in mydict.items())
'''

print(dep2([1,1,2,2,3,4,4,5,4]))