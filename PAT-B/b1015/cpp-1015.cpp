/*
    @name      : b1015
    @version   : 20.0511
    @author    : zhangpeng96
    @test_time : 
    @pass_rate : all
*/

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

struct node {
    int id, de, cai;
};

int cmp(struct node a, struct node b) {
    if ((a.de + a.cai) != (b.de + b.cai)) {
        return (a.de + a.cai) > (b.de + b.cai);
	}
	if (a.de != b.de) {
        return a.de > b.de;
	}
    return a.id < b.id;
}

int main() {
    int n, low, high;
    scanf("%d %d %d", &n, &low, &high);
    vector<node> admission[4];
    node temp;
    for (int i = 0; i < n; i++) {
        scanf("%d %d %d", &temp.id, &temp.de, &temp.cai);
        if (temp.de < low || temp.cai < low) {
		} else if (temp.de >= high && temp.cai >= high) {
            admission[0].push_back(temp);
		} else if (temp.de >= high && temp.cai < high) {
            admission[1].push_back(temp);
		} else if (temp.de < high && temp.cai < high && temp.de >= temp.cai) {
            admission[2].push_back(temp);
		} else {
            admission[3].push_back(temp);	
		}
    }
    int total = admission[0].size() + admission[1].size() + admission[2].size() + admission[3].size();
    printf("%d\n", total);
    for (int i = 0; i < 4; i++) {
        sort(admission[i].begin(), admission[i].end(), cmp);
        for (int j = 0; j < admission[i].size(); j++) {
            printf("%d %d %d\n", admission[i][j].id, admission[i][j].de, admission[i][j].cai);
		}
    }
    return 0;
}

