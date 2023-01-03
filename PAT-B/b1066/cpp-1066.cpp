/*
    @name      : b1066
    @version   : 20.0527.2
    @author    : zhangpeng96
    @test_time : 13'56"
    @pass_rate : all
*/

#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    // freopen("test_point.txt", "r", stdin);

    int height, width, start, end, color, temp;
    cin >> height >> width >> start >> end >> color;

    int bitmap[height][width];
    for (int i = 0; i < height; i++) {
        for (int j = 0; j < width; j ++) {
            cin >> temp;
            if (start <= temp && temp <= end) {
                bitmap[i][j] = color;
            } else {
                bitmap[i][j] = temp;
            }
        }
    }

    for (int i = 0; i < height; i++) {
        for (int j = 0; j < width; j ++) {
            if (j != 0) cout << " ";
            cout << setfill('0') << setw(3) << bitmap[i][j];
        }
        cout << endl;
    }

    return 0;
}
