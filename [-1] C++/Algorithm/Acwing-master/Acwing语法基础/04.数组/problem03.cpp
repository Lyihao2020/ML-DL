// Acwing 739. 数组选择
/*
输入一个长度为 100 的数组 A，请你按顺序输出其中不大于 10 的所有元素。

输入格式
输入 100 个数，每个数占一行，表示数组的所有元素的值。

每个数可能是整数也可能是浮点数。

输出格式
按顺序输出数组中的所有不大于 10 的元素，每个元素占一行。

输出格式为 A[i] = x，其中 i 为元素编号，x 为元素的值。

注意，所有的 x 均保留一位小数。

数据范围
−100≤A[i]≤100
输入样例：
0
-5
63
-8.5
...
输出样例：
A[0] = 0.0
A[1] = -5.0
A[3] = -8.5
...
*/

#include<iostream>
#include<iomanip>
using namespace std;

int main(){
    double a[100];

    for(int i = 0; i < 100; i++)
    {
        cin >> a[i];
        if(a[i] <= 10)
        {
            cout << "A[" << i << "] = " << fixed << setprecision(1) << a[i] << endl;
        }
    }
    return 0;
}