'''
    @name      : b1027
    @version   : 20.0515
    @author    : zhangpeng96
    @test_time : 
    @pass_rate : p0,p3 format error
'''

def star_count(n):
    return 1 + 2 * (n**2 - 1)

def star_width(n):
    return 2 * n - 1

def draw_sand_glass(n, token = '*'):
    stars = [star_width(i) for i in range(1, n+1)]
    width = max(stars)
    formats = '{:^' + str(width) + '}'
    for star in stars[::-1] + stars[1:]:
        print(formats.format(token * star ))

def greatest_use(provide):
    count = 1
    while star_count(count) <= provide:
        count += 1
    count -= 1
    return count, provide - star_count(count)


# input_str = input()
input_str = '8 *'
provide, token = int(input_str.split()[0]), input_str.split()[1]
count, remain = greatest_use(provide)

draw_sand_glass(count, token)
print(remain)
