// 765. 字符串加空格
/*
给定一个字符串，在字符串的每个字符之间都加一个空格。

输出修改后的新字符串。

输入格式
共一行，包含一个字符串。注意字符串中可能包含空格。

输出格式
输出增加空格后的字符串。

数据范围
1≤字符串长度≤100
输入样例：
test case
输出样例：
t e s t   c a s e
*/

#include<iostream>
#include<cstring>
using namespace std;

int main(){
    string s;
    getline(cin, s);

    int temp = 2 * s.size();
    char newStr[temp];
    memset(newStr, ' ', temp);
    for(int i = 0, j = 0; i < temp; i += 2, j++)
        newStr[i] = s[j];
    
    for(int i = 0; i < temp; i++)
        cout << newStr[i];

    return 0;

}

/*

#include<iostream>
using namespace std;
int main()
{
    string a;
    getline(cin, a);
    for(char &c : a) cout << c << ' '; 
}

*/