// Acwing 720. 连续整数相加
/*
读入两个整数值 A 和 N，计算从 A 开始的 N 个连续整数的和。

注意，如果读入的 N 为 0 或负数，则继续读取数字直至读入 N 值为正整数为止。

输入格式
共一行，包含整数 A 和若干个整数 N（不超过 100 个）。

输出格式
一个整数，表示从 A 开始的 N 个连续整数的和。

数据范围
1≤A≤100,
−100≤N≤100
输入样例1：
3 2
输出样例1：
7
输入样例2：
3 -1 0 -2 2
输出样例2：
7
*/

#include <iostream>
using namespace std;

int main()
{
    int a,n;
    cin >> a;
    // 重要!!!
    while(cin >> n,n<=0);  // 过滤0和负数
    int res=0;
    for(int i=0;i<n;i++)
    {
        res +=a++;
    }
    cout<<res;
}