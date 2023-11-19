// Acwing613. 面积
/*
给定三个浮点数 A，B 和 C。

然后，计算如下图形的面积：

底边为 A，高为 C 的三角形。
半径 C 的圆。（π=3.14159）
底边为 A 和 B，高为 C 的梯形。
边长为 B 的正方形。
边长为 A 和 B 的长方形。
输入格式
输入共一行，包含三个保留一位小数的浮点数 A，B，C。

输出格式
输出共五行，形式如下所示：

第一行，格式为 TRIANGULO: X，其中 X 为所求三角形面积。

第二行，格式为 CIRCULO: X，其中 X 为所求圆形面积。

第三行，格式为 TRAPEZIO: X，其中 X 为所求梯形面积。

第四行，格式为 QUADRADO: X，其中 X 为所求正方形面积。

第五行，格式为 RETANGULO: X，其中 X 为所求长方形面积。

所有答案保留三位小数。

数据范围
0≤A,B,C≤10000.0
输入样例：
3.0 4.0 5.2
输出样例：
TRIANGULO: 7.800
CIRCULO: 84.949
TRAPEZIO: 18.200
QUADRADO: 16.000
RETANGULO: 12.000
*/

#include<iostream>
#include<iomanip>
#define pi 3.14159
using namespace std;

int main(){
    double l1, l2, l3;
    cin >> l1 >> l2 >> l3;

    cout << "TRIANGULO: " << fixed << setprecision(3) << 0.5 * l1 * l3 << endl;
    cout << "CIRCULO: " << fixed << setprecision(3) << pi * l3 * l3 << endl;
    cout << "TRAPEZIO: " << fixed << setprecision(3) << 0.5 * l3 * (l1 + l2) << endl;
    cout << "QUADRADO: " << fixed << setprecision(3) << l2 * l2 << endl;
    cout << "RETANGULO: " << fixed << setprecision(3) << l1 * l2 << endl;

   return 0;
}