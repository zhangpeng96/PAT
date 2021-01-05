/*
    @name      : a1085
    @version   : 21.0105
    @author    : zhangpeng96
    @pass_rate : all
*/

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int binary_search_upper(vector<int> &seq, long long key, int low, int high) {
    while (low < high) {
        int mid = (low + high) / 2;
        if (seq[mid] > key)
            high = mid;
        else
            low = mid + 1;
    }
    return low;
}

int main() {
    int n, p, ans = 0;
    cin >> n >> p;
    vector<int> seq(n);

    for (int i = 0; i < n; i++)
        cin >> seq[i];

    sort(seq.begin(), seq.end());
    for (int i = 0; i < n; i++) {
        int low = binary_search_upper(seq, (long long) seq[i] * p, i, seq.size());
        ans = max(ans, low - i);
    }
    cout << ans;
    return 0;
}
