#include <iostream>

using namespace std;

int main() {
	int n, m;
	while (cin >> n >> m) {
		int k, a[255];
		k = m % n;

		for (int i = 0; i < n; i++){
			cin >> a[(i + k) % n];
		}

		for (int i = 0; i < n - 1; i++) {
			cout << a[i] << " ";
		}
		cout << a[n - 1] << endl;

	}
	return 0;
}