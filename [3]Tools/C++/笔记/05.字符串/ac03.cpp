/*

下面几个函数需要引入头文件:
#include <string.h>

(1)	strlen(str)，求字符串的长度
(2)	strcmp(a, b)，比较两个字符串的大小，a < b 返回-1，a == b 返回0，a > b返回1。这里的比较方式是字典序！
(3)	strcpy(a, b)，将字符串b复制给从a开始的字符数组。

*/

#include<iostream>
#include<cstring>
using namespace std;

int main(){

    char a[100] = "Hello World!", b[100];

    cout << strlen(a) << endl;

    strcpy(b, a);

    cout << strcmp(a, b) << endl;

    return 0;

}