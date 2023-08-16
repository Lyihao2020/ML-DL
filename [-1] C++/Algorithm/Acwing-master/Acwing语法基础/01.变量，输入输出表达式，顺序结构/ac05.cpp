#include<iostream>
#include<cstdio>
using namespace std;

// 输入一个字符，输出一个菱形
int main(){

    char c;
    cin >> c;

    printf("  %c\n", c);
    printf(" %c%c%c\n", c, c, c);
    printf("%c%c%c%c%c\n", c, c, c, c, c);
    printf(" %c%c%c\n", c, c, c);
    printf("  %c\n", c);

}