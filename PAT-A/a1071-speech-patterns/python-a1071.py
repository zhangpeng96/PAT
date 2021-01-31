"""
    @name     : a1071
    @version  : 21.0131
    @author   : zhangpeng96
    @time     : 14'20"
    @accepted : all
"""

import re
from collections import Counter

text = input()
text = re.sub(r'[^A-z,\s,0-9]', ' ', text.lower())
count = sorted(Counter(text.split()).most_common(), key=lambda x:(-x[1], x[0]))

print(count[0][0], count[0][1])
