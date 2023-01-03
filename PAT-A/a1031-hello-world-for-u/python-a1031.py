'''
    @name      : a1031
    @version   : 20.0531
    @author    : zhangpeng96
    @test_time : 45'03"
    @pass_rate : all
'''

def calc_n(n):
    for n2 in range(3, n):
        n1s = n - n2 + 2
        if n1s <= 2 * n2 and not (n1s % 2):
            return n1s//2 , n2

# ins = 'helloworld!'
ins = input()

vert, bottom = calc_n(len(ins))
vert = vert-1

spaces = ' ' * (bottom-2)
verts_left, verts_right, bottoms = ins[:vert], ins[-vert:][::-1], ins[vert:vert+bottom]

for i in range(vert):
    print( '{}{}{}'.format(verts_left[i], spaces, verts_right[i]) )
print(bottoms)
