// 遍历字符串中字符

#include<iostream>
#include<cstring>
using namespace std;

int main(){
    /*
    char a[100] = "Hello World!";

    for(int i = 0; i < strlen(a); i++)  cout << a[i] << endl;
    */

    char str[100];
    int cnt[26];
    bool flag = true;
    memset(cnt, 0, sizeof(cnt));

    // 练习：给定一个只包含小写字母的字符串，请你找到第一个仅出现一次的字符。如果没有，输出“no“

    cin >> str;
    for(int i = 0; i < strlen(str); i++)
    {
        int temp = str[i] - 97;
        cnt[temp]++;
    }

    for(int i = 0; i < 26; i++)
    {
        if(cnt[i] == 1){
            cout << (char)(i + 97) << " ";
            flag = false;
        }
    }

    if(flag) cout << "no" << endl;

    return 0;

}