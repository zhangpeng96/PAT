/*
    @name     : b1095/a1153
    @version  : 21.0222
    @author   : zhangpeng96
    @time     : >60'00"
    @accepted : all
    @desc     : 不能用cout会超时
*/

#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;

bool cmp(pair<string, int> &x, pair<string, int> &y) {
    if (x.second != y.second) {
        return x.second > y.second;
    } else {
        return x.first < y.first;
    }
}

void SelectLevel(string level, vector<pair<string, int>> &record) {
    vector<pair<string, int>> v;

    for (auto i : record)
        if (i.first[0] == level[0])
            v.push_back(i);

    sort(v.begin(), v.end(), cmp);

    if (v.size())
        for (auto i : v)
            printf("%s %d\n", i.first.c_str(), i.second);
    else
        printf("NA\n");
}

void SelectRoom(string room, vector<pair<string, int>> &record) {
    int cnt = 0;
    int sum = 0;

    for (auto i : record)
        if (i.first.substr(1, 3) == room) {
            cnt++;
            sum += i.second;
        }

    if (cnt)
        printf("%d %d\n", cnt, sum);
    else
        printf("NA\n");
}

void SelectDate(string date, vector<pair<string, int>> &record) {
    unordered_map<string, int> m;

    for (auto i : record)
        if (i.first.substr(4, 6) == date)
            m[i.first.substr(1, 3)]++;

    vector<pair<string, int>> v(m.begin(), m.end());
    sort(v.begin(), v.end(), cmp);

    if (m.size())
        for (auto i : v)
            printf("%s %d\n", i.first.c_str(), i.second);
    else
        printf("NA\n");
}


int main(void) {
    int n, m, op;
    string arg;
    cin >> n >> m;

    vector<pair<string, int>> record(n);
    for (int i = 0; i < n; ++i)
        cin >> record[i].first >> record[i].second;

    for (int i = 0; i < m; i++) {
        cin >> op >> arg;
        printf("Case %d: %d %s\n", i + 1, op, arg.c_str());

        switch (op) {
            case 1:
                SelectLevel(arg, record);
                break;
            case 2:
                SelectRoom(arg, record);
                break;
            case 3:
                SelectDate(arg, record);
                break;
            default:
                printf("NA\n");
                break;
        }
    }
    return 0;
}
