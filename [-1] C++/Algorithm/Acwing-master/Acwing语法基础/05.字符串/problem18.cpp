// Acwing 777. 字符串乘方
/*
给定两个字符串 a 和 b，我们定义 a×b 为他们的连接。

例如，如果 a=abc 而 b=def， 则 a×b=abcdef。

如果我们将连接考虑成乘法，一个非负整数的乘方将用一种通常的方式定义：a0=``(空字符串)，a(n+1)=a×(an)。

输入格式
输入包含多组测试样例，每组测试样例占一行。

每组样例包含一个由小写字母构成的字符串 s，s 的长度不超过 100，且不包含空格。

最后的测试样例后面将是一个点号作为一行。

输出格式
对于每一个 s，你需要输出最大的 n，使得存在一个字符串 a，让 s=an。

输入样例：
abcd
aaaa
ababab
.
输出样例：
1
4
3
*/

#include<iostream>
#include<cstring>
using namespace std;

int main(){

    string s;
    while(cin >> s, s != "."){
        int temp = s.size();
        string newStr;
        
        for(int i = temp; i > 0; i--){
            if(temp % i == 0){
                newStr = "";
                for(int j = 0; j < i; j++){
                    newStr += s.substr(0, temp / i);
                }
                if(s == newStr){
                    cout << i << endl;
                    break;
                }
            }else{
                continue;
            }
        }
    }

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
        int flag;
        if(s[0]=='.')   break;
        int len=s.size();
        for(int i=1;i<=len;i++)
        {
            flag=0;
            if(len%i!=0)    continue;
            for(int j=0;j<len;j++)
                if(s[j]!=s[j%i])    {flag=1;break;}
            if(!flag)   {cout<<len/i<<endl;break;}
        }
        if(flag)    cout<<"-1"<<endl;
    }
}

*/

/*

算法1
STL
C++ 代码
#include<iostream>

using namespace std;

int main()
{
    string s;
    while(cin>>s,s!=".")
    {
        for(int i=s.size();i;i--)
        {
            if(s.size()%i==0)
            {
                string str,a;
                int m=s.size()/i;
                str+=s.substr(0,m);
                for(int j=0;j<i;j++)
                a+=str;
                if(a==s)
                {
                    cout<< i <<endl;
                    break;
                }
            }
        }
    }
    return 0;
}

算法2
KMP求最小循环节
C++ 代码
#include<iostream>
#include<algorithm>
#include<cstring>

using namespace std;

const int N=110;

int ne[N];
int n;

int main()
{
    char s[N];
    while(cin>>s+1 && s[1]!='.')
    {
        int n=strlen(s+1);
        for(int i=2,j=0;i<=n;i++)
        {
            while(j && s[i]!=s[j+1]) j=ne[j];
            if(s[i]==s[j+1]) j++;
            ne[i]=j;
        }
        cout<< n/(n-ne[n]) <<endl;
    }
    return 0;
}

*/