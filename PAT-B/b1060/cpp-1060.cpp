/*
    @name      : b1060
    @version   : 20.0517
    @author    : zhangpeng96
    @test_time : 
    @pass_rate : 
    @source    : https://www.jianshu.com/p/cddb9a404f77
*/

#include <iostream>
#include <set>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
//  freopen("test_point.txt", "r", stdin);

    multiset<int, greater<int>> s;   //降序排列
    int n, t;
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> t;
        s.insert(t);                 //插入 排序
    }

    int max = 0, count = 1;          //记录天数
    for (auto it = s.begin(); it != s.end(); count++, it++) {
        if (*it > count)
            max = count > max ? count : max;  //找最大E
    }

    cout << max;
    return 0;
}
