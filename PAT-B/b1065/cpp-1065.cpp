/*
    @name      : b1065
    @version   : 20.0512
    @author    : zhangpeng96
    @test_time :
    @pass_rate :
*/

#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;


int main() {
    ios::sync_with_stdio(false);
    freopen("test_point.txt", "r", stdin);
    int pair_count, party_count;

    vector<set<int>> pair;
    cin >> pair_count;
    for (int i = 0; i < pair_count; i++) {
        int tmp_1, tmp_2;
        cin >> tmp_1 >> tmp_2;
        set<int> pair_set {tmp_1, tmp_2};
        pair.push_back(pair_set);
    }
    
    set<int> party;
    cin >> party_count;
    for (int i = 0; i < party_count; i++) {
        int tmp;
        cin >> tmp;
        party.insert(tmp);
    }
    
    
    for (auto &x : pair) {
    	bool result;
//    	result = includes(x.begin(), x.end(), party.begin(), party.end());
    	result = x < party;
//    	set_difference(x.begin(), x.end(), party.begin(), party.end(), inserter(party, party.begin() ) );
        cout << x.size() << " " << result << endl;
    }
    
    set<int>::iterator it;
    for(it = party.begin(); it != party.end(); it++) {
        cout << *it << " ";
    }
    
}
