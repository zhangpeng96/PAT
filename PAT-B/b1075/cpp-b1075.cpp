#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;

const int Max = 100000;
struct node {
    int address;
    int data;
    int next;
    int num;
};
node ans[Max];
bool cmp(node a, node b) { //排序
    return a.num < b.num;
}
int begin1, n, k;
int main() {
    cin >> begin1 >> n >> k;
    for (int i = 0; i <= Max; i++) {
        ans[i].num = Max; //令每个结点的num为最大值,方便后面做排序
    }
    for (int i = 0; i < n; i++) {
        int address;
        cin >> address;
        cin >> ans[address].data >> ans[address].next; //以地址作为数组的位置方便读取
        ans[address].address = address;
    }
    int cnt = 0;
    int j = 0;
    for (int i = begin1; i != -1; i = ans[i].next) {
        if (ans[i].data < 0) {
            ans[i].num = cnt++; //小于0的部分,cnt作为排序的依据
        }
    }
    for (int i = begin1; i != -1; i = ans[i].next) {
        if (ans[i].data >= 0 && ans[i].data <= k) {
            ans[i].num = cnt++; //大于0小于k的部分,cnt作为排序依据
        }
    }
    for (int i = begin1; i != -1; i = ans[i].next) {
        if (ans[i].data > k) { //大于k的部分,cnt作为排序依据
            ans[i].num = cnt++;
        }
    }
    sort(ans, ans + Max, cmp); //排序
    for (int i = 0; i < cnt - 1; i++) { //cnt是实际的个数的大小
        printf("%05d %d %05d\n", ans[i].address, ans[i].data, ans[i + 1].address);
    }
    printf("%05d %d -1", ans[cnt - 1].address, ans[cnt - 1].data);
    return 0;
}