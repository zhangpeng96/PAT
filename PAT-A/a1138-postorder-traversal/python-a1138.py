"""
    @name     : a1138
    @version  : 21.0203
    @author   : zhangpeng96
    @time     : 15'00"
    @accepted : p4,p5 timeout
"""

def create(root, start, end):
    if start > end: return
    i = start
    while i < end and in_order[i] != pre_order[root]:
        i += 1
    create(root+1, start, i-1)
    create(root+1+(i-start), i+1, end)
    post_traversal.append(pre_order[root])


count = int(input())
pre_order = list(map(int, input().split()))
in_order = list(map(int, input().split()))

post_traversal = []
create(0, 0, count-1)
print(post_traversal[0])

