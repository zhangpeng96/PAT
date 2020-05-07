import re

def draw_face(sign_id, sign_set):
    sign_id = map(int, sign_id.split())
    try:
        text = '{}({}{}{}){}'.format(*map(lambda i,s: s[i-1], sign_id, sign_set))
    except:
        text = 'Are you kidding me? @\\/@'
    print(text)


regex = r'\[(.*?)\]'

# str1 = r'[╮][╭][o][~\][/~]  [<][>]'
# str2 = r' [╯][╰][^][-][=][>][<][@][⊙]'
# str3 = r'[Д][▽][_][ε][^]'

hand = [match.group(1) for match in re.finditer(regex, input(), re.MULTILINE)]
eye = [match.group(1) for match in re.finditer(regex, input(), re.MULTILINE)]
mouth = [match.group(1) for match in re.finditer(regex, input(), re.MULTILINE)]

count = int(input())
id_list = [input() for i in range(0, count)]

for sign_id in id_list:
    draw_face(sign_id, [hand, eye, mouth, eye, hand])
