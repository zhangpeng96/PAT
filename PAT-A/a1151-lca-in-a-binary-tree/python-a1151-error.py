"""
    @name     : a1151
    @version  : 21.0308
    @author   : zhangpeng96
    @time     : 34'00"
    @accepted : 尝试用list做pos，但是会引发更多的错误
                因为树的节点编号并不是连续的
"""

import sys
sys.setrecursionlimit(20000)


queries, count = map(int, input().split())
in_order = [0] + list(map(int, input().split()))
pre_order = [0] + list(map(int, input().split()))

pos = [0] * (count+1)
for index, node in enumerate(in_order[1:], 1):
    pos[node] = index


def lca(a, b, in_left, in_right, pre_root):
    if in_left > in_right: return
    in_root = pos[ pre_order[pre_root] ]
    in_a, in_b = pos[a], pos[b]
    # 都在左边，在左子树里找，左边界不变，右边界到根节点，新的根节点先序下一个
    if in_a < in_root and in_b < in_root:
        lca(a, b, in_left, in_root-1, pre_root+1)
    # 都在右边，在右子树里找，右边界不变，左边界从根节点开始，新的根节点是排除左子树长度后的下一个
    elif in_a > in_root and in_b > in_root:
        lca(a, b, in_root+1, in_right, pre_root+1 + (in_root - in_left))
    # 如果两个点分别在左右两个子树，说明现在的根节点就是要找的LCA
    elif (in_a < in_root and in_b > in_root) or (in_a > in_root and in_b < in_root):
        print('LCA of {} and {} is {}.'.format( a, b, in_order[in_root] ))
    # LCA竟是我自己
    elif in_a == in_root:
        print('{} is an ancestor of {}.'.format(a, b))
    elif in_b == in_root:
        print('{} is an ancestor of {}.'.format(b, a))


for _ in range(queries):
    a, b = map(int, input().split())
    if (a < 1 or a > count) and (b < 1 or b > count):
        print('ERROR: {} and {} are not found.'.format(a, b))
    elif a < 1 or a > count:
        print('ERROR: {} is not found.'.format(a))
    elif b < 1 or b > count:
        print('ERROR: {} is not found.'.format(b))
    else:
        lca(a, b, 1, count, 1)
