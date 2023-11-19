// Acwing 727. 菱形
/*
输入一个奇数 n，输出一个由 * 构成的 n 阶实心菱形。

输入格式
一个奇数 n。

输出格式
输出一个由 * 构成的 n 阶实心菱形。

具体格式参照输出样例。

数据范围
1≤n≤99
输入样例：
5
输出样例：
  *  
 *** 
*****
 *** 
  *  
*/

// 正方形实质解法

#include<iostream>
using namespace std;

int main(){
    int n;
    cin >> n;

    int cx = n / 2, cy = n / 2;

    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if(abs(i - cx) + abs(j - cy) <= n / 2){
                cout << "*";
            }else{
                cout << " ";
            }
        }
        cout << endl;
    }

    return 0;
}

/*
#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
    int n;
    cin >> n;
    int x = n / 2;

    char s[n][n];

    // 输入空格
    for (int i = 0; i < n; i ++ )
        for (int j = 0; j < n; j ++ )
            s[i][j] = ' ' ;

    // 上半部分
    for (int i = 0; i < x; i ++ )
        for (int j = x - i; j <= x + i; j ++ )
            s[i][j] = '*';

    // 中间一行  
    for (int j = 0; j < n; j ++ )
        s[x][j] = '*';

    // 下半部分
    for (int i = x + 1; i < n; i ++ )
        for (int j = i - x; j < n - i + x; j ++ )
            s[i][j] = '*';

    // 输出
    for (int i = 0; i < n; i ++ )
    {
        for (int j = 0; j < n; j ++ )
            cout << s[i][j] ;
        cout << endl;
    }

    return 0;
}

*/

/*
int x = n / 2;

for (int i = 0; i < x; i ++)
{
    for (int j = 0; j < x - i; j ++ ) cout <<' ';
    for (int j = 0; j < 2 * i + 1; j ++  ) cout << '*';
    puts("");
}

for (int i = 0; i < n - x; i ++ )
{
    for (int j = 0; j < i; j ++ ) cout << ' ';
    for (int j = 0; j < n - 2 * i; j ++ ) cout << '*';
    puts("");
}

*/

/* 重点对称反转

int x = n / 2;
for (int i = -x; i <= x; i ++ )
    {
        for (int j = 0; j < abs(i); j ++ ) cout <<' ';
        for (int j = 0; j < n - abs(i) * 2; j ++ ) cout << '*';
        puts("");
    }

*/