#include <iostream>
#include <iomanip>

using namespace std;


bool divide (int dig, int remainder) {
	if (dig % 5 == remainder) {
		return true;
	}
	else {
		return false;
	}
}

bool isEven (int dig) {
	if (dig % 2 == 0) {
		return true;
	}
	else{
		return false;
	}
}


int main() {
	
	int number, list[1000], output[5], flag[5];
	for (int i = 0; i < 5; i++) {
		output[i] = 0;
		flag[i] = 0;
	}
	cin >> number;
	for (int i = 0; i < number; i++) {
		cin >> list[i];
	}
	
	int sign = -1;
	int count = 0;
	int max  = 0;
	float average;

	for (int i = 0; i < number; i++) {
		if (divide(list[i], 0) && isEven(list[i]) ) {
			flag[0] = 1;
			output[0] += list[i];
		}
		if (divide(list[i], 1)) {
			flag[1] = 1;
			sign *= -1;
			output[1] += list[i] * sign;
		}
		if (divide(list[i], 2)) {
			flag[2] = 1;
			output[2] ++;
		}
		if (divide(list[i], 3)) {
			flag[3] = 1;
			count++;
			output[3] += list[i];
		}
		if (divide(list[i], 4)) {
			flag[4] = 1;
			if (list[i] > max) {
				max = list[i];
			}
		}
	}

	average = (float)output[3] / count;
	if (flag[0]) cout << output[0] << " "; else cout << "N ";
	if (flag[1]) cout << output[1] << " "; else cout << "N ";
	if (flag[2]) cout << output[2] << " "; else cout << "N ";
	if (flag[3]) cout << setprecision(1) << fixed << average << " "; else cout << "N ";
	if (flag[4]) cout << max << endl; else cout << "N" << endl;

	return 0;
}