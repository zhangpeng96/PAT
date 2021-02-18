
class Apply():
    def __init__(self, appid, s):
        self.appid = appid
        self.exam, self.inter, *self.choice = map(int, s.split())
        self.final = (self.exam + self.inter) / 2
    def __eq__(self, other):
        return (self.exam == other.exam) and (self.final == other.final) and (self.inter == other.inter) and (self.choice == other.choice)
    def __repr__(self):
        return 'e:{} i:{} f:{} ({}) | '.format(self.exam, self.inter, self.final, ' '.join(map(str, self.choice)))

class School():
    def __init__(self, quota):
        self.quota = quota
        self.apply = []
    def __bool__(self):
        return bool(self.quota) if self.quota >= 0 else False
    def accept(self, appid):
        self.quota -= 1
        self.apply.append(appid)
    def __repr__(self):
        return 'Q:{} ({}) | '.format(self.quota, ' '.join(map(str, self.apply)))


apply_n, school_n, choice_n = map(int, input().split())
school = [ School(int(x)) for x in input().split() ]

applies = [ Apply(i, input()) for i in range(apply_n) ]
applies.sort(key=lambda x:(x.final, x.exam), reverse=True)

# print(applies)

for i, app in enumerate(applies):
    for choice in app.choice:
        if school[choice]:
            school[choice].accept(app.appid)
            same_rank_choice = choice
            break
        else:
            # print(app, applies[i-1])
            if app == applies[i-1]:
                school[same_rank_choice].accept(app.appid)
                # print('eq')
                break

for sch in school:
    print(*sorted(sch.apply))