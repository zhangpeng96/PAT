/*
    @name      : b1085
    @version   : 20.0511.2
    @author    : zhangpeng96
    @test_time : 223'40"
    @pass_rate : all
*/

#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

struct node {
    string school;
    int score;
    int count;
};

struct data {
    float score;
    int count;
};

bool cmp(node a, node b) {
    if (a.score != b.score) {
        return a.score > b.score;
    }
    if (a.count != b.count) {
        return a.count < b.count;
    }
    return a.school < b.school;
}


int main() {
    ios::sync_with_stdio(false);
//	freopen("test_point.txt", "r", stdin);

    vector<node> nodes;
    map<string, data> item;
    map<char, float> grade_weight;
    grade_weight['A'] = 1;
    grade_weight['B'] = 1/1.5;
    grade_weight['T'] = 1.5;

    int count;
    cin >> count;

    for (int i = 0; i < count; i++) {
        string school, pass_id;
        float score;

        cin >> pass_id >> score >> school;
        score *= grade_weight[pass_id[0]];
        transform(school.begin(), school.end(), school.begin(), ::tolower);

        if (item.count(school)) {
            item[school].score += score;
            item[school].count ++;
        } else {
            item.insert(make_pair(school, data {score, 1}));
        }
    }

    for (auto &x : item) {
        nodes.push_back(node {x.first, (int)x.second.score, x.second.count});
    }
    sort(nodes.begin(), nodes.end(), cmp);

    int prev_score = -1;
    int order, rank;
    order = 0;
    rank = 0;

    cout << nodes.size() << endl;
    for (auto &x: nodes) {
        order ++;
        if (prev_score != x.score) {
            rank = order;
        }
        prev_score = x.score;
        cout << rank << " " << x.school << " " << x.score << " " << x.count << endl;
    }

    return 0;
}

