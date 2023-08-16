// Acwing 751. 数组的左方区域
/*
输入一个二维数组 M[12][12]，根据输入的要求，求出二维数组的左方区域元素的平均值或元素的和。

数组的两条对角线将数组分为了上下左右四个部分，如下图所示，黄色部分为对角线，绿色部分为左方区域：

UOJ_1189.png

输入格式
第一行输入一个大写字母，若为 S，则表示需要求出左方区域的元素的和，若为 M，则表示需要求出左方区域的元素的平均值。

接下来 12 行，每行包含 12 个用空格隔开的浮点数，表示这个二维数组，其中第 i+1 行的第 j+1 个数表示数组元素 M[i][j]。

输出格式
输出一个数，表示所求的平均数或和的值，保留一位小数。

数据范围
−100.0≤M[i][j]≤100.0
输入样例：
S
4.7 -3.3 -2.3 4.5 -7.0 8.7 -4.1 -3.0 -7.6 6.3 -6.6 -4.7
-7.2 9.3 -7.6 9.1 9.2 9.0 5.5 -7.5 -9.3 -1.6 -3.5 -4.2
0.5 -7.5 -8.3 -9.0 -6.4 3.8 0.1 -3.5 7.9 2.1 2.4 -6.2
7.0 5.7 -9.0 -5.8 1.6 2.6 -9.2 -6.2 4.6 8.2 -8.3 -1.4
3.8 -9.9 6.2 -2.5 -3.5 9.4 1.6 7.0 3.3 -0.5 6.7 6.0
1.6 -3.8 5.0 8.8 4.2 7.7 0.7 7.4 7.9 -5.9 4.4 3.3
3.7 6.2 6.7 -1.4 6.1 -6.0 8.5 9.1 5.7 -4.2 5.9 -3.5
5.0 0.3 2.2 -3.6 6.3 -10.0 9.5 -4.7 2.7 8.1 7.5 -8.4
-5.7 -0.3 -3.7 -3.3 7.7 9.3 -1.3 1.0 0.3 1.9 9.9 9.0
-7.4 1.3 -9.6 -3.6 2.2 3.4 -3.6 3.5 8.3 0.5 9.7 -6.8
1.0 -2.7 -1.5 5.4 -6.5 -3.7 5.6 8.0 -9.9 0.1 2.2 7.6
5.6 4.3 1.5 -0.8 5.8 -5.1 5.5 6.2 -5.8 8.8 -0.6 -2.3
输出样例：
13.3
*/

#include<iostream>
#include<iomanip>
#include<cmath>
using namespace std;

int main(){
    double total = 0;
    char sym;
    int num = 0;
    cin >> sym;

    for(double i = -6; i < 6; i++)
        for(double j = 0; j < 12; j++)
        {
            double temp;
            cin >> temp;
            if(j < 5 - abs(i + 0.5))
            {
                total += temp;
                num++;
            }
        }
    
    cout << fixed << setprecision(1) << ((sym == 'S')? total: total / num);

    return 0;
}

/*

//数组的左方区域:(i+j)<=10&&i>j
#include <iostream>
using namespace std;
int main()
{
    char a;
    cin>>a;

    double s=0;
    for(int i=0;i<12;i++)
    {
        for(int j=0;j<12;j++)
        {
            double a;
            cin>>a;
            if((i+j)<=10&&i>j) // 规律
            s+=a;
        }
    }
    printf("%.1lf", a=='S' ? s : s/30);

}

*/