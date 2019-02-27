#include <iostream>
#include <vector>

using namespace std;

int main(void){
	int N = 0, M = 0, num = 0;
	cin >> N >> M;
	vector<int> ivec;
	for (int count = 0; count < N; count++){
		cin >> num;
		ivec.push_back(num);
	}
	for (int count = 0; count < M; count++){
		ivec.insert(ivec.begin(), *(ivec.end() - 1));
		ivec.pop_back();
	}
	for (vector<int>::iterator iter = ivec.begin(); iter < ivec.end(); iter++){
		cout << *iter;
		if (iter + 1 != ivec.end())
			cout << " ";
	}
	
	return 0;
}
