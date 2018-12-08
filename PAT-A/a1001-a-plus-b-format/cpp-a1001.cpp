/*
    @name     : a1001
    @version  : 18.1208
    @author   : zhangpeng96
    @time     : 30'00"
    @accepted : p8, p9 error
*/

#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;
int main() {
    int input1, input2;
    int sum, ctn;
    char str[20];

    cin >> input1 >> input2;
    sum = input1 + input2;

    sprintf(str, "%d", sum);

    ctn = 0;
    for(int i = 0; i < strlen(str); i++) {
        ctn = strlen(str) - i;

        if (!(ctn%3) && str[i-1]!='-') {
            cout << ",";
        }
        cout << str[i];

    }

    return 0;
}
