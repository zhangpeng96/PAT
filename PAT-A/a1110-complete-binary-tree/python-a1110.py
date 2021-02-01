"""
    @name     : a1110
    @version  : 21.0201
    @author   : zhangpeng96
    @time     : 30'00"
    @accepted : all
    @desc     : https://blog.csdn.net/bbwqsb/article/details/107539800
"""

def node_ptr(left, right):
    if left == '-':
        left = -1
    else:
        left = int(left)
    if right == '-':
        right = -1
    else:
        right = int(right)
    return left, right

def find_root(nodes):
    pool = set([i for i in range(len(nodes))])
    for node in nodes:
        pool -= set(node)
    return pool.pop()

def level_traversal(root, nodes):
    queue, count, last = [], len(nodes), -1
    queue.append(root)
    while count:
        ptr = queue.pop(0)
        if ptr == -1:
            return 'NO', root
        else:
            last = ptr
        queue.append(nodes[ptr][0])
        queue.append(nodes[ptr][1])
        count -= 1
        # print(queue)
    return 'YES', last


count = int(input())
nodes = [ node_ptr(*input().split()) for _ in range(count) ]
root = find_root(nodes)

print('{} {}'.format(*level_traversal(root, nodes)))
