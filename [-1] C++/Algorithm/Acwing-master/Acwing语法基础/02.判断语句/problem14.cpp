// Acwing 663. 简单排序
/*
读取三个整数并按升序对它们进行排序。

输入格式
共一行，包含三个整数。

输出格式
首先，将三个整数按升序顺序输出，每行输出一个整数。

然后，输出一个空行。

紧接着，将三个整数按原输入顺序输出，每行输出一个整数。

数据范围
−100≤输入整数≤100,
输入整数各不相同。

输入样例：
7 21 -14
输出样例：
-14
7
21

7
21
-14
*/

#include<iostream>
#include<cstdio>
using namespace std;

int main(){
    int a, b, c;
    cin >> a >> b >> c;
    int x, y, z;
    x = a; y = b; z = c;

    if(a > b) swap(a, b);
    if(a > c) swap(a, c);
    if(b > c) swap(b, c);
    /*
    x=max(a,max(b,c));
    y=min(a,min(b,c));
    z=a+b+c-x-y;
    */

    cout << a << endl << b << endl << c << endl << endl;
    cout << x << endl << y << endl << z;

    return 0;
}