#include<bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int ans=0;
    
    for (int i=1; i<=5; i++) {
        for (int j=1; j<=5; j++) {
            int a;
            cin >> a;
            if (a==1) {
                ans=abs(j-3)+abs(i-3);
            }
        }
    }
    cout << ans;


    return 0;
}