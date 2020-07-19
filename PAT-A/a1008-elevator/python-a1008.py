
requests = map(int, '3 2 3 1'.split())

floor = 0
timer = 0

for request in requests:
    pos = request - floor
    if pos > 0:
        timer += 6 * pos
        print(floor, '->', request, pos, timer)
    elif pos < 0:
        timer += 4 * abs(pos)
        print(floor, '<-', request, pos, timer)
    floor = request
    timer += 5

print(timer)
