// Acwing 604 圆的面积
/*
计算圆的面积的公式定义为 A=πR2。

请利用这个公式计算所给圆的面积。

π 的取值为 3.14159。

输入格式
输入包含一个浮点数，为圆的半径 R。

输出格式
输出格式为 A=X，其中 X 为圆的面积，用浮点数表示，保留四位小数。

数据范围
0<R<10000.00
输入样例：
2.00
输出样例：
A=12.5664
*/

/*
#define pi 3.14159
#include<iostream>
using namespace std;

int main(){
    // 用 double 比 float 要精准
    double r, s;
    cin >> r;

    cout << "A=";
    printf("%.4lf", pi * r * r);
    return 0;
}
*/

#define pi 3.14159
#include<iostream>
#include<iomanip>
using namespace std;

int main(){
    // 用 double 比 float 要精准
    double r, s;
    cin >> r;

    cout << "A=" << fixed << setprecision(4) << pi * r * r;
    return 0;
}