/*
    @name      : b1065
    @version   : 20.0513
    @author    : zhangpeng96
    @test_time : 40'00"
    @pass_rate : p3 timeout
*/

#include <iostream>
#include <set>
#include <vector>
#include <algorithm>
using namespace std;


int main() {
    ios::sync_with_stdio(false);
//    freopen("test_point.txt", "r", stdin);
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
    	if (includes(party.begin(), party.end(), x.begin(), x.end())) {
			for (set<int>::iterator it = x.begin(); it != x.end(); ++it) {
				party.erase(*it);
			}
		}
    }

    cout << party.size() << endl;
    set<int>::iterator it;
    for(it = party.begin(); it != party.end(); it++) {
    	if (it != party.begin()) {
    		cout << " ";
		}
        cout << *it;
	}
}

/*
	References
	- http://www.cplusplus.com/reference/set/set/erase/
*/
