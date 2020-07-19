"""
    @name      : a1008
    @version   : 20.0719
    @author    : zhangpeng96
    @test_time : 12'00"
    @pass_rate : all
"""

requests = map(int, input().split()[1:])
# requests = map(int, '3 2 3 1'.split()[1:])

floor = 0
timer = 0

for request in requests:
    pos = request - floor
    if pos > 0:
        timer += 6 * pos
    elif pos < 0:
        timer += 4 * abs(pos)
    floor = request
    timer += 5

print(timer)
