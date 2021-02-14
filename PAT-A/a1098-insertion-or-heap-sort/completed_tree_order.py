

def pre_order(root):
    if root >= len(seq): return
    print(' {} ->'.format(seq[root]), end='')
    pre_order(root*2)
    pre_order(root*2+1)

def in_order(root):
    if root >= len(seq): return
    in_order(root*2)
    print(' {} ->'.format(seq[root]), end='')
    in_order(root*2+1)

def post_order(root):
    if root >= len(seq): return
    post_order(root*2)
    post_order(root*2+1)
    print(' {} ->'.format(seq[root]), end='')

seq = [None, 9, 17, 65, 32, 45, 78, 87, 53]
post_order(1)
