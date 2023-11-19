// Acwing 809. 最小公倍数
/*
输入两个整数 a 和 b，请你编写一个函数，int lcm(int a, int b)，计算并输出 a 和 b 的最小公倍数。

输入格式
共一行，包含两个整数 a 和 b。

输出格式
共一行，包含一个整数，表示 a 和 b 的最小公倍数。

数据范围
1≤a,b≤1000
输入样例：
6 8
输出样例：
24
*/

/*

C++ 求最小公倍数的方法有多种，下面给出两种实现：

方法一：使用辗转相除法求最大公约数，再用两数之积除以最大公约数得到最小公倍数。

```cpp
int gcd(int a, int b) {
    return b == 0 ? a : gcd(b, a % b);
}

int lcm(int a, int b) {
    return a / gcd(a, b) * b;
}
```

方法二：将两数相乘，再除以它们的最大公约数得到最小公倍数。

```cpp
int gcd(int a, int b) {
    return b == 0 ? a : gcd(b, a % b);
}

int lcm(int a, int b) {
    return (a * b) / gcd(a, b);
}
```

这两种方法都能够正确地求出最小公倍数，具体选择哪种方法可以根据实际情况进行判断。

*/

#include<iostream>
// #include<bits/stdc++.h>
using namespace std;
/*
int lcm(int a, int b){
    return a * b / gcd(a, b);
}

int main(){
    int a, b;
    cin >> a >> b;
    cout << lcm(a, b) << endl;
    return 0;
}
*/