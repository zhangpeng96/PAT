'''
    @name      : a1005
    @version   : 21.0101
    @author    : zhangpeng96
    @test_time : 4'40"
    @pass_rate : all
'''

portal = '12345'
# portal = input()
sums = sum(map(int, portal))
letter = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

print(
    ' '.join( map(lambda x: letter[int(x)], str(sums)) )
)
