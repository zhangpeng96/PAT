#include <cstdio>
#include <algorithm>
using namespace std;

long long a[100005];

int main() {
    int n, m, x, y;
    scanf("%d", &n);
    for (int i = 1; i <= n; ++i) {
        scanf("%lld", a + i);
        a[i] += a[i-1];
    }
    scanf("%d", &m);
    while (m--) {
        scanf("%d%d", &x, &y);
        if (y < x) {
            swap(x, y);
        }
        printf("%d\n", min(a[y-1] - a[x-1], a[x-1] + a[n] - a[y-1]));
    }
    return 0;
}
