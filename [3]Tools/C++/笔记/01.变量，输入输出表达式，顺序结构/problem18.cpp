// Acwing 618. 燃料消耗
/*
一辆汽车每行驶 12 公里需要消耗 1 升汽油，现在告诉你该汽车的行驶速度 S（km/h）和行驶时间 T（h），请你计算该车在行驶过程中一共消耗了多少升汽油。

输入格式
输入共两行，第一行包含一个整数 T，表示行驶时间（h）。

第二行包含一个整数 S，表示行驶速度（km/h）。

输出格式
输出行驶期间的总油耗，结果保留三位小数。

数据范围
1≤T,S≤107
输入样例：
10
85
输出样例：
70.833
*/

/*
//本题只用scanf和printf可以做出来,但有两个小坑
#include<bits/stdc++.h>
using namespace std;
long long s,t;
//第一个坑,要开long long,因为数据有点大,int可能会爆0
double ans;
int main()
{
    scanf("%lld%lld",&t,&s);
    ans=t*s*1.0/12;
    //这道题第二个坑,乘1.0来保存小数点后的数
    printf("%.3lf",ans);
    return 0;
}
*/
#include<iostream>
#include<iomanip>
using namespace std;

int main(){
    double t, v;
    cin >> t >> v;

    double total = (t * v) / 12.0;
    cout << fixed << setprecision(3) << total;

    return 0;

}

