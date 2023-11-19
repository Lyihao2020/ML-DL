// Acwing 812. 打印数字
/*
输入一个长度为 n 的数组 a 和一个整数 size，请你编写一个函数, void print(int a[], int size), 打印数组 a 中的前 size 个数。

输入格式
第一行包含两个整数 n 和 size。

第二行包含 n 个整数 a[i]，表示整个数组。

输出格式
共一行，包含 size 个整数，表示数组的前 size 个数。

数据范围
1≤n≤1000,
1≤size≤n,

输入样例：
5 3
1 2 3 4 5
输出样例：
1 2 3
*/

#include<iostream>
using namespace std;

void print(int a[], int size){
    for(int i = 0; i < size; i++)
        cout << a[i] << " ";
    cout << endl;
}

int main(){

    int n, size;
    cin >> n >> size;
    int a[n];

    for(int i = 0; i < n; i++)  cin >> a[i];
    print(a, size);

    return 0;

}