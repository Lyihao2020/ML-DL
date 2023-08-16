// Acwing 823. 排列
/*
给定一个整数 n，将数字 1∼n 排成一排，将会有很多种排列方法。

现在，请你按照字典序将所有的排列方法输出。

输入格式
共一行，包含一个整数 n。

输出格式
按字典序输出所有排列方案，每个方案占一行。

数据范围
1≤n≤9
输入样例：
3
输出样例：
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
*/

#include<iostream>
#define N 9
using namespace std;

int n;
int arr[N];
bool st[N];

// 显示数组
void show(int arr[], int n){
    for(int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;
}

void dfs(int sym){

    if(sym == n){
        show(arr, n);
        return;
    }else{
        for(int i = 1; i <= n; i++){
            if(!st[i]){
                st[i] = true;
                arr[sym] = i;
                dfs(sym + 1);
                st[i] = false;
            }
        }
    }

}

int main(){

    cin >> n;

    dfs(0);

    return 0;

}

/*
解法一：dfs
题目分析：因为要按照字典序大小排列数字，因此这里的递归要按照字典序，从1开始到n从大到小依次遍历。又因为每一个数字都要进行输出，因此还需要对每个位置上的数字进行遍历。
思路：从第一个位置开始递归，从数字1到n进行考虑所有情况，然后开始第二个位置的递归，直到全部遍历完成。

递归搜索树


代码
#include<iostream>
#include<cstring>
using namespace std;

const int N = 10;//根据题目，最大数字是9
int q[N];//存储的是遍历到的数字
bool st[N];//判断数字是否被遍历
int n;//这里n一定要定义再全局变量里面，因为下面这个函数需要使用

//深度优先搜索遍历
void dfs(int u)
{
    //当遍历到最后一层的时候,先输出，再退出
    if(u == n)
    {
        for(int i = 0 ; i<n ; i++) cout<<q[i]<<" ";
        cout<<endl;
        return;//退出函数
    }

    for(int i = 1 ; i <=n ; i++)//按字典序遍历数字
        if(!st[i])//当这个数字不存在于q[]数组中,可以进入，否则继续遍历
        {
            q[u] = i;//存入数字
            st[i] = true;//先将数字进行标记
            dfs(u+1);//进入下一层
            st[i] = false;//当从下一层出来的时候，这个数字也不再被标记
        }
}

int main()
{
    cin>>n;

    dfs(0);

    return 0;
}
解法二：next_permutation()
介绍：next_permutation函数将按字母表顺序生成给定序列的下一个较大的排列，直到整个序列为降序为止。注意添加头文件#include<algorithm>

使用方法：next_permutation(数组头地址，数组尾地址);
若下一个排列存在，则返回真，如果不存在则返回假
若求上一个排列，则用prev_permutation

详见寒假每日一题(入门组) Week4 火星人

代码一：直接使用next_permutation()
#include<iostream>
#include<algorithm>//注意添加头文件
using namespace std;

int q[10];//1 ~ 9最多9个数字 
int n;

int main()
{
    cin>>n;

    //输入数字 1 ~ n
    for(int i = 0 ; i<n ; i++)
        q[i] = i+1;

    //输出字典序最小的排列
    for(int i = 0 ; i<n ; i++)
        cout<<q[i]<<" ";
    cout<<endl;

    //当存在比当前字典序更大的排列时，next_permutation()返回真，直到没有更大的排列的时候才退出循环
    while(next_permutation(q,q+n))//利用next_permutation()自动找到下一个更大的字典序
    {
        //输出更大的排列
        for(int i = 0 ; i<n ; i++)
            cout<<q[i]<<" ";
        cout<<endl;
    }

    return 0;
}
手写next_permutation()思路


代码二：手写next_permutation()
#include<iostream>
#include<algorithm>
using namespace std;

int a[12];

bool turn(int a[] ,int n)
{
    int k = n - 1; 
    while(a[k-1] > a[k]) k--;//找到位置k

    //当k的位置是0的时候，说明整个排列时递减的，这个排列的字典序最大
    if(k == 0) return false;//因此返回false

    k = k - 1;
    int t = n - 1;
    while(a[k] > a[t]) t--;//从后往前找到第一个大于a[k]的数字的位置 
    swap(a[k] , a[t]);//交换
    reverse(a + k + 1, a + n);//翻转

    return true;//返回true
}

int main()
{
    int n;
    cin>>n;

    for(int i = 0 ; i<n ; i++) a[i] = i + 1;//输入
    for(int i = 0 ; i<n ; i++) cout<<a[i]<<" ";//输出
    cout<<endl;

    while(turn(a, n))
    {
        //输出进行一个排序后的排列
        for(int i = 0 ; i<n ; i++) cout<<a[i]<<" ";
        cout<<endl;
    }


    return 0;
}

解法3:
dfs排列(含详细伪代码，易理解)
y总代码
#include <iostream>
using namespace std;
const int N = 10;
int n;
void dfs(int u, int nums[], bool st[])
{
    if (u > n)
    {
        for (int i = 1; i <= n; i ++ ) printf("%d ", nums[i]);
        puts("");
    }
    else
    {
        for (int i = 1; i <= n; i ++ )
            if (!st[i])
            {
                st[i] = true;
                nums[u] = i;
                dfs(u + 1, nums, st);
                st[i] = false;  // 恢复现场
            }
    }
}
int main()
{
    scanf("%d", &n);
    int nums[N];
    bool st[N] = {0};
    dfs(1, nums, st);
    return 0;
}
伪代码(n=3时，第一组数据(123，132)产生过程）
i=1(st[1]==0)i=1
st[1]=1     //st[i]=true;
num[1]=1    //num[u]=i;
    i=1(st[1]==1,st[2]==0)i=2//缩进表示递归层数
    st[2]=1
    num[2]=2
        i=1(st[1,2]==1,st[3]==0)i=3
        st[3]=1
        num[3]=3
            u=4>3//输出num,并中止调用
        st[3]=0//if结束时，恢复现场
    st[2]=0//if结束时，恢复现场
    i=3(st[3]==0)i=3
    st[3]=1
    num[2]=3
        i=1(st[1]==1,st[2]==0)i=2
        st[2]=1
        num[3]=2
            u=4>3
        st[2]=0
    st[3]=0
i=2(st[2]==0)i=2


*/