#include <iostream>

using namespace std;

int map1[3], map2[3];

char maxSign(int map[]) {
	//cout << map[2] << ">" << map[0] << "," << map[2] << ">" << map[1] << endl;

	if ((map[2] > map[0]) && (map[2] > map[1])) {
		return 'B';
	}
	if (map[0] > map[1] && map[0] > map[2]) {
		return 'C';
	}
	if (map[1] > map[0] && map[1] > map[2]) {
		return 'J';
	}
}

int judge (char op1, char op2) {
	if (op1 == op2) {
		return 0;
	}
	else if (op1 == 'C' && op2 == 'J') {
		map1[0] ++;
		return 1;
	}
	else if (op1 == 'C' && op2 == 'B') {
		map2[2] ++;
		return -1;
	}
	else if (op1 == 'J' && op2 == 'C') {
		map2[0] ++;
		return -1;
	}
	else if (op1 == 'J' && op2 == 'B') {
		map1[1] ++;
		return 1;
	}
	else if (op1 == 'B' && op2 == 'C') {
		map1[2] ++;
		return 1;
	}
	else if (op1 == 'B' && op2 == 'J') {
		map2[1] ++;
		return -1;
	}
	else {
		return 2333;
	}
}

int main () {
	int times, result1[3], result2[3];
	char op1, op2;
	for (int i = 0; i < 3; i++) {
		result1[i] = 0;
		result2[i] = 0;
	}
	
	cin >> times;

	while (times--) {
		cin >> op1 >> op2;
		if (judge(op1, op2) == 0) {
			result1[1] ++;
			result2[1] ++;
		}
		else if (judge(op1, op2) == 1) {
			result1[0] ++;
			result2[2] ++;
		}
		else if (judge(op1, op2) == -1) {
			result1[2] ++;
			result2[0] ++;
		}
	}

	cout << result1[0] << " " << result1[1] << " " << result1[2] << endl;
	cout << result2[0] << " " << result2[1] << " " << result2[2] << endl;
	cout << maxSign(map1) << " " << maxSign(map2) << endl;
	return 0;
}