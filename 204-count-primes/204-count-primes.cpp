class Solution {

public:
    int countPrimes(int n) {
        int cnt = 0;
        vector<int> v(n+1, 1);
            if(n==0||n==1){
                return 0;
            }
            for(int i = 2; i < n; i++){
                if(v[i]){
                    cnt++;
                    for(int j = i*2; j < n;j=j+i){
                        v[j]= 0;
                    }
                }
            }
        
        return cnt;
    }
};