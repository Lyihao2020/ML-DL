// Acwing 756. 蛇形矩阵
/*
输入两个整数 n 和 m，输出一个 n 行 m 列的矩阵，将数字 1 到 n×m 按照回字蛇形填充至矩阵中。

具体矩阵形式可参考样例。

输入格式
输入共一行，包含两个整数 n 和 m。

输出格式
输出满足要求的矩阵。

矩阵占 n 行，每行包含 m 个空格隔开的整数。

数据范围
1≤n,m≤100
输入样例：
3 3
输出样例：
1 2 3
8 9 4
7 6 5
*/

#include<iostream>
using namespace std;

int main(){
    int n, m, cnt = 1;
    cin >> n >> m;
    int arr[n][m];

    int up = 0, down = n - 1, left = 0, right = m - 1;
    while(cnt <= m * n)
    {
        for(int i = left; i <= right; i++)
        {
            arr[up][i] = cnt++;
        }
        if(++up > down) break;
        for(int i = up; i <= down; i++)
        {
            arr[i][right] = cnt++;
        }
        if(--right < left) break;
        for(int i = right; i >= left; i--)
        {
            arr[down][i] = cnt++;
        }
        if(--down < up) break;
        for(int i = down; i >= up; i--)
        {
            arr[i][left] = cnt++;
        }
        if(++left > right) break;
    }

    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < m; j++)
        {
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }
    
    return 0;

}

/*
#include <iostream>

using namespace std;
const int N = 105;

int a[N][N];
int n, m;

int main() {
    cin >> n >> m;

    int left = 0, right = m - 1, top = 0, bottom = n - 1;
    int k = 1;
    while (left <= right && top <= bottom) {
        for (int i = left ; i <= right; i ++) {
            a[top][i] = k ++;
        }
        for (int i = top + 1; i <= bottom; i ++) {
            a[i][right] = k ++;
        }
        for (int i = right - 1; i >= left && top < bottom; i --) {
            a[bottom][i] = k ++;
        }
        for (int i = bottom - 1; i > top && left < right; i --) {
            a[i][left] = k ++;
        }
        left ++, right --, top ++, bottom --;
    }
    for (int i = 0; i < n; i ++) {
        for (int j = 0; j < m; j ++) {
            cout << a[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}

*/

/*

#include <iostream>

using namespace std;

int m,n;

int const N = 110;

int f[N][N];

int main()
{
    cin >> n >> m;
    int dx[4] = { 0, 1, 0, -1};
    int dy[4] = { 1, 0, -1, 0};//准备两个数值表示当前行走方向 依此为 东-南-西-北-东-...(右-下-左-上-右-...) 
    int x = 1, y = 1,d = 0;//x,y表示从(1,1)点开始行走 ， d表示初始方向为东  
    for(int i = 1; i <= n * m; i ++)
    {
        if((x + dx[d] > n || y + dy[d] > m || y + dy[d] == 0) || (f[x + dx[d]][y + dy[d]]))//判断行走的下一个状态是否碰壁 
        //( 下移时是否碰越下界 || 右移时是否越右界  || 左移时是否越左界) || (若不改变移动方向 下一点是否已经到达过)
            d = (d + 1) % 4;//碰壁后换移动方向 
        f[x][y] = i;//标记当前到达点 
        x += dx[d];
        y += dy[d];//以当前方向(可能改变也可能未改变)移动一次 
    }
    for(int i = 1; i <= n; i ++)
    {
        for(int j = 1;j <= m; j ++)
            cout << f[i][j] << ' ';
        cout << endl;
    }//输出 

    return 0;

}

*/
    

