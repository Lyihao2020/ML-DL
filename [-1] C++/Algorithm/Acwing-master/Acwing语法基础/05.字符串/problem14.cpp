// Acwing 771. 字符串中最长的连续出现的字符
/*
求一个字符串中最长的连续出现的字符，输出该字符及其出现次数，字符串中无空白字符（空格、回车和 tab），如果这样的字符不止一个，则输出第一个。

输入格式
第一行输入整数 N，表示测试数据的组数。

每组数据占一行，包含一个不含空白字符的字符串，字符串长度不超过 200。

输出格式
共一行，输出最长的连续出现的字符及其出现次数，中间用空格隔开。

输入样例：
2
aaaaabbbbbcccccccdddddddddd
abcdefghigk 
输出样例：
d 10
a 1
*/

#include<iostream>
#include<cstring>
using namespace std;

int main(){
    int n;
    string s;
    cin >> n;

    while(n > 0 && cin >> s){
        int cnt = 1, max = 0; char c;
        int i;
        for(i = 0; i < s.size() - 1; i++){
            if(s[i] == s[i + 1]){
                cnt++;
            }else if(cnt > max){
                c = s[i];
                max = cnt;
                cnt = 1;
            }else{
                cnt = 1;
            }
        }
        if(i == s.size() - 1 && cnt > max){
            c = s[i - 1];
            max = cnt;
        }

        cout << c << " " << max << endl;
        n--;
    }

    return 0;

}

/*

#include <iostream>
using namespace std;
int main()
{
    int T;
    cin >> T;
    while(T --)
    {
        int maxn = -1;//maxn记录最大长度
        string str, maxs;//maxs记录最大长度时的字符
        cin >> str;
        for(int i = 0; i < str.size(); i ++)
        {
            int j = i;
            int cnt = 0;
            while(str[j] == str[i] && j < str.size())//当指针j没有越界且与指针i的内容相同时移动
                j ++, cnt ++;
            if(cnt > maxn)//更新最大值
                maxn = cnt, maxs = str[i];
            i = j - 1;//移动指针i
        }
        cout << maxs << " " << maxn << endl;
    }
}


*/