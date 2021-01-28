"""
    @name     : a1065
    @version  : 21.0128
    @author   : zhangpeng96
    @time     : 19'15"
    @accepted : all
"""

partner = {}

def dog(v):
    w = partner.get(v, False)
    if w:
        if w not in visitor_pool: return True
    else:
        return True
    return False


n = int(input())
for _ in range(n):
    cp1, cp2 = input().split()
    partner[cp1] = cp2
    partner[cp2] = cp1

m = int(input())
visitor = input().split()
visitor_pool = set(visitor)

single = sorted(filter(dog, visitor))
count = len(single)
if count:
    print(count)
    print(' '.join(single))
else:
    print(count)
