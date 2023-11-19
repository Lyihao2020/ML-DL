// Acwing 655. 天数转换
/*
读取对应于一个人的年龄（以天为单位）的整数值，并转化为年，月和日表示方式输出，年、月、日分别对应 ano(s), mes(es), dia(s)。

注意：为了方便计算，假设全年 365 天，每月 30 天。 数据保证，不会出现 12 个月和几天的情况，例如 360,363 或 364。

输入格式
输入一个整数 N。

输出格式
参照输出样例，输出转换后的天数表达。

数据范围
1≤N≤1000000
输入样例：
400
输出样例：
1 ano(s)
1 mes(es)
5 dia(s)
*/

#include<iostream>
using namespace std;
/*
int main(){
    int n;
    cin >> n;

    cout << n / 365 << " ano(s)" << endl;
    n -= 365 * (n / 365);
    cout << n / 30 << " mes(es)" << endl;
    n -= 30 * (n / 30);
    cout << n << " dia(s)" << endl;

    return 0;
}
*/

int main(){
    int n;
    cin >> n;

    cout << n / 365 << " ano(s)" << endl;
    cout << n % 365 / 30 << " mes(es)" << endl;
    cout << n % 365 % 30 << " dia(s)" << endl;
    return 0;
}