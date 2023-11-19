// Acwing 612. 球的体积
/*
给定你一个球体的半径 R，请你计算球体的体积。

计算球体的公式为 V=(4/3)∗π∗R3。

π 取 3.14159。

注意：有些语言中 (4/3) 无法得到 1.3333…，建议在公式中使用 (4/3.0)。

输入格式
输入一个整数 R。

输出格式
输出格式为 VOLUME = X，其中 X 为球体的体积，结果保留三位小数。

数据范围
1≤R≤2000
输入样例：
3
输出样例：
VOLUME = 113.097
*/

#define pi 3.14159
#include<math.h>
#include<iostream>
#include<iomanip>
using namespace std;

int main(){
    int r;
    cin >> r;

    cout << "VOLUME = " << fixed << setprecision(3) << (4 / 3.0) * pi * pow(r, 3);

    return 0;
}