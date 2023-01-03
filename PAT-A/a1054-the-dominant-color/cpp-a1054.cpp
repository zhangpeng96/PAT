/*
    @name      : a1054
    @version   : 20.0528.2
    @author    : zhangpeng96
    @test_time : 21'00"
    @pass_rate : all
*/

#include <iostream>
#include <map>

using namespace std;

int main() {
    ios::sync_with_stdio(false);

    int width, height, temp, threshold;
    map<int, int> bitmap;
    cin >> width >> height;
    threshold = width * height / 2;

    for (int i = 0; i < height; i++) {
        for (int j = 0; j < width; j++) {
            cin >> temp;
            if (bitmap.count(temp)) {
                bitmap[temp] ++;
            } else {
                bitmap.insert(make_pair(temp, 0));
            }
            if (bitmap.count(temp) > threshold)
                break;
        }
    }

    cout << temp << endl;

    return 0;
}
