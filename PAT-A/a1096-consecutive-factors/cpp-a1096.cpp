#include <iostream>
#include <cmath>
using namespace std;
long int number, product;
int main(){
    cin >> number;
    int first = 0, len = 0, maxn = sqrt(number) + 1;
    for (int a = 2; a <= maxn; a++) {
        int b;
        product = 1;
        for (b = a; b <= maxn; b++) {
            product *= b;
            if (number % product != 0) break;
        }
        if (b - a > len) {
            len = b - a;
            first = a;
        }
    }
    if (first == 0) {
        cout << 1 << endl << number;
    } else {
        cout << len << endl;
        for (int i = 0; i < len; i++) {
            cout << first + i;
            if (i != len - 1) cout << '*';
        }
    }
    return 0;
}
