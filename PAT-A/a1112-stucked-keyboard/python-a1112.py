"""
    @name      : a1112
    @version   : 20.0720
    @author    : zhangpeng96
    @test_time : 16'54"
    @pass_rate : all
"""

# repeat = int('3')
# text = 'caseee1__thiiis_iiisss_a_teeeeeest'
repeat = int(input())
text = input()

stucked = []

for char in set(text):
    find = char*repeat
    if find in text:
        if not text.replace(find, '').count(char):
            stucked.append(char)

origin = text
for char in stucked:
    origin = origin.replace(char*repeat, char)

stucked.sort(key=text.index)

print(''.join(stucked))
print(origin)
