// Acwing 822. 走方格
/*
给定一个 n×m 的方格阵，沿着方格的边线走，从左上角 (0,0) 开始，每次只能往右或者往下走一个单位距离，问走到右下角 (n,m) 一共有多少种不同的走法。

输入格式
共一行，包含两个整数 n 和 m。

输出格式
共一行，包含一个整数，表示走法数量。

数据范围
1≤n,m≤10
输入样例：
2 3
输出样例：
10
*/

#include<iostream>
using namespace std;

int solution(int n, int m){
    if(n == 0 && m == 0){
        return 1;
    }else if(n == 0 && m != 0){
        return solution(n, m - 1);
    }else if(n != 0 && m == 0){
        return solution(n - 1, m);
    }else{
        return solution(n, m - 1) + solution(n - 1, m);
    }
}

/*

#include <iostream>

using namespace std;

int f(int n, int m) // f(n,m)表示到达n,m点的方案数
{
    if(m == 0 || n == 0) return 1;//在左界或上界时 只能由一个方向接受所到来的点 所以方案数为1
    return f(n - 1, m) + f(n, m - 1);// (n,m)点可由上边或者左边接收到 固加方案数即为到达上边点与左边点的和
}

int main()
{
    int n, m;
    cin >> n >> m;
    cout << f(n,m) << endl;//f(n,m)即是答案
    return 0;
}

*/
int main(){

    int n, m;
    cin >> n >> m;

    cout << solution(n, m);
    
    return 0;

}

/*

算法1
(暴搜) (2n+m)O(2n+m)
首先题目数据范围不大，可以使用爆搜。

每次搜索中

若搜到了点 (n,m)(n,m)，那么 res++res++ 并返回
否则如果不是最下面的点，那么搜该点下面的点
如果不是最右边的点，那么搜该点右边的点
C 代码
#include <stdio.h>

int n, m;
int res;                  // res 存答案

void dfs(int x, int y)    // 爆搜函数
{
    if (x == n && y == m) // 如果搜到了点 (n, m), 那么 res ++ 并返回
    {
        res ++ ;
        return ;
    }
    if (x < n) dfs(x + 1, y); // 如果不是最下面的点，那么搜该点下面的点
    if (y < m) dfs(x, y + 1); // 如果不是最右边的点，那么搜该点右边的点
}

int main()
{
    scanf("%d %d", &n, &m);
    dfs(0, 0);            // 从点 (0, 0) 开始爆搜
    printf("%d\n", res);
    return 0;
}

算法2
(动态规划) (nm)O(nm)
f[i][j]f[i][j] 表示走到点 (i,j)(i,j) 的方案数，由于每次只能往下走或往右走，所以点 (i,j)(i,j) 只能从点 (i−1,j)(i−1,j) 或点 (i,j−1)(i,j−1) 上走过来
所以走到点 (i,j)(i,j) 的方案数是走到点 (i−1,j)(i−1,j) 的方案数与走到点 (i,j−1)(i,j−1) 的方案数之和，推出 f[i][j]=f[i−1][j]+f[i][j−1]f[i][j]=f[i−1][j]+f[i][j−1]
边界：f[i][0]=f[0][j]=1f[i][0]=f[0][j]=1
CC 代码
#include <stdio.h>

int n, m;
int f[11][11];

int main()
{
    scanf("%d %d", &n, &m);
    for (int i = 0; i <= n; i ++ )
        for (int j = 0; j <= m; j ++ )
            if (!i || !j) f[i][j] = 1; // 如果 i == 0 或 j == 0，那么 f[i][j] = 1
            else    f[i][j] = f[i - 1][j] + f[i][j - 1]; // 否则 f[i][j] = f[i - 1][j] + f[i][j - 1]
    printf("%d\n", f[n][m]);
    return 0;
}
算法3
（动态规划优化) (nm)O(nm)
用滚动数组优化一下上述dp，将空间复杂度优化至 O(m)O(m)
CC 代码
#include <stdio.h>

int n, m;
int f[11];

int main()
{
    scanf("%d %d", &n, &m);
    for (int i = 0; i <= m; i ++ )
        f[i] = 1;
    for (int i = 1; i <= n; i ++ )
        for (int j = 1; j <= m; j ++ )
            f[j] += f[j - 1];
    printf("%d\n", f[m]);
    return 0;
}
算法4
(组合数) (n+m)O(n+m)
首先将dp的数组打印出来，找下规律。

    1     1     1     1     1     1     1     1     1
    1     2     3     4     5     6     7     8     9
    1     3     6    10    15    21    28    36    45
    1     4    10    20    35    56    84   120   165
    1     5    15    35    70   126   210   330   495
    1     6    21    56   126   252   462   792  1287
    1     7    28    84   210   462   924  1716  3003
    1     8    36   120   330   792  1716  3432  6435
    1     9    45   165   495  1287  3003  6435 12870
如果你从左上往右下斜着看，不难发现这就是一个旋转后的杨辉三角
其中，数组中的第 ii 行，第 jj 个数字是杨辉三角中的第 i+ji+j 行，第 jj 个数字。（坐标为从 第 00 行，第 00 列开始）
杨辉三角中的第 nn 行，第 mm 个数正好是 Cnm=n!/m!(n−m)!，Cmn=n!/m!(n−m)!
所以我们只需要求下 Cn（n+m） 就好啦~
当然，感性的理解下，你要走到点 (n,m)(n,m)，一共必然要走 n+m 步，且必然有 n 步是往下走的，就相当于是从 n+m 步中，选出 n 步往下走，答案为 Cn（n+m）
所以我们可以通过求组合数的方式来快速求出答案。

CC 代码
#include <stdio.h>

int n, m;
long long res = 1;

int main()
{
    scanf("%d %d", &n, &m);
    int i = m + 1, j = 2;
    for (; i <= n + m; i ++ )
    {
        res *= i;
        while (j <= n && res % j == 0)
            res /= j, j ++ ; // 这里边乘边除是为了防止溢出，当然对于这题来说所有的数都乘完之后再除也是可以的
    }
    printf("%d\n", res);
    return 0;
}

*/