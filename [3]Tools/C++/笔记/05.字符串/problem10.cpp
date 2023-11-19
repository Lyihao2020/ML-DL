// Acwing 766. 去掉多余的空格
/*
输入一个字符串，字符串中可能包含多个连续的空格，请将多余的空格去掉，只留下一个空格。

输入格式
共一行，包含一个字符串。

输出格式
输出去掉多余空格后的字符串，占一行。

数据范围
输入字符串的长度不超过 200。
保证输入字符串的开头和结尾没有空格。

输入样例：
Hello      world.This is    c language.
输出样例：
Hello world.This is c language.
*/

#include<iostream>
#include<cstring>
using namespace std;

int main(){
    
    string s;
    getline(cin, s);

    for(int i = 0; i < s.size() - 1; i++)
    {
        if(s[i] != ' ' && s[i + 1] != ' ')
            cout << s[i];
        else if(s[i] != ' ' && s[i + 1] == ' ')
            cout << s[i] << " ";
    }
    cout << s[s.size() - 1] << endl;

    return 0;

}

/*
#include<bits/stdc++.h>
using namespace std;
int main()
{
    string s;
    while(cin>>s)
    {
        cout<<s<<" ";
    }
    return 0;
}
*/

/*
#include <iostream>
using namespace std;

int main()
{
    string s;
    getline(cin, s);
    for(int i = 0; i < s.size(); i++)
        if(s[i] != ' ' || s[i+1] != ' ') cout << s[i];
    return 0;
}
*/