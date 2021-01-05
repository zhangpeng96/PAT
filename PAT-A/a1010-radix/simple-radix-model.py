
def deci_to_radix(n, base, symbol = '0123456789abcdefghijklmnopqrstuvwxyz'):
    def digit(n, base):
        if n < base:
            return [n]
        else:
            return digit(n//base, base) + [n % base]
    return ''.join(map(lambda i: symbol[i], digit(n, base)))


def radix_to_deci(n, base, symbol = '0123456789abcdefghijklmnopqrstuvwxyz'):
    digits = map(lambda r: symbol.index(r), n[::-1])
    return sum([ digit * base ** r for r, digit in enumerate(digits) ])


# print(deci_to_radix(255, 16))
# print(radix_to_deci('ff', 16))
