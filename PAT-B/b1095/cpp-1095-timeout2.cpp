# include <iostream>
# include <vector>
# include <algorithm>
# include <unordered_map>

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
            cout << i.first << " " << i.second << endl;
    else
        cout << "NA" << endl;
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
        cout << cnt << " " << sum << endl;
    else
        cout << "NA" << endl;
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
            cout << i.first << " " << i.second << endl;
    else
        cout << "NA" << endl;
}


int main(void) {
    ios::sync_with_stdio(false);
    int n, m, op;
    string arg;
    cin >> n >> m;

    vector<pair<string, int>> record(n);
    for (int i = 0; i < n; ++i)
        cin >> record[i].first >> record[i].second;

    for (int i = 0; i < m; i++) {
        cin >> op >> arg;
        cout << "Case " << i+1 << ": " << op << " " << arg << endl;

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
                cout << "NA" << endl;
                break;
        }
    }
    return 0;
}