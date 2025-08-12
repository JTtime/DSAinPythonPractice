#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;

    int ans = 0;

    while (t--) {
        char a, b, c;
        cin >> a >> b >> c;

        if (b=='+') {
            ans++;
        } else {
            ans--;
        }

    }

    cout << ans;

    return 0;
}