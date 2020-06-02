'''
    @name      : a1005
    @version   : 20.0602
    @author    : zhangpeng96
    @test_time : 4'40"
    @pass_rate : all
'''

# digits = '12345'

digits = input()
summation = sum(map(int, digits))
spell_map = dict(zip('0123456789', ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']))

print(
    ' '.join( map(lambda x:spell_map[x], str(summation)) )
)
