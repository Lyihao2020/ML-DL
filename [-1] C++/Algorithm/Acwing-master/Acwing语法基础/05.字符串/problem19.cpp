// Acwing 778. 字符串最大跨距
/*
有三个字符串 S,S1,S2，其中，S 长度不超过 300，S1 和 S2 的长度不超过 10。

现在，我们想要检测 S1 和 S2 是否同时在 S 中出现，且 S1 位于 S2 的左边，并在 S 中互不交叉（即，S1 的右边界点在 S2 的左边界点的左侧）。

计算满足上述条件的最大跨距（即，最大间隔距离：最右边的 S2 的起始点与最左边的 S1 的终止点之间的字符数目）。

如果没有满足条件的 S1，S2 存在，则输出 −1。

例如，S= abcd123ab888efghij45ef67kl, S1= ab, S2= ef，其中，S1 在 S 中出现了 2 次，S2 也在 S 中出现了 2 次，最大跨距为：18。

输入格式
输入共一行，包含三个字符串 S,S1,S2，字符串之间用逗号隔开。

数据保证三个字符串中不含空格和逗号。

输出格式
输出一个整数，表示最大跨距。

如果没有满足条件的 S1 和 S2 存在，则输出 −1。

输入样例：
abcd123ab888efghij45ef67kl,ab,ef
输出样例：
18
*/

/*

如果要读取以逗号分隔的多个字符串，可以使用 `%[^,]` 格式说明符来读取除了逗号以外的字符。具体步骤如下：

1. 声明一个字符数组 `str` 来存储读入的字符串。
2. 使用 `scanf` 函数来读取以逗号分隔的字符串序列，格式为 `" %[^,],%[^,],%[^,],..., %[^\n]"`。其中 `%[^,]` 表示读入除逗号以外的任意字符序列（不包括空格）， `,` 表示读入逗号，并用空格跳过之前的空格，`%[^\n]` 表示读取一行末尾的换行符之前的所有字符。
3. 使用读取到的字符串进行后续处理。

例如，假设要读取三个以逗号隔开的字符串，可以使用以下代码：

```c++
char str1[20], str2[20], str3[20];
scanf(" %[^,], %[^,], %[^\n]", str1, str2, str3);
```

在输入时，需要注意每个字符串中间的逗号后面不能有空格，否则会导致读取失败。如果需要容忍输入中有空格，可以将格式说明符中的空格改成 `%*[ ]`，表示忽略一个或多个空格，例如：

```c++
char str1[20], str2[20], str3[20];
scanf("%[^,]%*[ ],%*[ ]%[^,]%*[ ],%*[ ]%[^\n]", str1, str2, str3);
```

这样即使输入中有多余的空格，也可以正确读取每个字符串。

*/

#include<iostream>
#include<cstring>
using namespace std;

int main(){

    char str1[300], str2[10], str3[10];
    scanf(" %[^,], %[^,], %[^\n]", str1, str2, str3);

    int posA = strlen(str1) + 1, posB = -1;
    bool flagA = true, flagB = true;
    for(int i = 0; i < strlen(str1) ; i++){
        int pos = i;
        if(flagA){
            for(int j = 0; j < strlen(str2); j++){
                if(str1[pos] == str2[j]){
                  pos++;
                }
            }
            if(pos - i == strlen(str2)){
                posA = pos;
                flagA = false;
            }
        }
        pos = strlen(str1) - 1 - i;
        if(flagB){
            for(int j = strlen(str3) - 1; j >= 0; j--){
                if(str1[pos] == str3[j]){
                    pos--;
                }
            }
            if(strlen(str1) - i - 1 - pos == strlen(str3)){
                posB = pos;
                flagB = false;
            }
        }
        if(!flagA && !flagB) break;
    }
    
    if(posA - 1 > posB) cout << "-1" << endl;
    else cout << posB - posA + 1 << endl;

    return 0;

}

/*

算法1
缺点1：在读入这个字符串 讲其转化为 3个字符串不够简洁
可以将其改进为：
（方法一）string s, s1, s2;
    char c;
    while (cin >> c, c != ',') s += c;
    while (cin >> c, c != ',') s1 += c;
    while (cin >> c) s2 += c;
(方法二) string s,s1,s2;
    getline(cin,s,',');
    getline(cin,s1,',');
    getline(cin,s2,'\n');
缺点2：自己在查找第二个字符串的时候从前往后查找 会浪费时间
可以改进为从后往前找 使得代码更加高效
C++ 代码
#include <iostream>
using namespace std;
int main(){
    string str;
    getline(cin,str);
    int a[2]={0};
    for(int i=0,j=0;i<str.size();i++){
        if(str[i] == ','){
            a[j]=i;
            j++;
        }
    }
    string s  = str.substr(0,a[0]);
    string s1 = str.substr(a[0]+1,a[1]-a[0]-1);
    string s2 = str.substr(a[1]+1);
    int p1=0,p2=0;
    bool flag1=false,flag2=false;
    for(int i=0;i<s.size();i++){
        for(int j=i,cnt=0,k=0;j <s.size();j++){
            if(s[j] == s1[k++] ) cnt++;
            else break;
            if (cnt == s1.size()){
                p1 = i + s1.size() ; 
                flag1 = true;
                break;
            }
        }
        if(flag1) break;
    }
    for(int i=0;i<s.size();i++){
        for(int j=i,cnt=0,k=0; j < s.size() ; j++ ){
            if(s[j] == s2[k++] ) cnt++;
            else break;
            if (cnt == s2.size()){
                p2 = i ;
                flag2 = true;
                break;
            }
        }
    }
    int outcome=p2-p1;
    if(flag1 == false || flag2==false || p1>=p2 ) cout << "-1" << endl;
    else cout << outcome << endl;
    return 0;
}

*/

/*

find 大法好
s.find();    // 在字符串s上从前往后找
s.rfind();   // 从后往前
s.find(s1)的返回值为所查找的子串的第一个字符的位置，找不到返回 -1

#include <iostream> 

using namespace std;

int main()
{
    string s, s1, s2, a;
    getline(cin, a);

    int f1, f2;                      // 两个','的位置
    f1 = a.find(',');
    f2 = a.rfind(',');
    s = a.substr(0, f1);
    s1 = a.substr(f1 + 1, f2 - f1 - 1);
    s2 = a.substr(f2 + 1);


    int l, r;
    l = s.find(s1);                   // 在字符串s上从左往右找s1
    r = s.rfind(s2);                  // 在字符串s上从右往左找s2

    if (l == -1 || r == -1)           // s1 或 s2 不在 s 上
    { 
        cout << "-1";
        return 0;
    }

    l = s.find(s1)  + s1.size() - 1;   // l为s1最右面的下标

    if ( l >= r )                      // s1 s2 交叉
        cout << "-1";
    else cout << r - l - 1;

    return 0;
}

*/