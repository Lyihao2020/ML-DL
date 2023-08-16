// Acwing 805. x和y的最大值
/*
输入两个整数 x 和 y，请你编写一个函数，int max(int x, int y)，计算并输出 x 和 y 的最大值。

输入格式
共一行，包含两个整数 x 和 y。

输出格式
共一行，包含一个整数，表示两个数中较大的那个数。

数据范围
−100≤x,y≤100
输入样例：
3 6
输出样例：
6
*/

#include<iostream>
using namespace std;

int max(int x, int y){
    return (x > y)? x: y;
}

int main(){

    int x, y;
    cin >> x >> y;
    cout << max(x, y) << endl;
    return 0;
}