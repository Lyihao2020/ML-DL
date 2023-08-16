
class Solution {
public:
    int getSum(int n) {
        int res = n;
        (n > 0) && (res += getSum(n - 1));
        return res;
    }
};

/*
class Solution {
public:
    int getSum(int n) {
        char a[n][n+1];
        return sizeof(a)>>1;
    }
};

class Solution {
public:
    int getSum(int n) {
        int res = n;
        (n>0) && (res += getSum(n-1));
        return res;
    }
};
*/
