#include <iostream>
#define MAX1 255

using namespace std;


int main() {

	int number;
	long long data[MAX1][3];
	cin >> number;

	for (int i = 0; i < number; i++) {
		for (int j = 0; j < 3; j++) {
			cin >> data[i][j];
		}
	}

	for (int i = 0; i < number; i++) {
		if ((data[i][0] + data[i][1]) > data[i][2]) {
			cout << "Case #" << (i + 1) << ": true" << endl;
		}
		else {
			cout << "Case #" << (i + 1) << ": false" << endl;
		}
	}

	return 0;
}