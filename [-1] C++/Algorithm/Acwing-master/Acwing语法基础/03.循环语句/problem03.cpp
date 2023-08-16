// Acwing 712. 正数
/*
输入 6 个实数，它们要么是正数，要么是负数。

请你统计并输出正数的个数。

输入格式
六个数字，每个占一行。

输出格式
输出格式为 x positive numbers，其中 x 为正数的个数。

数据范围
输入数字的绝对值不超过 100。

输入样例：
7
-5
6
-3.4
4.6
12
输出样例：
4 positive numbers
*/

#include<iostream>
using namespace std;

int main(){
    double ans;
    int cnt = 0;

    for(int i = 0; i < 6; i++){
        cin >> ans;
        if(ans > 0) cnt++;
    }

    cout << cnt << " positive numbers" << endl;

    return 0;

}