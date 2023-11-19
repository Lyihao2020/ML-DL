// Acwing 811. 交换数值
/*
输入两个整数 x 和 y，请你编写一个函数, 交换两个整数的数值并输出交换后的 x 和 y。

C++中的格式为：void swap(int &x, int &y)。

Java中的格式为：void swap(int[] a)，交换a[0]和a[1]。

输入格式
共一行，包含两个整数 x 和 y。

输出格式
共一行，包含交换后的 x 和 y。

数据范围
1≤x,y≤100
输入样例：
3 5
输出样例：
5 3
*/

#include<iostream>
using namespace std;

void swap(int &x, int &y){
    int temp; 
    temp = x; 
    x = y;
    y = temp;
}

int main(){

    int x, y;
    cin >> x >> y;
    swap(x, y);
    cout << x << " " << y;

    return 0;
}