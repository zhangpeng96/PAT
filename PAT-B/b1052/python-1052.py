"""
    @name     : b1052
    @version  : 21.0125
    @author   : zhangpeng96
    @time     : 50'00"
    @accepted : all
"""

import sys
import re

hands = sys.stdin.buffer.readline()
eyes = sys.stdin.buffer.readline()
mouths = sys.stdin.buffer.readline()
count = int(input())

parts = [tuple(map(int, input().split())) for _ in range(count)]

r = re.compile(rb'(?<=\[)(.*?)(?=\])')
hands = r.findall(hands)
eyes = r.findall(eyes)
mouths = r.findall(mouths)

for p1, p2, p3, p4, p5 in parts:
    if 0<p1<=len(hands) and 0<p2<=len(eyes) and 0<p3<=len(mouths) and 0<p4<=len(eyes) and 0<p5<=len(hands):
        line = hands[p1-1] + b'(' + eyes[p2-1] + mouths[p3-1] + eyes[p4-1] + b')' + hands[p5-1] + b'\n'
        sys.stdout.buffer.write(line)
    else:
        sys.stdout.buffer.write(b'Are you kidding me? @\/@\n')
