"""
    @name     : a1091
    @version  : 21.0221
    @author   : zhangpeng96
    @time     : >60'00"
    @accepted : p4, p5 timeout
"""

from collections import defaultdict

def bfs(kv, iv, jv, height, length, width):
    count = 0
    queue, visited[ (kv, iv, jv) ] = [ (kv, iv, jv) ], True
    while queue:
        k, i, j = queue.pop(0)
        count += 1
        if k+1 < height and bitmap[k+1][i][j] == '1' and not visited[ (k+1, i, j) ]:
            queue.append( (k+1, i, j) )
            visited[ (k+1, i, j) ] = True

        if i+1 < length and bitmap[k][i+1][j] == '1' and not visited[ (k, i+1, j) ]:
            queue.append( (k, i+1, j) )
            visited[ (k, i+1, j) ] = True

        if j+1 < width and bitmap[k][i][j+1] == '1' and not visited[ (k, i, j+1) ]:
            queue.append( (k, i, j+1) )
            visited[ (k, i, j+1) ] = True

        if k-1 >= 0 and bitmap[k-1][i][j] == '1' and not visited[ (k-1, i, j) ]:
            queue.append( (k-1, i, j) )
            visited[ (k-1, i, j) ] = True

        if i-1 >= 0 and bitmap[k][i-1][j] == '1' and not visited[ (k, i-1, j) ]:
            queue.append( (k, i-1, j) )
            visited[ (k, i-1, j) ] = True

        if j-1 >= 0 and bitmap[k][i][j-1] == '1' and not visited[ (k, i, j-1) ]:
            queue.append( (k, i, j-1) )
            visited[ (k, i, j-1) ] = True

    return count


length, width, height, threshold = map(int, input().split())
bitmap = [ [ input().split() for _ in range(length) ] for _ in range(height) ]
visited = defaultdict(bool)
amount = 0

for k in range(height):
    for i in range(length):
        for j in range(width):
            if bitmap[k][i][j] == '1' and not visited[ (k, i, j) ]:
                count = bfs(k, i, j, height, length, width)
                if count >= threshold:
                    amount += count

print(amount)