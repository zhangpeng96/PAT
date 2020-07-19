#include <iostream>
using namespace std;

int main() {
	int arr[10] = {9, 0, 1, 4, 5, 7, 8, 2, 3, 6};
	swap(arr[0], arr[ arr[0] ]);

	for(int i=0; i<10; i++) cout << arr[i] << " ";
	// output: 6 0 1 4 5 7 8 2 3 9 
	return 0;
}
