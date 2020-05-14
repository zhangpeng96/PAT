'''
    @name      : b1044
    @version   : 20.0514
    @author    : zhangpeng96
    @test_time : 82'36"
    @pass_rate : all
'''

tridec_base_map = ['tret', 'jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jly', 'aug', 'sep', 'oct', 'nov', 'dec']
tridec_carry_map = ['tam', 'hel', 'maa', 'huh', 'tou', 'kes', 'hei', 'elo', 'syy', 'lok', 'mer', 'jou']

tridec_base_hex = dict(zip(tridec_base_map, '0123456789abcdef'))
tridec_carry_hex = dict(zip(tridec_carry_map, '123456789abcdef'))

def decimal_to_tridec(n, base = 13, str_map = tridec_base_map, carry_map = tridec_carry_map):
    def digit(n, base):
        if n < base:
            return [n]
        else:
            return digit(n//base, base) + [n % base]
    dig = digit(n, base)
    if len(dig) > 1:
        if dig[-1]:
            return ' '.join( list(map(lambda x:carry_map[x-1], dig[0:-1])) + list(map(lambda x:str_map[x], dig[-1:])) )
        else:
            return carry_map[dig[0]-1]
    else:
        return str_map[dig[0]]


def tridec_to_decimal(tridec_str, tridec_base = tridec_base_hex, tridec_carry = tridec_carry_hex):
    tri = tridec_str.split()
    if len(tri) > 1:
        hex_str = ''.join( list(map(lambda x:tridec_carry[x], tri[0:-1])) + list(map(lambda x:tridec_base[x], tri[-1:])) )
    else:
        if tridec_carry.get(tri[0]):
            hex_str = tridec_carry[tri[0]] + '0'
        else:
            hex_str = ''.join(map(lambda x:tridec_base[x], tri))
    return int(hex_str, 13)


count = int(input())
query_list = [input() for _ in range(count)]
# query_list = ['29', '5', 'elo nov', 'tam']

for query in query_list:
    if query.isdigit():
        print(decimal_to_tridec(int(query)))
    else:
        print(tridec_to_decimal(query))
