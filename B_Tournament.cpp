# include <bits/stdc++.h>
using namespace std;


int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int t;
    cin >> t;
    
    for (int i=0; i<t; i++) {
        int n, j, k;
        cin >> n >> j >> k;
        vector<int> arr(n);
        for (int j=0; j<n; j++) {
            cin >> arr[j];
        }
        int maxVal = *max_element(arr.begin(), arr.end());
        
        
        if ((k==1 && arr[j-1]==maxVal) || (k > 1)) {
            cout << "YES" << endl; 
        } else {
            cout << "NO" << endl;
        }
    }
    
    return 0;
}