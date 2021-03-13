def time_to_int(string):
    h, m, s = map(int, string.split(':'))
    return h*3600 + m*60 + s

"""
18:00:01 64801 , 23:07:01 83221
04:09:59 14999 , 11:30:08 41408
11:35:50 41750 , 13:00:00 46800
23:45:00 85500 , 23:55:50 86150
13:00:00 46800 , 17:11:22 61882
06:30:50 23450 , 11:42:01 42121
17:30:00 63000 , 23:50:00 85800
"""

people = []
count = int(input())
for _ in range(count):
    enter, quit = map(lambda x:time_to_int(x), input().split())
    people.append( (enter, quit-enter, quit) )

people.sort()
print(people)

