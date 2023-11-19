// Acwing 772. 只出现一次的字符
/*
给你一个只包含小写字母的字符串。

请你判断是否存在只在字符串中出现过一次的字符。

如果存在，则输出满足条件的字符中位置最靠前的那个。

如果没有，输出 no。

输入格式
共一行，包含一个由小写字母构成的字符串。

数据保证字符串的长度不超过 100000。

输出格式
输出满足条件的第一个字符。

如果没有，则输出 no。

输入样例：
abceabcd
输出样例：
e
*/

#include<iostream>
#include<cstring>
using namespace std;

int main(){

    string s;
    cin >> s;
    int alpha[26];
    memset(alpha, 0, 26);

    for(int i = 0; i < s.size(); i++)
        alpha[s[i] - 97]++;
    
    int i;
    for(i = 0; i < s.size(); i++)
        if(alpha[s[i] - 97] == 1)
        {
            cout << s[i] << endl;
            break;
        }

    if(i == s.size())
        cout << "no" << endl;
    
    return 0;

}

/*
#include<iostream>
using namespace std;
int main()
{
    string s;
    cin>>s;
    int index=0;
    int x[100000];
    for(auto i: s)
        x[i]++;
    for(auto i:s)
    {
        if(x[i]==1)
        {
            cout<<i<<endl;
            return 0;
        }
    }
    cout<<"no"<<endl;
}
*/

/*
#include<iostream>
#include<cstdio>
#include<string>
using namespace std;
int main()
{
    string A;
    bool s=0;
    while(getline(cin,A))
    {
        for(int i=0;i<A.size();i++)
        {
            if(A.find(A[i])==A.rfind(A[i]))
            {
                cout<<A[i]<<endl;
                s=1;
                break;
            }
        }
    }
    if(s==0)
        cout<<"no"<<endl;
    return 0;
}
*/

