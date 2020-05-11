/*
    @name      : b1085
    @version   : 20.0511
    @author    : zhangpeng96
    @test_time : 
    @pass_rate : all
*/

#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

struct node {
	float level;
	int count, score;
    string school;
    string id;
    node() {
    	count = 0;
    	score = 0;
	}
};

int main() {
	ios::sync_with_stdio(false);
	map<char, float> grade_weight;
	grade_weight['A'] = 1;
	grade_weight['B'] = 1/1.5;
	grade_weight['T'] = 1.5;
//	printf("%.2f", grade_weight['B']);
//	for (int i = 0; i < 2; i++) {
		node temp;
		int score;
		cin >> temp.id >> score >> temp.school;
//		transform(school.begin(), school.end(), school.begin(), ::tolower);
		transform(temp.school.begin(), temp.school.end(), temp.school.begin(), ::tolower);
//		temp.school = school;
		temp.level = grade_weight[temp.id[0]];
		temp.score += score;
//		cout << school[0] << endl;
		cout << temp.school << " " << temp.level << " " << temp.score << endl; 
//	}
//	vector<node> admission;
	return 0;
}

