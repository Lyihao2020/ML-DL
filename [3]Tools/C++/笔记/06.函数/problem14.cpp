// Acwing 821. 跳台阶
/*
一个楼梯共有 n 级台阶，每次可以走一级或者两级，问从第 0 级台阶走到第 n 级台阶一共有多少种方案。

输入格式
共一行，包含一个整数 n。

输出格式
共一行，包含一个整数，表示方案数。

数据范围
1≤n≤15
输入样例：
5
输出样例：
8
*/

#include<iostream>
#include<cmath>
using namespace std;

int solution(int n){

    if(n == 1){
        return 1;
    }else if(n == 2){
        return 2; 
    }else{
        return solution(n - 1) + solution(n - 2);
    }

}

int main(){
    int n;
    cin >> n;

    cout << solution(n) << endl;

    return 0;

}

/*
解题思路
先自己手动列举一下，

台阶/级	步数/步
1	1
2	2
3	3
4	5
5	8
6	13
根据以上列举，不难发现，这就是一斐波那契数列！

算法1
递归
说人话就是到这一级的步数等于到上一级的方案数和上上级的方案数，
而第一级台阶方案数为1，第二级台阶方案数为2，后面的步骤就是有手就行了。

C++ 代码
#include <bits/stdc++.h>
using namespace std;

int n;

int dg(int dep)
{
    if (dep == 1)  return 1;
    if (dep == 2)  return 2; //终止条件
    return dg(dep - 1) + dg(dep - 2);
}

int main()
{
    scanf("%d", &n);
    printf("%d\n", dg(n)); //用递归
    return 0;
}
算法2
for循环
C++代码
#include <bits/stdc++.h>
using namespace std;

int a[20], n;

int main()
{
    a[1] = 1;
    a[2] = 2;
    for (int i = 3; i <= 15; i++) ]
        a[i] = a[i - 1] + a[i - 2];
    scanf("%d", &n);
    printf("%d\n", a[n]);
    return 0;
}
算法3
#include <bits/stdc++.h>
using namespace std;
int n;
int cmt=0;
void f(int k)
{
  if(k==n) cmt++;
  else if(k<n)
  {
    f(k+1);
    f(k+2);
  }
}
int main()
{

  cin>>n;
  f(0);
  cout<<cmt<<endl;
  return 0;
}
算法4:DP
#include <bits/stdc++.h>
using namespace std;
int n, a[20];
int main() {
    scanf("%d", &n);
    a[0] = 1;
    for (int i = 1;i <= n; i++) {
        a[i] += a[i - 1];
        if (i > 1) a[i] += a[i - 2];
    }
    printf("%d", a[n]);
    return 0;
}

*/