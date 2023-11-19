// Acwing 820. 递归求斐波那契数列
/*
请使用递归的方式求斐波那契数列的第 n 项，下标从1开始。

斐波那契数列：1,1,2,3,5…，这个数列从第 3 项开始，每一项都等于前两项之和

输入格式
共一行，包含整数 n。

输出格式
共一行，包含一个整数，表示斐波那契数列的第 n 项。

数据范围
1≤n≤30
输入样例：
4
输出样例：
3
*/

#include<iostream>
using namespace std;

int fib(int n){
    if(n == 1 || n == 2){
        return 1;
    }else{
        return fib(n - 1) + fib(n - 2);
    }
}

int main(){

    int n;
    cin >> n;
    cout << fib(n) << endl;

    return 0;

}