#include <iostream>
#include <iomanip>

using namespace std;


int maxNumber(int count, int dig[])
{
	int temp = 0;
	for (int i = 0; i < count; i++)	{
		if (dig[i] > temp) {
			temp = dig[i];
		}
	}
	return temp;
}

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
	
	int number, list[254], output[5];
	//memset(output, 0, sizeof(output));
	for (int i = 0; i < 5; i++) {
		output[i] = 0;
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
			output[0] += list[i];
		}
		if (divide(list[i], 1)) {
			sign *= -1;
			output[1] += list[i] * sign;
		}
		if (divide(list[i], 2)) {
			output[2] ++;
		}
		if (divide(list[i], 3)) {
			count++;
			output[3] += list[i];
		}
		if (divide(list[i], 4)) {
			if (list[i] > max) {
				max = list[i];
			}
		}
	}

	average = (float)output[3] / count;
	cout << output[0] << " " << output[1] << " " << output[2] << " " << setprecision(1) << fixed << average << " " << max << endl;

	return 0;
}