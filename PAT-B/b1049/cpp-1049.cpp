/*
    @name      : b1049
    @version   : 20.0516
    @author    : zhangpeng96
    @test_time : 
    @pass_rate : 
*/

#include <iostream>
#include <algorithm>
#include <vector>
#include <numeric>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
	freopen("test_point.txt", "r", stdin);

	int count;
	float summon, temp; 
	vector<float> digit;
	cin >> count;

	for (int i = 0; i < count; i++) {
		cin >> temp;
		digit.push_back(temp);
	}
	summon = accumulate(digit.begin(), digit.end(), 0.0);
	
	for (int i = 0; i < digit.size(); i++) {
		float count = 0.0;
		for (int j = 0; j < digit.size(); j++) {
			if (i > j) {
				count += digit[]
			}
		}
		cout << digit[i] << endl;
	}
	
	cout << summon << endl;
	return 0;
}
