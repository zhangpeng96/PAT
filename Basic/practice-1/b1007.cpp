#include <iostream>

using namespace std;

bool primeCheck(int num) {
	for (int i = 2; i*i <= num; i++) {
		if (num % i == 0) {
			return false;
		}
	}
	return true;
}

int main() {
	int counter, N, prime[1000], result;
	counter = 0;
	result = 0;

	cin >> N;

	for (int i = 2; i <= N; i++) {
		if (primeCheck(i)) {
			prime[counter] = i;
			counter++;
			//cout << i << endl;
		}
	}

	for (int i = 0; i < counter; i++) {
		if ((prime[i + 1] - prime[i]) == 2) {
			result++;
		}
	}

	cout << result << endl;

	return 0;
}