#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

int main() {
    string digit;
    int sum = 0;
    map<char, string> letter = {
        {'0', "zero"},
        {'1', "one"},
        {'2', "two"},
        {'3', "three"},
        {'4', "four"},
        {'5', "five"},
        {'6', "six"},
        {'7', "seven"},
        {'8', "eight"},
        {'9', "nine"}
    };
    cin >> digit;

    for (int i = 0; i < digit.size(); i++)
        sum += (int)digit[i] - 48;

    string str = to_string(sum);

    for (int i = 0; i < str.size(); i++) {
        cout << letter[str[i]];
        if (i < str.size()-1)
            cout << ' ';
    }
}
