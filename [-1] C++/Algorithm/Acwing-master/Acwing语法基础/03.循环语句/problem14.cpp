// Acwing 713. 区间 2
/*
读取 N 个整数 X1,X2,…,XN，判断这 N 个整数中有多少个在 [10,20] 的范围内，有多少个在范围外。

输入格式
第一行包含整数 N，表示共有 N 个整数需要进行判断。

接下来 N 行，每行包含一个整数 Xi。

输出格式
第一行输出 x in，其中 x 为在范围内的整数的数量。

第二行输出 y out，其中 y 为在范围外的整数的数量。

数据范围
1≤N≤10000,
−107<Xi<107
输入样例：
4
14
123
10
-25
输出样例：
2 in
2 out
*/

#include<iostream>
using namespace std;

int main(){

    int n, cnt = 0;
    cin >> n;

    for(int i = 0; i < n; i++){
        int temp;
        cin >> temp;
        if(temp >= 10 && temp <= 20)
        {
            cnt++;
        }
    }

    cout << cnt << " in" << endl;
    cout << n - cnt << " out";
    
    return 0;
}