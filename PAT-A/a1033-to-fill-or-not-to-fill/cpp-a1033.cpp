#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int maxn = 510;
const int INF = 1000000000;

struct station {
    double price, dis;//价格、与起点之间的距离
} st[maxn];

bool cmp(station a, station b) {
    return a.dis < b.dis;
}

int main() {
    int n;
    double Cmax, D, Davg;
    scanf("%lf%lf%lf%d", &Cmax, &D, &Davg, &n);
    for (int i = 0; i < n; i++) {
        scanf("%lf%lf", &st[i].price, &st[i].dis);
    }
    st[n].price = 0.0;
    st[n].dis = D;
    sort(st, st + n, cmp);//将所有加油站按照距离从小到大排序
    if (st[0].dis != 0) {
        printf("The maximum travel distance = 0.00\n");
    } else {
        int now = 0;//当前所处的加油站编号
        //总花费、当前油量、满油行使的距离
        double ans = 0, nowTank = 0, MAX = Cmax * Davg;//Max是满油行使的距离
        while (now < n) {//每次循环将选出下一个需要到达的加油站
            //选出从当前加油站满油能到达范围内的最近的油价低于当前油价的加油站 
            //如果没有低于当前油价的，则在满油能到达的范围内找出最低的油价加油站，并且在本站加满油，去往下一站
            int k = -1;//最低油价的加油站编号
            double priceMin = INF;//最低油价
            for (int i = now + 1; i <= n && st[i].dis - st[now].dis <= MAX; i++) {
                if (st[i].price < priceMin) {
                    priceMin = st[i].price;
                    k = i;
                    //如果找到第一个比当前油价还低的，直接break
                    if (priceMin < st[now].price) {
                        break;
                    }
                }
            }
            if (k == -1) break;//满油状态无法到达加油站，退出循环输出结果
            //下面为能找到可达的加油站，计算转移花费
            double need = (st[k].dis - st[now].dis) / Davg;//从now 转移到k需要的油量
            if (priceMin < st[now].price) {//如果加油站k的油价低于当前油价
                if (nowTank < need) {//尤其注意，这里也是要判断的，而我自己忘记判断了
                    ans += (need - nowTank) * st[now].price;
                    nowTank = 0;//到达加油站k后油箱为0
                } else {//如果当前油量超过need
                    nowTank = -need;//直接到达加油站，不需要计算钱了
                }
            } else {//如果加油站k的油价高于当前油价
                ans += (Cmax - nowTank) * st[now].price;//要足够严谨，此时也许油箱里有油
                nowTank = Cmax - need;//到达k站后油量为Cmax-need
            }
            now = k;
        }
        if (now == n) {//说明是循环结束退出，能够到达重点
            printf("%.2f", ans);
        } else {
            printf("The maximum travel distance = %.2f\n", st[now].dis + MAX);
        }
    }
    return 0;
}
