/*
字符串就是字符数组加上结束符’\0’。
可以使用字符串来初始化字符数组，但此时要注意，每个字符串结尾会暗含一个’\0’字符，因此字符数组的长度至少要比字符串的长度多1！
*/

#include<iostream>
using namespace std;

int main(){

    char arr1[] = {'C', '+', '+'};  //  列表初始化，没有空字符
    char arr2[] = {'C', '+', '+', '\0'};  // 列表初始化，含有显示空字符
    char arr3[] = "C++";  // 自动添加字符串结尾的空字符
    //char arr4[6] = "Daniel";  // 错误，没有空间存放空字符

    char str[100];

    cin >> str; // 输入字符串，遇到空格或回车就停止
    cout << str << endl; // 输出字符串，遇到空格或回车不会停止
    printf("%s\n", str);
    cout << endl;

    // 读入一串字符串包括空格
    gets(str);
    cout << str << endl;
    
    return 0;
}