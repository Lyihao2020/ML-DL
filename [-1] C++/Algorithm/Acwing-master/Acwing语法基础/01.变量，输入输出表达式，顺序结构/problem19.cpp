// Acwing 656. 钞票和硬币
/*
读取一个带有两个小数位的浮点数，这代表货币价值。

在此之后，将该值分解为多种钞票与硬币的和，每种面值的钞票和硬币使用数量不限，要求使用的钞票和硬币的总数量尽可能少。

钞票的面值是 100,50,20,10,5,2。

硬币的面值是 1,0.50,0.25,0.10,0.05 和 0.01。

经过实验证明：在本题中，优先使用面额大的钞票和硬币可以保证所用的钞票和硬币总数量最少。

输入格式
输入一个浮点数 N。

输出格式
参照输出样例，输出每种面值的钞票和硬币的需求数量。

数据范围
0≤N≤1000000.00
输入样例：
576.73
输出样例：
NOTAS:
5 nota(s) de R$ 100.00
1 nota(s) de R$ 50.00
1 nota(s) de R$ 20.00
0 nota(s) de R$ 10.00
1 nota(s) de R$ 5.00
0 nota(s) de R$ 2.00
MOEDAS:
1 moeda(s) de R$ 1.00
1 moeda(s) de R$ 0.50
0 moeda(s) de R$ 0.25
2 moeda(s) de R$ 0.10
0 moeda(s) de R$ 0.05
3 moeda(s) de R$ 0.01
*/

#include<iostream>
#include<iomanip>
using namespace std;

int main(){
    double n;
    cin >> n;
    int m = (int)(n * 100);
    int ans[] = {10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1};
    int cnt[12];

    for(int i = 0; i < 12; i++){
        cnt[i] = m / ans[i];
        m -= ans[i] * cnt[i];
    }

    cout << "NOTAS:" << endl;
    for(int i = 0; i < 6; i++) cout << cnt[i] << " nota(s) de R$ " << fixed << setprecision(2) << ans[i] / 100.0 << endl;
    cout << "MOEDAS:" << endl;
    for(int i = 6; i < 12; i++) cout << cnt[i] << " moeda(s) de R$ " << fixed << setprecision(2) << ans[i] / 100.0 << endl;
    
    return 0;
}


/*

// 如果你输入的是156.03，在变量里储存的不是156.03而是153.02999999，所以要加0.0001

#include<iostream>
#include<cmath>
#include<cstdio>
using namespace std;

int main(){
    double n;
    cin>>n;
    //钞票面额数组
    double nota[6]={100,50,20,10,5,2};
    //硬币面额数组
    double modea[6]={1,0.5,0.25,0.1,0.05,0.01};

    //钞票输出
    cout<<"NOTAS:"<<endl;
    for(int i=0;i<6;i++){
        //num为当前面额为nota[i]的钞票所需张数
        int num=int(n/nota[i]);
        printf("%d nota(s) de R$ %.2lf\n",num,nota[i]);
        n=n-num*nota[i];
    }

    //硬币输出
    cout<<"MOEDAS:"<<endl;
    for(int i=0;i<6;i++){
        //num为当前面额为modea[i]的硬币所需个数，面额最小为10e-2
        int num=int(n/modea[i]+10e-3);//通过加一个10e-3来防止精度问题
        printf("%d moeda(s) de R$ %.2lf\n",num,modea[i]);
        n=n-num*modea[i];
    }
    return 0;

}
*/