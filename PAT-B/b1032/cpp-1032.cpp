/*
    @name      : b1032
    @version   : 20.0512.2
    @author    : zhangpeng96
    @test_time : 16'04"
    @pass_rate : all
*/

#include <iostream>
#include <map>
#include <algorithm>

using namespace std;

bool cmp(const pair<int, int> &a, const pair<int, int> &b) {
   return a.second < b.second;
}

int main() {
    ios::sync_with_stdio(false);
//	freopen("test_point.txt", "r", stdin);
    int count;
    cin >> count;

    map<int, int> dicts;

    for (int i = 0; i < count; i++) {
        int key, value;
        cin >> key >> value;
        if (dicts.count(key)) {
            dicts[key] += value;
        } else {
            dicts[key] = value;
        }
    }

    auto max = max_element(dicts.begin(), dicts.end(), cmp);
    cout << max->first << " " << max->second << endl;
}

/*
    References
    - https://stackoverflow.com/a/44641350
    - http://www.cplusplus.com/reference/algorithm/max_element/
    - https://stackoverflow.com/questions/30611709/find-element-with-max-value-from-stdmap
 */