// 输入输出，变量的大小类型
#include<iostream>
using namespace std;

int main(){
    // bool false/true  1 Byte
    // char 'c', 'a', ' ', '\n' 1Byte
    // int -2147483648 ~ 2147483647 4Byte(2的32位)
    // float 1.23, 2.5, 1.235e2, 6-7位有效数字 4Byte
    // double 15-16位有效数字   8Byte

    // long long -2^63 ~ 2^63-1 8Byte
    // long double 18-19位有效数字  12/16Byte

    // 1 Byte = 8 bit

    /*
    int a, b = 2, c = b;
    float d = 1.5, e = 1, f = 1.235e2;
    bool g = true, h = false;
    char j = 'a', k = 'b';

    long long l = 100000000000000LL;
    long double m = 123.45;

    另外，浮点数比较存在误差，即误差在多少以内合理
    */
    int a, b;

    cin >> a >> b;
    cout << a + b << endl;

    return 0;

}