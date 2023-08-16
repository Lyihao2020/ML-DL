// 可以将string对象当成字符数组来处理：
// 或者使用基于范围的for语句：

#include<iostream>
#include<cstring>
using namespace std;

int main(){
    /*
    string s = "Hello World!";
    for(int i = 0; i < s.size(); i++)
    {
        cout << s[i] << endl;
    }

    for(char c : s) cout << c << endl;
    for(char &c : s) c = 'a';
    cout << s << endl;
    */

    // 练习：密码翻译，输入一个只包含小写字母的字符串，将其中的每个字母替换成它的后继字母，如果原字母是’z’，则替换成’a’。
    string s1;
    cin >> s1;
    /*
    for(char&c : s1) c += 1;
    cout << s1 << endl;
    */
    // 练习：输入两个字符串，验证其中一个串是否为另一个串的子串。

    string s2;
    cin >> s2;

    bool flag = true;
    for(int i = 0; i < s1.size(); i++)
    {
        int temp = i;
        flag = true;
        for(int j = 0; j < s2.size(); j++)
        {
            if(s1[temp] == s2[j])
            {
                temp++;
            }
            else
            {
                flag = false;
                break;
            }
        }
        if(flag) break; 
    }
    cout << flag << endl;

    return 0;

}