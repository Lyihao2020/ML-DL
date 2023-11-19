// Acwing 808. 最大公约数
/*
输入两个整数 a 和 b，请你编写一个函数，int gcd(int a, int b), 计算并输出 a 和 b 的最大公约数。

输入格式
共一行，包含两个整数 a 和 b。

输出格式
共一行，包含一个整数，表示 a 和 b 的最大公约数。

数据范围
1≤a,b≤1000
输入样例：
12 16
输出样例：
4
*/

#include<iostream>
using namespace std;

int gcd(int a, int b){

    while(a != 0){
        int temp = b % a;
        b = a; 
        a = temp;
    }

    return b;

}

/*
int gcd(int a, int b){
    if(a == 0){
        return b;
    }
    return gcd(b % a, a);
}
*/

int main(){

    int a, b;
    cin >> a >> b;
    cout << gcd(a, b) << endl;
    return 0;

}

/*

以下是使用最大公约数（辗转相除法）求解C++的最小公倍数代码：

```c++
#include <iostream>
using namespace std;

// 使用欧几里得算法（辗转相除法）求解最大公约数
int gcd(int a, int b) {
    if (a == 0) {
        return b;
    }
    return gcd(b % a, a);
}

// 计算最小公倍数
int lcm(int a, int b) {
    return (a * b) / gcd(a, b);
}

int main() {
    int a = 12, b = 18;
    cout << "最小公倍数是：" << lcm(a, b) << endl;
    return 0;
}
```

在这个例子中，我们先使用`gcd()`函数计算12和18的最大公约数，然后将其用于计算它们的最小公倍数。输出将是36，因为36是12和18的最小公倍数。
*/

/*
辗转相除法（欧几里得算法）
前置定理：gcd(a,b)=gcd(b,a mod b)gcd(a,b)=gcd(b,a mod b)。

证明：

假设 c=gcd(a,b)c=gcd(a,b)，则必存在 n,mn,m 使 a=mc,b=nca=mc,b=nc;

令 r=a mod br=a mod b，即存在 kk，使 r=a−kb=mc−knc=(m−kn)cr=a−kb=mc−knc=(m−kn)c;

故 gcd(b,a mod b)=gcd(b,r)=gcd(nc,(m−kn)c)=gcd(n,m−kn)cgcd(b,a mod b)=gcd(b,r)=gcd(nc,(m−kn)c)=gcd(n,m−kn)c;

则 cc 亦为 bb 与 a mod ba mod b 的公约数;

假设 d=gcd(n,m−kn)d=gcd(n,m−kn)，则存在 x,yx,y，使 n=xd,m−kn=ydn=xd,m−kn=yd; 故 m=yd+kn=yd+kxd=(y+kx)dm=yd+kn=yd+kxd=(y+kx)d;

故有 a=mc=(y+kx)dc,b=nc=xdca=mc=(y+kx)dc,b=nc=xdc，得 gcd(a,b)=gcd((y+kx)dc,xdc)=dcgcd(a,b)=gcd((y+kx)dc,xdc)=dc;

因为 gcd(a,b)=cgcd(a,b)=c，所以 d=1d=1;

即 gcd(n,m−kn)=1gcd(n,m−kn)=1，可得 gcd(b,a mod b)=cgcd(b,a mod b)=c;

故 gcd(a,b)=c=gcd(b,a mod b)gcd(a,b)=c=gcd(b,a mod b)。

因为 gcd(a,b)=gcd(b,a mod b)gcd(a,b)=gcd(b,a mod b)，所以我们可以一直将 gcd(a,b)gcd(a,b) 转化为 gcd(x,0)gcd(x,0)，此时 xx 为 gcd(a,b)gcd(a,b)。

代码：

while (b) {

    int tmp = a % b;

    a = b;
    b = tmp;
}
时间复杂度 O(log2(a+b))O(log2(a+b))。

part3 递归（本质同 part2 一样）
毕竟道理一样，所以不想再写太多，直贴代码：

int gcd (int a, int b) {

    return b ? gcd (b, a % b) : a;
}
part4 __gcd
C++ 中自带的函数，可以求 gcd(a,b)gcd(a,b)，算法跟欧几里得算法一样，不多解释：

printf ("%d\n", __gcd (a, b));


*/