// Acwing 761. 字符串中的数字个数
/*
输入一行字符，长度不超过 100，请你统计一下其中的数字字符的个数。

输入格式
输入一行字符。注意其中可能包含空格。

输出格式
输出一个整数，表示字数字字符的个数。

输入样例：
I am 18 years old this year.
输出样例：
2
*/

#include<iostream>
#include<cstring>
using namespace std;

int main(){

   char str[100];
   int cnt = 0;
   gets(str);

   for(int i = 0; i < strlen(str); i++)
   {
      if(str[i] >= 48 && str[i] <= 57)
      {
         cnt++;
      }
   }

   cout << cnt << endl;

   return 0;

}

/*

#include<iostream>

using namespace std;

int main()
{
    string a;
    getline(cin,a);
    int ans = 0;
    for(int i = 0; i < a.size(); i ++)
    {
        if(a[i] <= '9' && a[i] >= '0')
        {
            ans ++;
        }
    }

    cout << ans << endl;

    return 0;
}
*/