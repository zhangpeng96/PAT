/*
    @name      : b1073
    @version   : 20.0514
    @author    : zhangpeng96
    @test_time : 
    @pass_rate : 
*/

#include <iostream>
#include <set>
#include <vector>
#include <algorithm>
using namespace std;


float choice_weight(set<int> a, set<int> b) {
	bool include;
	include = includes(a.begin(), a.end(), b.begin(), b.end());
	if (include && (a != b)) {
		return 0.5;
	} else if (a == b) {
		return 1.0;
	} else {
		return 0.0;
	}
}

struct problem {
	int score;
	set<char> key;
};


int main() {
    ios::sync_with_stdio(false);
//    freopen("test_point.txt", "r", stdin);
    int student_count, problem_count;
    cin >> student_count >> problem_count;
    vector<problem> problems;
    vector<set<char>> students[student_count];

//    for (int i = 0; i < problem_count; i++) {
//    	int score, count, right;
//    	set<char> problem_key;
//    	cin >> score >> count >> right;
//    	for (int j = 0; j < right; j++) {
//    		char right_option;
//    		cin >> right_option;
//    		problem_key.insert(right_option);
//		}
//		problems.push_back(problem {score, problem_key});
//	}
	
	for (int i = 0; i < student_count; i++) {
        for (int j = 0; j < problem_count; j++) {
            char ch;
            int answer_count;
            set<char> answer;
            scanf("(%d", &answer_count);
            for (int k = 0; k < answer_count; k++) {
                scanf(" %c)", &ch);
                answer.insert(ch);
            }
            students[i].push_back(answer);
        }
    }
//    if (pair_set == pair_choice) {
//    	cout << "yes" << endl;
//	} else {
//		cout << "no" << endl;
//	}


    // vector<set<int>> pair;
    // cin >> pair_count;
    // for (int i = 0; i < pair_count; i++) {
    //     int tmp_1, tmp_2;
    //     cin >> tmp_1 >> tmp_2;
    //     set<int> pair_set {tmp_1, tmp_2};
    //     pair.push_back(pair_set);
    // }
    
    // set<int> party;
    // cin >> party_count;
    // for (int i = 0; i < party_count; i++) {
    //     int tmp;
    //     cin >> tmp;
    //     party.insert(tmp);
    // }

}

// https://www.liuchuo.net/archives/4216    