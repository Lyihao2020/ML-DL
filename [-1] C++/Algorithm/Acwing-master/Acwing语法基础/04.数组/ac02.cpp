// 输入一个n， 再输入n个整数， 将这n个整数逆序输出
#include<iostream>
using namespace std;

int main(){

    int n;
    int a[100];
    cin >> n;

    for(int i = 0; i < n; i++)  cin >> a[i];
    for(int i = n - 1; i >= 0; i--) cout << a[i] << " ";
    cout << endl;

    return 0;

}