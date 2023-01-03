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
	int counter, M, N, prime[10000];
	counter = 0;

	cin >> M >> N;

	for (int i = 2; i <= 1000000; i++) {
		if (primeCheck(i)) {
			prime[counter] = i;
			counter++;
		}
		if (counter > N) {
			break;
		}
	}
	
	counter = 0;
	for (int i = (M-1); i < N; i++) {
		cout << prime[i];
		counter++; 
		if ((counter % 10) && (i!= N-1)) {
			cout << " ";
		}
		else {
			cout << endl;
		}
	}

	return 0;
}