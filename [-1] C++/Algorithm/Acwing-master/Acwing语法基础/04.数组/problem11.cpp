// Acwing 741. 斐波那契数列
/*
输入整数 N，求出斐波那契数列中的第 N 项是多少。

斐波那契数列的第 0 项是 0，第 1 项是 1，从第 2 项开始的每一项都等于前两项之和。

输入格式
第一行包含整数 T，表示共有 T 个测试数据。

接下来 T 行，每行包含一个整数 N。

输出格式
每个测试数据输出一个结果，每个结果占一行，

结果格式为 Fib(N) = x，其中 N 为项数，x 为第 N 项的值。

数据范围
0≤N≤60
输入样例：
3
0
4
2
输出样例：
Fib(0) = 0
Fib(4) = 3
Fib(2) = 1
*/

#include<iostream>
using namespace std;

int main(){
    int n;
    cin >> n;

    for(int i = 0; i < n; i++)
    {
        long tempA = 0, tempB = 1, num;
        cin >> num;
        for(int j = 0; j < num; j++)
        {
            long temp = tempB;
            tempB = tempA + tempB;
            tempA = temp;
        }
        cout << "Fib(" << num << ") = " << tempA << endl;
    }

    return 0;
}
