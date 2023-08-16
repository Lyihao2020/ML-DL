// Acwing 775. 倒排单词
/*
编写程序，读入一行英文(只包含字母和空格，单词间以单个空格分隔)，将所有单词的顺序倒排并输出，依然以单个空格分隔。

输入格式
输入为一个字符串（字符串长度至多为 100）。

输出格式
输出为按要求排序后的字符串。

输入样例：
I am a student
输出样例：
student a am I
*/

#include<iostream>
#include<cstring>
using namespace std;

int main(){

    string s, newStr[100];
    int count = 0;
    getline(cin, s);
    s = ' ' + s + ' ';

    int i = 1;
    while(i < s.size() - 1){
        int pos = i, cnt = 0;
        while(s[pos + cnt] != ' '){
            cnt++;
        }
        for(i = pos; i < pos + cnt; i++){
            newStr[count] += s[i];
        }
        count++;
        i = pos + cnt + 1;
    }

    for(int i = count - 1; i >= 0; i--){
        cout << newStr[i] << " ";
    }

    return 0;

}

/*

#include <iostream>
using namespace std;

int main()
{
    string str, res;
    while (cin >> str)
        res = str + ' ' + res;
    cout << res;
    return 0;
}

*/