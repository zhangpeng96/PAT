/*
    @name     : a1001
    @source   : https://en.cppreference.com/w/cpp/locale/numpunct/thousands_sep
*/

#include <iostream>
#include <locale>
using namespace std;

struct space_out: numpunct<char> {
    char do_thousands_sep() const {
        return ',';
    }
    string do_grouping() const {
        return "\3";
    }
};

int main() {
    long long a, b, sum;
    cin >> a >> b;
    sum = a + b;
    cout.imbue(locale(cout.getloc(), new space_out));
    cout << sum << endl;
    return 0;
}
