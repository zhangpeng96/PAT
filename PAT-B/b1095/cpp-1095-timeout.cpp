#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>

using namespace std;

struct node {
    string id, level;
    int score, room, date, order;
};

bool cmp(const node &a, const node &b) {
    if (a.score != b.score) {
        return a.score > b.score;
    } else {
        return a.id < b.id;
    }
}

bool cmp2(const pair<int, int> &a, const pair<int, int> &b) {
    if (a.second != b.second) {
        return a.second > b.second;
    } else {
        return a.first < b.first;
    }
}

int main() {
    int m, k;
    cin >> m >> k;
    vector<node> record(m); // 必须用()
    for (int i = 0; i < m; i++) {
        string id;
        cin >> id >> record[i].score;
        record[i].level = id[0];
        record[i].id = id;
        record[i].room = stoi(id.substr(1,3));
        record[i].date = stoi(id.substr(4,6));
        record[i].order = stoi(id.substr(10,3));
    }
    sort(record.begin(), record.end(), cmp);
    for (int i = 0; i < k; i++) {
        int op;
        string arg;
        cin >> op >> arg;
        cout << "Case " << i+1 << ": " << op << " " << arg << endl;
        if (op == 1) {
            int count = 0;
            for (int j = 0; j < m; j++) {
                if (record[j].level == arg) {
                    cout << record[j].id << " " << record[j].score << endl;
                    count ++;
                }
            }
            if (!count)
                cout << "NA" << endl;
        } else if (op == 2) {
            int count = 0, sum = 0;
            for (int j = 0; j < m; j++) {
                if (record[j].room == stoi(arg)) {
                    count ++;
                    sum += record[j].score;
                }
            }
            if (count)
                cout << count << " " << sum << endl;
            else
                cout << "NA" << endl;
        } else if (op == 3) {
            unordered_map<int, int> ts;
            for (int j = 0; j < m; j++) {
                if (record[j].date == stoi(arg)) {
                    ts[record[j].room] ++;
                }
            }
            vector<pair<int, int>> v(ts.begin(), ts.end());
            if (ts.size() == 0) {
                cout << "NA" << endl;
            } else {
                sort(v.begin(), v.end(), cmp2);
                for (auto i: v)
                    cout << i.first << " " << i.second << endl;
            }
        }
    }
    return 0;
}
