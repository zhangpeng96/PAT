

def dog(v):
    w = partner.get(v, False)
    if w:
        if w not in visitor: return True
    else:
        return True
    return False



partner = {}
n = int(input())
for _ in range(n):
    cp1, cp2 = input().split()
    partner[cp1] = cp2
    partner[cp2] = cp1

m = int(input())
visitor = input().split()

single = sorted(filter(dog, visitor))
count = len(single)
if count:
    print(count)
    print(' '.join(single))
else:
    print(count)
