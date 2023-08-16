// printf输出
#include<cstdio>
#include<iostream>
using namespace std;

// 使用printf时最好添加头文件 #include<cstdio>
int main(){
    float a, b;

    //cin cout 都可以用 scanf printf替换
    //但 scanf printf 不一定可以用cin cout替换，效率问题
    // cin cout 不需要考虑类型
    // double %lf  long long %lld  long double %llf
    // int %d float %f char %c bool %d
    scanf("%f%f", &a, &b);
    //%f %lf 默认保留6位小数

    printf("%.2f %.2f\n", a, b);
    printf("a + b = %.2f\na * b = %.3f\n", a + b, a * b);

    return 0;
}