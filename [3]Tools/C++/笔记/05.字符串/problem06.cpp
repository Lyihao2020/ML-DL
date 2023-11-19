// Acwing 773. 字符串插入
/*
有两个不包含空白字符的字符串 str 和 substr，str 的字符个数不超过 10，substr 的字符个数为 3。（字符个数不包括字符串结尾处的 \0。）

将 substr 插入到 str 中 ASCII 码最大的那个字符后面，若有多个最大则只考虑第一个。

输入格式
输入包括若干行，每一行为一组测试数据，格式为

str substr

输出格式
对于每一组测试数据，输出插入之后的字符串。

输入样例：
abcab eee
12343 555
输出样例：
abceeeab
12345553
*/

#include<iostream>
#include<cstring>
using namespace std;

int main(){

    string s1, s2;
    while(cin >> s1 >> s2)
    {
        int pos = 0; char m = s1[0];
        for(int i = 1; i < s1.size(); i++)
        {
            if(s1[i] > m)
            {
                m = s1[i];
                pos = i;
            }
        }
        for(int i = 0; i < s1.size(); i++)
        {
            if(i != pos)
                cout << s1[i];
            else    
                cout << s1[i] << s2;
        }
        cout << endl;
    }

    return 0;

}

/*

    string s,sub;
    while(cin >> s>>sub)
    {
        int idx=0;
        for(int i=0;i<s.size();i++)
            if(s[i] > s[idx])
            {
                idx= i;
            }
        s.insert(idx+1,sub);
        cout<<s<<endl;
    }
    
*/