// 求反三位数
#include<iostream>
using namespace std;

int main(){

    int n;
    cin >> n;
    int a = n % 10;
    n /= 10;
    int b = n % 10;
    n /= 10;
    int c = n % 10;

    cout << a << b << c << endl;
    
    return 0;
}