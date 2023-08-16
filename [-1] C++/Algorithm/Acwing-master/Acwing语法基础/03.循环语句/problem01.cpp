// Acwing 708. 偶数
/*
编写一个程序，输出 1 到 100 之间（包括 1 和 100）的全部偶数。

输入格式
无输入。

输出格式
输出全部偶数，每个偶数占一行。

输入样例
No input
输出样例
2
4
6
...
100
*/

#include<iostream>
using namespace std;

int main(){

    for(int i = 2; i <= 100; i += 2){
        cout << i << endl;
    }
    
    return 0;
}