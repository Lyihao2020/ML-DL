// Acwing 776. 字符串移位包含问题
/*
对于一个字符串来说，定义一次循环移位操作为：将字符串的第一个字符移动到末尾形成新的字符串。

给定两个字符串 s1 和 s2，要求判定其中一个字符串是否是另一字符串通过若干次循环移位后的新字符串的子串。

例如 CDAA 是由 AABCD 两次移位后产生的新串 BCDAA 的子串，而 ABCD 与 ACBD 则不能通过多次移位来得到其中一个字符串是新串的子串。

输入格式
共一行，包含两个字符串，中间由单个空格隔开。

字符串只包含字母和数字，长度不超过 30。

输出格式
如果一个字符串是另一字符串通过若干次循环移位产生的新串的子串，则输出 true，否则输出 false。

输入样例：
AABCD CDAA
输出样例：
true
*/
#include<iostream>
#include<cstring>
using namespace std;

int main(){

    string s1, s2;
    bool flag = false;
    cin >> s1 >> s2;
    if(s1.size() < s2.size()) swap(s1, s2);

    for(int i = 0; i < s1.size(); i++){
        s1.insert(s1.end(), s1[0]);
        s1.erase(s1.begin());
        if(s1.find(s2) != string::npos){
            flag = true;
            break;
        }
    }

    if(flag){
        cout << "true" << endl;
    }else{
        cout << "false" << endl;
    }

    return 0;
}


/*

#include<bits/stdc++.h>
using namespace std;
int main(){
    string a,b,c;
    cin>>a>>b;
    if(a.size() < b.size()) swap(a,b);
    c =a+a; //整个循环移位字符串都包含了
    // size_t 是一些C/C++标准在stddef.h中定义的，size_t 类型表示C中任何对象所能达到的最大长度，它是无符号整数
    size_t t =c.find(b);   
    if(t != string::npos)puts("true");    
    else puts("false");
}

*/