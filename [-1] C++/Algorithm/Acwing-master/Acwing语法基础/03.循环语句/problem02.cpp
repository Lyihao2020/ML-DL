// Acwing 709. 奇数
/*
输入一个整数 X，输出 1 到 X 之间（包括 1 和 X）的全部奇数。

输入格式
一个整数 X。

输出格式
输出所有满足条件的奇数，每个数占一行。

数据范围
1≤X≤1000
输入样例：
8
输出样例：
1
3
5
7
*/

#include<iostream>
using namespace std;

int main(){
    int n;
    cin >> n;

    for(int i = 1; i <= n; i += 2){
        cout << i << endl;
    }

    return 0;
}