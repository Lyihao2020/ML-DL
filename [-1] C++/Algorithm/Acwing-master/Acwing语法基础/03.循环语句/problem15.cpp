// Acwing 719. 连续奇数的和 2
/*
输入 N 对整数对 X,Y，对于每对 X,Y，请你求出它们之间（不包括 X 和 Y）的所有奇数的和。

输入格式
第一行输入整数 N，表示共有 N 对测试数据。

接下来 N 行，每行输入一组整数 X 和 Y。

输出格式
每对 X,Y 输出一个占一行的奇数和。

数据范围
1≤N≤100,
−1000≤X,Y≤1000
输入样例：
7
4 5
13 10
6 4
3 3
3 5
3 4
3 8
输出样例：
0
11
5
0
0
0
12
*/

#include<iostream>
using namespace std;

int main(){

    int n;
    cin >> n;

    for(int i = 0; i < n; i++){
        int tempA, tempB, total = 0;
        cin >> tempA >> tempB;
        if(tempA > tempB) swap(tempA, tempB);
        /*
        if(tempA > tempB)
        {
            int temp = tempA;
            tempA = tempB;
            tempB = temp;
        }
        */
        // 如果%左边的操作数为负数时，则模除的结果为负数或者0，
        // 如果%左边的操作数为正数时，则模除的结构为正数或者0

        for(int j = tempA + 1; j < tempB; j++){
            if(j % 2 == 1 || j % 2 == -1){
                total += j;
            }
        }
        cout << total << endl;
    }

    return 0;
}

/*
#include<stdio.h>
int x,y,ans,t;
int main(){
    scanf("%d",&t);
    while(t--){
        ans=0;
        scanf("%d%d",&x,&y);
        for(int i=(x<y?x:y)+1;i<(x>y?x:y);i++) if(i&1) ans+=i;
        printf("%d\n",ans);
    }
}
*/

