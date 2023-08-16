// 练习：把一个字符串中特定的字符全部用给定的字符替换，得到一个新的字符串。

#include<iostream>
#include<cstring>
using namespace std;

int main(){

    char sym, resym;
    char str[60];
    cin >> str >> sym >> resym;

    for(int i = 0; i < strlen(str); i++)
    {
        if(str[i] == sym)
        {
            str[i] = resym;
        }
    }

    cout << str << endl;

    return 0;
}