// 输入一个整数，表示时间，单位是秒。输出一个字符串，用”时:分:秒”的形式表示这个时间

#include<iostream>
#include<cstdio>
using namespace std;

int main(){

    int t;
    cin >> t;

    int h = t / 3600;
    int m = t % 3600 / 60;
    int s = t % 60;

    printf("%d : %d : %d", h, m, s);
    return 0;
}