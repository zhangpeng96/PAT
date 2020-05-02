def star_count(rank):
    return 1 + sum([ 2*i + 1 for i in range(1, rank)]) * 2

def calc_rank(given):
    for i in range(1, 23):
        if star_count(i) > 19:
            return i-1

def star_draw(rank, star):
    # star = '*'
    star_part = [''.join([star] * (2*i+1)) for i in range(1, rank)]
    star_list = star_part[::-1] + [star] + star_part
    width_format = r'{:^' + str(len(star_list[0])) + r'}'
    print('\n'.join(map(lambda x: width_format.format(x), star_list)))


if __name__ == '__main__':
    given, star = '19 *'.split()
    given = int(given)
    rank = calc_rank(given)
    star_draw(rank, star)
    print(given - star_count(rank))