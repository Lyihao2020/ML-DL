#include<iostream>
#include<cstdio>

using namespace std;

int main(){
    
    int a = 3;
    float b = 3.12345678;
    double c = 3.12345678;

    // a.	%8.3f, 表示这个浮点数的最小宽度为8
    // 保留3位小数，当宽度不足时在前面补空格
    printf("%5d!\n", a);
    printf("%8.4f!\n", b);
    printf("%7.3lf!\n", c);

    cout << endl;
    // %-8.3f，表示最小宽度为8，保留3位小数
    // 当宽度不足时在后面补上空格
    printf("%-5d!\n", a);
    printf("%-8.4f!\n", b);
    printf("%-7.3lf!\n", c); 

    // %08.3f, 表示最小宽度为8，保留3位小数
    // 当宽度不足时在前面补上0
    cout << endl;
    printf("%05d!\n", a);
    printf("%08.4f!\n", b);
    printf("%07.3lf!\n", c);  

    return 0;
}