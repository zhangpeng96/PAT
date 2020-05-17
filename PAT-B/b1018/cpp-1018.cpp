/*
    @name      : b1018
    @version   : 20.0516.2
    @author    : zhangpeng96
    @test_time : 77'42"
    @pass_rate : all
*/

#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;

bool cmp(const pair<char, int> &a, const pair<char, int> &b) {
    if (a.second != b.second) {
        return (a.second > b.second);
    }
    return (a.first < b.first);
}

int decision(char a, char b) {
    if (a == b) {
        return 0;
    } else if (a == 'J' && b == 'C') {
        return -1;
    } else if (a == 'J' && b == 'B') {
        return 1;
    } else if (a == 'C' && b == 'J') {
        return 1;
    } else if (a == 'C' && b == 'B') {
        return -1;
    } else if (a == 'B' && b == 'J') {
        return -1;
    } else if (a == 'B' && b == 'C') {
        return 1;
    }
}


int main() {
    ios::sync_with_stdio(false);
//    freopen("test_point.txt", "r", stdin);

    int count, temp;
    char player_1, player_2;
    map<int, int> result_1 = {
        {1, 0}, {0, 0}, {-1, 0}
    };
    map<int, int> result_2 = {
        {-1, 0}, {0, 0}, {1, 0}
    };
    map<char, int> gesture_1 = {
        {'J', 0}, {'C', 0}, {'B', 0}
    };
    map<char, int> gesture_2 = {
        {'J', 0}, {'C', 0}, {'B', 0}
    };

    cin >> count;
    for (int i = 0; i < count; i++) {
        cin >> player_1 >> player_2;
        temp = decision(player_1, player_2);
        result_1[temp] ++;
        result_2[temp] ++;
        if (temp == 1) {
            gesture_1[player_1] ++;
        } else if (temp == -1) {
            gesture_2[player_2] ++;
        }
    }

// 这里的逻辑比较混乱，采用 map 并不是一个很好的选择
    cout << result_1[1] << " " << result_1[0] << " " << result_1[-1] << endl;
    cout << result_2[-1] << " " << result_2[0] << " " << result_2[1] << endl;

// C++ map 是无法针对 key value 分别排序，因此需要将其转换为 pair 在放入 vector 中排序
    vector<pair<char, int>> gest_1, gest_2;
    map<char, int> :: iterator it;
    for (it = gesture_1.begin(); it != gesture_1.end(); it++) {
        gest_1.push_back(make_pair(it->first, it->second));
    }
    for (it = gesture_2.begin(); it != gesture_2.end(); it++) {
        gest_2.push_back(make_pair(it->first, it->second));
    }
    sort(gest_1.begin(), gest_1.end(), cmp);
    sort(gest_2.begin(), gest_2.end(), cmp);

    cout << gest_1[0].first << " " << gest_2[0].first << endl;
}
