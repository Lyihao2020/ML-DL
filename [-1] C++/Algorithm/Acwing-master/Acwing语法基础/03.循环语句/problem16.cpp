// Acwing 717. 简单斐波那契
/*
以下数列 0 1 1 2 3 5 8 13 21 ... 被称为斐波纳契数列。

这个数列从第 3 项开始，每一项都等于前两项之和。

输入一个整数 N，请你输出这个序列的前 N 项。

输入格式
一个整数 N。

输出格式
在一行中输出斐波那契数列的前 N 项，数字之间用空格隔开。

数据范围
0<N<46
输入样例：
5
输出样例：
0 1 1 2 3
*/

#include<iostream>
using namespace std;

int main(){
    int n, tempA = 0, tempB = 1;
    cin >> n;

    for(int i = 0; i < n; i++){
        cout << tempA << " ";
        int temp = tempA;
        tempA = tempB;
        tempB = temp + tempA;
    }

    return 0;
}

/* 高精度写法
#include<stdio.h>
#include<memory.h>
#pragma GCC optimize(3)
#define M 100001
int n,a[M],b[M],c[M],la=1,lb=1;
void add(){
    memcpy(c,b,sizeof(b));
    la=lb;
    for(int i=1;i<=lb;i++){
        b[i]+=a[i];
        if(b[i]>9&&i<lb) b[i]-=10,b[i+1]++;
    }
    if(b[lb]>9) b[lb]-=10,b[++lb]++;
    memcpy(a,c,sizeof(c));
}
int main(){
    scanf("%d",&n),b[1]=1;
    while(n--){
        for(int i=la;i;i--) printf("%d",a[i]);
        printf(" ");
        add();
    }
}
*/
/* 滚动数组
//这篇题解使用了滚动数组的知识
#include <iostream>
using namespace std;
int main()
{
    int n, a = 0, b = 1, c; // 一个输入变量和三个求值变量
    cin >> n;
    while (n -- ) // 进行n次，然后结束，等价于for(int i = 0; i < n; i ++)
    {
        cout << a << " "; // 输出第一个
        c = a + b; // 求出末项的值
        a = b; // 由于下次直接输出，所以，这里要提前滚动
        b = c; // 滚动
    }
    return 0;
}
滚动数组知识详解：
滚动数组适合求第xx项只要前几项就可以完成的定律
在斐波那契数列求解的时候，这种策略就非常适用于滚动数组
比如求第xx项的情况
*/
