import dis

def gcd(a, b):
    while(b):
        a %= b
        a, b = b, a
    return a


def lcm(a, b):
    return int(a*b/gcd(a, b))


if __name__ == '__main__':
    a, b = 81, 135
    # print(lcm(a, b, gcd(a, b)))
    print(
        gcd(a, b),
        lcm(a, b)
    )
    dis.dis(gcd)
