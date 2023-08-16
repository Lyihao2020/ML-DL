// Acwing 768. 忽略大小写比较字符串大小
/*
一般我们用 strcmp 可比较两个字符串的大小，比较方法为对两个字符串从前往后逐个字符相比较（按 ASCII 码值大小比较），直到出现不同的字符或遇到 \0 为止。

如果全部字符都相同，则认为相同；如果出现不相同的字符，则以第一个不相同的字符的比较结果为准。

但在有些时候，我们比较字符串的大小时，希望忽略字母的大小，例如 Hello 和 hello 在忽略字母大小写时是相等的。

请写一个程序，实现对两个字符串进行忽略字母大小写的大小比较。

输入格式
输入为两行，每行一个字符串，共两个字符串。注意字符串中可能包含空格。

数据保证每个字符串的长度都不超过 80。

输出格式
如果第一个字符串比第二个字符串小，输出一个字符 <。

如果第一个字符串比第二个字符串大，输出一个字符 >。

如果两个字符串相等，输出一个字符 =。

输入样例：
Hello
hello
输出样例：
=
*/

#include<iostream>
#include<cstring>
using namespace std;

int main(){
    string s1, s2;
    getline(cin, s1);
    getline(cin, s2);
    bool flag = true;

    for(int i = 0; i < min(s1.size(), s2.size()); i++)
    {
        s1[i] = (s1[i] < 97)? s1[i] + 32: s1[i];
        s2[i] = (s2[i] < 97)? s2[i] + 32: s2[i];
        if(s1[i] > s2[i]){
            cout << ">" << endl; flag = false; break;
        }else if(s2[i] > s1[i]){
            cout << "<" << endl; flag = false; break;
        }
    }

    if(flag){ 
        if(s1.size() == s2.size()) cout << "=" << endl;
        else if(s1.size() > s2.size()) cout << ">" << endl;
        else cout << "<" << endl;
    }

    return 0;

}

/*
#include <iostream>
#include <string>
#include <cstring>

using namespace std;

int main()
{
    string a,b;
    getline(cin,a);
    getline(cin,b);

    for (int i = 0; i < a.size(); i ++)
        if (a[i] >= 'A' && a[i] <= 'Z') a[i] += 32;

    for (int i = 0; i < b.size(); i ++)
        if (b[i] >= 'A' && b[i] <= 'Z') b[i] += 32;

    int c;
    c = strcmp(a.c_str(),b.c_str());
    if(c < 0) cout << "<";
    if(c == 0) cout << "=";
    if(c > 0) cout << ">";

    return 0;
}

*/

/*
#include<iostream>
using namespace std;
int main()
{
    string a,b;
    getline(cin,a);
    getline(cin,b);
    for(auto &c:a) c = tolower(c);
    for(auto &c:b) c = tolower(c);
    if(a == b) cout << '=';
    if(a > b) cout << '>';
    if(a < b) cout << '<';
}
*/