#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, k;
    cin >> n >> k;
    int ans=0;
    int target=0;
    int adjust=n;

    while (n--) {
        int i;
        cin >> i;
        if (n==(adjust-k)) {
            target=i;
        }
        if ((i<target) || (i==0)) {
            break;
        } else {
            ans++;
        }

    }

    cout << ans;
    return 0;
}