// AcWing 662. 点的坐标
/*
给定两个保留一位小数的浮点数 X,Y，用来表示一个点的横纵坐标。

请你判断该点在坐标系中的位置。

输入格式
共一行，包含两个浮点数 X,Y，表示点的横纵坐标。

输出格式
如果点在第一象限，则输出 Q1，在第二象限，则输出 Q2，以此类推。

如果点在原点处，则输出 Origem。

否则，如果点在 x 坐标上，则输出 Eixo X，在 y 坐标上，则输出 Eixo Y。

数据范围
−10.0≤X,Y≤10.0
输入样例1：
4.5 -2.2
输出样例1：
Q4
输入样例2：
0.0 0.0
输出样例2：
Origem

*/
#include<iostream>
using namespace std;

int main(){
    double x, y;
    cin >> x >> y;

    if(x == 0 && y == 0){
        cout << "Origem";
    }else if(x == 0){
        cout << "Eixo Y";
    }else if(y == 0){
        cout << "Eixo X";
    }else if(x > 0 && y > 0){
        cout << "Q1";
    }else if(x < 0 && y > 0){
        cout << "Q2";
    }else if(x < 0 && y < 0){
        cout << "Q3";
    }else if(x > 0 && y < 0){
        cout << "Q4";
    }

    return 0;
}