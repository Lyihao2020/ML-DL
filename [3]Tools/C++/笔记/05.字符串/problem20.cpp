// Acwing 779. 最长公共字符串后缀
/*
给出若干个字符串，输出这些字符串的最长公共后缀。

输入格式
由若干组输入组成。

每组输入的第一行是一个整数 N。

N 为 0 时表示输入结束，否则后面会继续有 N 行输入，每行是一个字符串（字符串内不含空白符）。

每个字符串的长度不超过 200。

输出格式
共一行，为 N 个字符串的最长公共后缀（可能为空）。

数据范围
1≤N≤200
输入样例：
3
baba
aba
cba
2
aa
cc
2
aa
a
0
输出样例：
ba

a
*/

#include<iostream>
#include<cstring>
#define N 200
using namespace std;

int main(){

    int n;
    string str[N];
    while(cin >> n, n > 0){
        // 定义变量一定要初始化，不然为 undefined 出错
        int temp = 0, pos =0, len = -1;
        bool flag = true;
        while(temp < n){
            cin >> str[temp++];
        }
        temp = str[0].size();
        for(int i = 1; i < n; i++){
            if(str[i].size() < temp){
                temp = str[i].size();
                pos = i;
            }
        }
        for(int i = temp - 1; i >= 0; i--){
            for(int j = 0; j < n; j++){
                int a = str[j].size() - temp + i;
                if(str[pos][i] != str[j][a]){
                    len = i;
                    flag = false;
                    break;
                }
            }
            if(!flag) break;
        }
        
        if(len == temp - 1) cout << endl;
        else cout << str[pos].substr(len + 1, temp - len - 1) << endl;
    }

    return 0;
}


/*

#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
    int n;
    while(cin >> n, n)
    {
        string s, a;
        int MAX = 999999;
        cin >> s;
        for(int i = 1; i < n; ++ i)
        {
            int res = 0;
            cin >> a;
            for(int j = 0; j < a.size() && j < s.size(); ++ j)
                if(a[a.size() - 1 - j] == s[s.size() - 1 - j]) res++;
                else break;
            MAX = min(MAX, res);
        }
        if(MAX) cout << s.substr(s.size()-MAX) << endl;
        else cout << endl;
    }
    return 0;
}

*/

/*
思路
把所有字符串首尾翻转，求公共后缀就变为公共前缀，依次从前往后比较所有字符串每一位的字符是否相同，取所有字符串中最短的长度作为len，从第 0 位依次比较到第 len - 1 位，即可确定前几位是公共前缀。

c++代码
#include <iostream>
#include <algorithm>

using namespace std;

const int N = 210;

string s[N];

int main()
{
    int m;      // m个字符串
    while (cin >> m && m)
    {
        int len = 200;
        for (int i = 0; i < m; i ++)
        {
            cin >> s[i];
            reverse( s[i].begin(), s[i].end() );         // 把每个字符串首尾翻转 变后缀为前缀
            if ( s[i].size() < len) len = s[i].size();   // 取所有字符串中最短长度作为len
        }

        string a;                           // 从前往后存放相同的字符 最后一位不一定属于公共前缀
        int l = -1;
        for(int i = 0; i < len; i ++)       // 从字符串第一位依次比较
        {
            a += s[0][i];                   // 把第一个字符串的第i个字符存到a[i]中用于与后面的比较
            for (int j = 1; j < m; j ++)
                if (a[i] != s[j][i])        
                {
                    l = i;                  // 把出现不同的位数存到l中
                    break;
                }
            if (l != -1) break;             // 已经知道前缀的位数 后面的没必要判断
        }

        if (l == -1)                        // 说明没出现过a[i] != s[j][i] a中的字符都是公共前缀
            for (int i = len - 1; i >= 0; i --)  // 因为翻转过 倒序输出
            cout << a[i];
        else
            for (int i = l - 1; i >= 0; i --)    // a的第l位字符不是公共前缀 l之前的字符都是
                cout << a[i];
        cout << endl;
    }
    return 0;
}

*/