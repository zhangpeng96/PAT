'''
    @name      : b1034
    @version   : 20.506
    @author    : zhangpeng96
    @test_time : 
    @pass_rate : 
'''

def gcd(a, b):
    while(b):
        a %= b
        a, b = b, a
    return a

def lcm(a, b):
    return int(a*b/gcd(a, b))

def gcd_frac(a, b):
    gcd_num = gcd(a, b)
    return int(a/gcd_num), int(b/gcd_num)

def lcm_frac(b, a, d, c):
    lcm_num = lcm(a, c)
    b = int(b * (lcm_num/a))
    d = int(d * (lcm_num/c))
    return b, d, lcm_num

def simplify(nume, deno):
    # print('>', nume, deno)
    if nume % deno:
        if nume > 0:
            add = int(nume / deno) if nume > deno else 0
            nume, deno = gcd_frac(nume, deno)
            nume = nume % deno
        elif nume < 0:
            add = int(nume / deno) if abs(nume) > deno else 0
            nume, deno = gcd_frac(nume, deno)
            if add == 0:
                nume = nume - add * deno
            else:
                nume = abs(nume - add * deno)
        elif nume == 0:
            add, nume, deno = 0, 0, 0
    else:
        add, nume, deno = int(nume/deno), 0, 0
    return (add, nume, deno)

def frac_format(nume, deno):
    if nume == None or deno == None:
        return 'Inf'
    add, nume, deno = simplify(nume, deno)
    if nume > 0:
        frac_str = '%s/%s' % (nume, deno)
    elif nume < 0:
        frac_str = '(%s/%s)' % (nume, deno)
    elif nume == 0:
        if add < 0:
            return '(%s)' % add
        elif add == 0:
            return '0'
        elif add > 0:
            return '%s' % add
    if add < 0:
        return '(%s %s)' % (add, frac_str)
    elif add == 0:
        return frac_str
    else:
        return '%s %s' % (add, frac_str)

def calc_plu(num1, num2):
    nume_a, deno_a = num1
    nume_b, deno_b = num2
    if deno_a == deno_b:
        result = (nume_a + nume_b, deno_a)
    else:
        nume_a, nume_b, deno = lcm_frac(nume_a, deno_a, nume_b, deno_b)
        result = (nume_a + nume_b, deno)
    return result

def calc_sub(num1, num2):
    return calc_plu(num1, (-num2[0], num2[1]))

def calc_mul(num1, num2):
    return (num1[0]*num2[0], num1[1]*num2[1])

def calc_div(num1, num2):
    if num2[0]:
        if num2[0] < 0:
            return calc_mul(num1, (-num2[1], -num2[0]))
        elif num2[0] > 0:
            return calc_mul(num1, (num2[1], num2[0]))
    else:
        return (None, None)

def calc(frac1, frac2):
    frac1_str, frac2_str = frac_format(*frac1), frac_format(*frac2)
    print('{} + {} = {}'.format(frac1_str, frac2_str, frac_format(*calc_plu(frac1, frac2)) ))
    print('{} - {} = {}'.format(frac1_str, frac2_str, frac_format(*calc_sub(frac1, frac2)) ))
    print('{} * {} = {}'.format(frac1_str, frac2_str, frac_format(*calc_mul(frac1, frac2)) ))
    print('{} / {} = {}'.format(frac1_str, frac2_str, frac_format(*calc_div(frac1, frac2)) ))



if __name__ == '__main__':
    # simplify(-9, 6)
    # print(gcd(-4, -12))
    # print(lcm_frac(5, 6, 2, 9))
    # print(calc_div((-5, 6), (0, 9)))
    # frac_format(0, 9)
    input_str = '2/3 -4/2'
    # input_str = '5/3 0/6'
    input_frac = list(map(lambda x:
        tuple(map(int, x.split('/'))), input_str.split()
    ))
    calc(*input_frac)
    # print(frac_format(-24, 12))
    # print(input_frac)
