'''
    @name      : b1069
    @version   : 
    @author    : zhangpeng96
    @test_time : 
    @pass_rate : p0, p3 failed
'''

def main():
    m, n, s = list(map(int, input().split()))
    data = []
    result = []
    data = list(input() for i in range(0, m))
    for i in range(s-1, len(data), n):
        if data[i] in result:
            for j in range(i, len(data)):
                if data[j] not in data:
                    result.append(data[j])
                    break
        else:
            result.append(data[i])

    if len(result):
        for r in result:
            print(r)
    else:
        print('Keep going...')


if __name__ == '__main__':
    main()