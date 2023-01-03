def single_element(iters):
    r = 0
    for i in iters:
        r ^= i
    return r

print(single_element([1,1,1,1,2,1]))