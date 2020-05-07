import re
import sys

def input_raw():
    return sys.stdin.readline().strip()

def draw_face(sign_id, sign_set):
    sign_id = map(int, sign_id.split())
    try:
        text = '{}({}{}{}){}'.format(*map(lambda i,s: s[i-1], sign_id, sign_set))
    except:
        text = 'Are you kidding me? @\\/@'
    print(text)

regex = r'\[(.*?)\]'

hand = [match.group(1) for match in re.finditer(regex, input_raw())]
eye = [match.group(1) for match in re.finditer(regex, input_raw())]
mouth = [match.group(1) for match in re.finditer(regex, input_raw())]

count = int(input_raw())
id_list = [input_raw() for _ in range(0, count)]

for sign_id in id_list:
    draw_face(sign_id, [hand, eye, mouth, eye, hand])
