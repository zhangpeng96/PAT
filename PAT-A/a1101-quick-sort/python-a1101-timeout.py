
count = int(input())
elements = list(map(int, input().split()))

pivot = []

for i, elem in enumerate(elements):
    if i == 0:
        if elem < min(elements[1:]):
            pivot.append(elem)
        continue
    if i == count-1:
        if elem > max(elements[:-1]):
            pivot.append(elem)
        continue
    if max(elements[:i]) < elem < min(elements[i+1:]):
        pivot.append(elem)

pivot.sort()
print(len(pivot))
print(*pivot)
