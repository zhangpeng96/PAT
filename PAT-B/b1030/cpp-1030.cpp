#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    int n, p, ans = 0;
    cin >> n >> p;
    vector<int> seq(n);

    for (int i = 0; i < n; i++)
        cin >> seq[i];

    sort(seq.begin(), seq.end());
    for (int i = 0; i < n; i++) {
        int low = upper_bound(seq.begin() + 1, seq.end(), (long long) seq[i] * p) - seq.begin();
        ans = max(ans, low - i);
    }
    cout << ans;
    return 0;
}
