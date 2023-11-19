// Acwing 760. 字符串长度
/*
给定一行长度不超过 100 的非空字符串，请你求出它的具体长度。

输入格式
输入一行，表示一个字符串。注意字符串中可能包含空格。

输出格式
输出一个整数，表示它的长度。

数据范围
1≤字符串长度≤100
字符串末尾无回车

输入样例：
I love Beijing.
输出样例：
15
*/

#include<iostream>
#include<cstring>
using namespace std;

int main(){

    string s;
    getline(cin, s);

    cout << s.size() << endl;

    return 0;

}

/*
C++ 代码（常用）
#include <iostream>
#include <cstring>

using namespace std;

int main()
{
    string a;
    getline(cin,a);
    cout<<a.size()<<endl;
    return 0;
}

算法3
C++ 代码
#include <iostream>
#include <cstring>

using namespace std;

int main()
{
    char a[105];
    cin.get(a,105);//需要注意cin.get()不会把换行符取出删除，影响下一次读入！
    cout<<strlen(a)<<endl;
    return 0;
}

算法4
C++ 代码
#include <iostream>
#include <cstring>

using namespace std;

int main()
{
    char a[105];
    cin.getline(a,105);//需要注意cin.getline()会把换行符取出删除，不影响下一次读入！
    cout<<strlen(a)<<endl;
    return 0;
}
顺带一提 cin 和 scanf读入字符串时遇到空格就停止了。


*/