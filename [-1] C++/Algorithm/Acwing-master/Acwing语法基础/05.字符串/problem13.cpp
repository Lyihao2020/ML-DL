// Acwing 770. 单词替换
/*
输入一个字符串，以回车结束（字符串长度不超过 100）。

该字符串由若干个单词组成，单词之间用一个空格隔开，所有单词区分大小写。

现需要将其中的某个单词替换成另一个单词，并输出替换之后的字符串。

输入格式
输入共 3 行。

第 1 行是包含多个单词的字符串 s;

第 2 行是待替换的单词 a(长度不超过 100);

第 3 行是 a 将被替换的单词 b(长度不超过 100)。

输出格式
共一行，输出将 s 中所有单词 a 替换成 b 之后的字符串。

输入样例：
You want someone to help you
You
I
输出样例：
I want someone to help you
*/

#include<iostream>
#include<cstring>
using namespace std;

int main(){
    string s1, s2, s3;
    int cnt = 0, pos = 0;
    getline(cin, s1); cin >> s2 >> s3;

    if(s1.size() < s2.size()){
        cout << s1 << endl;
        return 0;
    }

    while(pos < s1.size()){
        if(s1[pos] == s2[cnt] && cnt < s2.size()){
            pos++;
            cnt++;
        }else if(cnt == s2.size()){
            if(pos - cnt - 1 < 0 && s1[pos] == ' '){
                cout << s3;
                cnt = 0;
            }else if(s1[pos - cnt - 1] == ' ' && s1[pos] == ' '){
                cout << s3;
                cnt = 0;
            }else{
                cout << s1[pos - cnt];
                pos = pos - cnt + 1;
                cnt = 0;
            }
        }else{
            cout << s1[pos - cnt];
            pos = pos - cnt + 1;
            cnt = 0;
        }
    }

    if(s1[pos - cnt - 1] == ' ' && pos == s1.size()){
        cout << s3;
    }else if(pos - cnt - 1 < 0 && pos == s1.size()){
        cout << s3;
    }

    return 0;

}

/*

#include<bits/stdc++.h>
using namespace std;
string a[10000],b,d;
int main(){
    int i=0;
    while(cin>>a[i]) i++;
    for(int k=0;k<i-2;k++){
        if(a[k]==a[i-2]) cout<<a[i-1];
        else cout<<a[k];
        cout<<" ";
    }
}

*/

/*

string 函数介绍
string s1, s2;

s1.find(s2);    
// 在 s1 中查找字符串 s2，找到返回 s2 首字母在字符串中的下标，找不到返回 -1

s1.replace(pos, len, s2);
// 把 s1 中从下标 pos 开始的长度为 len 的子串替换为 s2

s1.erase(it);    
// 把 s1 字符串中迭代器 it 处的字符删除

s1.erase(pos, len);
// 把 s1 中从下标 pos 开始的长度为 len 的子串删除

c++代码：
#include <iostream> 

using namespace std;

int main()
{
    string s1, a, b;
    getline(cin, s1);
    cin >> a >> b;
    // 如果不加空格的话，比如要把a替换成b，会误把首字母是a的单词也换掉，比如and,会误换为bnd
    s1 = ' ' + s1 + ' ';    // 把单词和语句前后都加上空格 便于查找
    a = ' ' + a + ' ';
    b = ' ' + b + ' ';

    while(s1.find(a) != -1)  // 一直查找 找到就替换
        s1.replace(s1.find(a), a.size(), b);

    s1.erase(s1.begin());    // s1.erase(0, 1);
    s1.erase(s1.end() - 1);  // 别忘了把加进去的首尾空格都删除

    cout << s1;
    return 0;
}

*/