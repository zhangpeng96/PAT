/*
用例:
30 2 3 10
2145174067 0
35 1
2 0
58 1
67 1
56 1
42 1
73 1
19 0
37 0

对应输出应该为:

1.33

你的输出为:

715058034.00
 */

#include <bits/stdc++.h>
using namespace std;

const int inf = 99999999;
typedef struct station {
    double price, dis;

    station() {}

    station(double price, double dis) {
        this->price = price;
        this->dis = dis;
    }
} station;

bool cmp(station &a, station &b) {
    return a.dis < b.dis;
}

/*
bool cmp(station &a, station &b) {
    if (a.dis != b.dis) {
        return a.dis < b.dis;
    } else {
        return a.price < b.price;
    }
}
 */

int main() {
    double cmax, d, davg;
    int n;
    cin >> cmax >> d >> davg >> n;

    // 读入数据，目的地视为一个油价为0的加油站，这样就算计算的距离超出了d也不会增加总花费
    vector<station> sta(n + 1);
    sta[0] = station(0.0, d);
    for (int i = 1; i <= n; i++)
        cin >> sta[i].price >> sta[i].dis;

    // 按距离排序
    sort(sta.begin(), sta.end(), cmp);

    double nowprice = 0.0, nowdis = 0.0;    // 当前加油站价格 和 当前加油站距离
    double totalPrice = 0.0;                // 总花费
    double leftdis = 0.0;                   // 油箱中剩余的油所能走的距离

    // 距离为0处如果不存在加油站则最远距离为0，因为一开始油箱为空
    if (sta[0].dis != 0) {
        cout << "The maximum travel distance = 0.00" << endl;
        return 0;
    } else
        nowprice = sta[0].price;

    while (nowdis < d) {
        int flag = 0;   // 标记在可到达的范围内是否找到了价格小于当前价格的加油站
        double maxDis = nowdis + cmax * davg;  // 能到达的最远的距离
        double minPrice = inf, minPriceDis = 0.0;    // 当前加油站所能到达的范围内的加油站的最低价格和它所在的位置
        for (int i = 1; i <= n && sta[i].dis <= maxDis; i++) {
            if (sta[i].dis <= nowdis) continue;

            // 如果存在加油站比当前价格低
            if (sta[i].price < nowprice) {
                // 去下一个加油站的路上也在消耗之前剩的油
                totalPrice += (sta[i].dis - nowdis - leftdis) * nowprice / davg;
                nowprice = sta[i].price;
                nowdis = sta[i].dis;
                leftdis = 0.0;
                flag = 1;
                break;
            }

            // 记录能到达范围内的最低的油价
            if (sta[i].price < minPrice) {
                minPrice = sta[i].price;
                minPriceDis = sta[i].dis;
            }
        }

        // 如果不存在比当前加油站油价低的加油站，但存在加油站
        if (flag == 0 && minPrice != inf) {
            totalPrice += nowprice * (cmax - leftdis / davg);  // 把油箱装满
            leftdis = cmax * davg - (minPriceDis - nowdis);    // 到达下一个加油站后剩余的油能走的距离
            nowdis = minPriceDis;
            nowprice = minPrice;
        }

        //  如果在可到达的范围内没有加油站
        if (flag == 0 && minPrice == inf) {
            nowdis += cmax * davg;
            printf("The maximum travel distance = %.2lf\n", nowdis);
            return 0;
        }
    }
    printf("%.2lf\n", totalPrice);
    return 0;
}
