"""
    @name     : a1151
    @version  : 21.0308
    @author   : zhangpeng96
    @time     : 34'00"
    @accepted : p4 timeout
"""

import sys
sys.setrecursionlimit(20000)
from collections import defaultdict


queries, count = map(int, input().split())
in_order = [0] + list(map(int, input().split()))
pre_order = [0] + list(map(int, input().split()))

pos = defaultdict(int)
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
    if not pos[a] and not pos[b]:
        print('ERROR: {} and {} are not found.'.format(a, b))
    elif not pos[a] or not pos[b]:
        print('ERROR: {} is not found.'.format(b if pos[a] else a))
    else:
        lca(a, b, 1, count, 1)
