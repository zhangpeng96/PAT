"""
    @name     : a1143
    @version  : 21.0308
    @author   : zhangpeng96
    @time     : 33'48"
    @accepted : p4 timeout
"""

queries, count = map(int, input().split())
pre_order = list(map(int, input().split()))
tree = set(pre_order)


def lca_bst(a, b):
    # 对于BST来说，给出任意先序或后序即可确定树，因为BST中序是递增序列
    for node in pre_order:
        # 对于BST有性质，任意子树：左节点<根节点<右节点，因此如果有一个节点值介于左右节点
        # 那么就很有可能是它们的根节点，但要防止这样的情形：左节点a的右子节点x，和右节点b
        # 因此要用先序序列按序尝试，这样总是自上而下尝试，就不会过深遍历到子节点
        # 等于号是考虑树只有左或右子树的情形
        if (node >= a and node <= b) or (node >= b and node <= a):
            return node


for _ in range(queries):
    a, b = map(int, input().split())
    if a not in tree and b not in tree:
        print('ERROR: {} and {} are not found.'.format(a, b))
    elif a not in tree or b not in tree:
        print('ERROR: {} is not found.'.format(b if a in tree else a))
    else:
        lca = lca_bst(a, b)
        if lca == a or lca == b:
            print('{} is an ancestor of {}.'.format(lca, b if lca == a else a))
        else:
            print('LCA of {} and {} is {}.'.format(a, b, lca))
