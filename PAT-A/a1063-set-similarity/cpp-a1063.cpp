/*
    @name      : a1063
    @version   : 20.0531.2
    @author    : zhangpeng96
    @test_time : 43'19"
    @pass_rate : 
*/

#include <iostream>
#include <unordered_set>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std; 

int main() {
    ios::sync_with_stdio(false);
    freopen("test_point.txt", "r", stdin);
	cout << setiosflags(ios::fixed) << setprecision(1);

    int case_count, query_count, set_count, temp;
    
    vector<unordered_set<int>> cases;
    cin >> case_count;
    for (int i = 0; i < case_count; i++) {
        unordered_set<int> record;
        cin >> set_count;
        for (int j = 0; j < set_count; j++) {
            cin >> temp;
            record.insert(temp);
        }
        cases.push_back(record);
    }
    
    cin >> query_count;
    for (int i = 0; i < query_count; i++) {
        int a, b, inter_count, union_count;
        unordered_set<int> op;
        cin >> a >> b;
        set_intersection(cases[a-1].begin(), cases[a-1].end(), cases[b-1].begin(), cases[b-1].end(), inserter(op, op.begin() ) );
        inter_count = op.size();
//        for (auto &x: op) {
//            cout << x << ' ';
//        }
        set_union(cases[a-1].begin(), cases[a-1].end(), cases[b-1].begin(), cases[b-1].end(), inserter(op, op.begin() ) );
        union_count = op.size();
        float percentage;
        percentage = (inter_count * 100.0 / union_count);
    
        cout << percentage << '%' << endl;
        // for (auto &x: cases[a-1]) {
        //     cout << x << ' ';
        // }
        // cout << endl;
//        cout << endl << inter_count << '/' << union_count << endl;
//        cout << "*************" << endl;        
        // for (it = myset.begin(); it != myset.end(); ++it)
        //     cout << ' ' << *it;
        // cout << '\n';
    }

    return 0;
}
