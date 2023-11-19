// 753. 平方矩阵 I
/*
输入整数 N，输出一个 N 阶的回字形二维数组。

数组的最外层为 1，次外层为 2，以此类推。

输入格式
输入包含多行，每行包含一个整数 N。

当输入行为 N=0 时，表示输入结束，且该行无需作任何处理。

输出格式
对于每个输入整数 N，输出一个满足要求的 N 阶二维数组。

每个数组占 N 行，每行包含 N 个用空格隔开的整数。

每个数组输出完毕后，输出一个空行。

数据范围
0≤N≤100
输入样例：
1
2
3
4
5
0
输出样例：
1

1 1
1 1

1 1 1
1 2 1
1 1 1

1 1 1 1
1 2 2 1
1 2 2 1
1 1 1 1

1 1 1 1 1
1 2 2 2 1
1 2 3 2 1
1 2 2 2 1
1 1 1 1 1
*/

#include<iostream>
using namespace std;

int main(){

    int n;
    while(cin >>n, n > 0){
        for(int i = 0; i < n; i++)
        {
            for(int j = 0; j < n; j++)
                cout << min(min(n - i, n - j), min(i + 1, j + 1)) << " ";
            cout << endl;
        }
        cout << endl;
    }

    return 0;
}

/*

解法一(找规律法)
①通过观察回字形矩阵, 矩阵关于对角线是左上方和右下方对称的
②利用二维行列循环, 获取行列+1的最小值(即min(i + 1, j + 1)), 可得如下图形(例如n == 4):
1 1 1 1
1 2 2 2
1 2 3 3
1 2 3 4
可以看出未划横线部分（左上部分）满足题解,此时如果使图像沿着对角线翻转,再重合,即可求解答案
③翻转图像,采用min(n - i, n - j)即可, 得到图像如下(例如n == 4):
4 3 2 1
3 3 2 1
2 2 2 1
1 1 1 1
④进行图像的重合, 对应位置取最小值即可求解min(Left上, right下)

#include <iostream>
#include <cmath>

using namespace std;


int main(){
    int n;

    while (cin >> n, n){

        for (int i = 0; i < n; i ++){
            for(int j = 0; j < n; j ++){
                cout << min(min(i + 1, j + 1), min(n - i, n - j)) << " ";
            }
            cout << endl ;
        }
        cout << endl;
    }

    return 0;
}
解法二（曼哈顿距离法）
①当n为奇数时, 找取中间点n / 2分别于行i列j的距离的最大值(max(abs(n / 2 - i), abs(n / 2 - j))),可以的如下图形(例如n == 5):
2 2 2 2 2
2 1 1 1 2
2 1 0 1 2
2 1 1 1 2
2 2 2 2 2
②观察结果, 随着回形越深入,内外围回形相差为1, 因此想到 (n + 1) / 2
③当n为偶数时，采用同样的方法, 这里我们就让中心点在图形的中间位置 (n - 1) / 2.0, 再求解其分别于行i列j的距离的最大值(max(abs((n - 1) / 2.0 - i), abs((n - 1) / 2.0 - j)))
④再考虑所得图形与实际结果相差值,这里我们依然设置(n + 1) / 2

#include <iostream>
#include <cmath>

using namespace std;

int main(){
    int n;
    while(cin >> n, n ){

        for (int i = 0; i < n; i ++){
            for (int j = 0; j < n; j ++){
                if (n % 2) 
                    cout << (n + 1) / 2 - max(abs(n / 2 - i), abs(n / 2 - j)) << ' ';
                else
                    cout << (n + 1) / 2.0 - max(abs((n - 1) / 2.0 - i), abs((n - 1) / 2.0 - j)) << ' ';
            }
            cout << endl;
        }

        cout << endl;
    }

    return 0;
}
解法三(利用蛇形矩阵求解)
①设置一个计数器统计方向改变次数
②设置变量res表示回形当前圈数
③其他部分与蛇形矩阵相同

#include <iostream>
#include <cstring>
#include <cmath>

using namespace std;

const int N = 100 + 10;
int m[N][N];

int main(){
    int n;
    int dx[] = {-1, 0, 1, 0}, dy[] = {0, 1, 0, -1};

    while(cin >> n, n ){
        memset(m, 0, sizeof m);
        int d = 1, x = 0, y = 0;
        int cnt = 0;  // 表示改变方向次数
        int res = 1;  // 回形当前圈数
        for (int i = 0; i < n * n; i ++){
            int a = x + dx[d], b = y + dy[d];
            m[x][y] = res;

            if (a < 0 || a >= n || b < 0 || b >= n || m[a][b]){
                d = (d + 1) % 4;
                a = x + dx[d], b = y + dy[d];
                cnt ++;
                if (!(cnt % 4)) res ++;
            }
            x = a, y = b;
        }

        for (int i = 0; i < n; i ++){
            for (int j = 0; j < n; j ++)
                cout << m[i][j] << ' ';
            cout << endl;
        }
        cout << endl;
    }

    return 0;
}
*/