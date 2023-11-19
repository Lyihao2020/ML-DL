// Acwing 818. 数组排序
/*
给定一个长度为 n 的数组 a 以及两个整数 l 和 r，请你编写一个函数，void sort(int a[], int l, int r)，将 a[l]∼a[r] 从小到大排序。

输出排好序的数组 a。

输入格式
第一行包含三个整数 n，l，r。

第二行包含 n 个整数，表示数组 a。

输出格式
共一行，包含 n 个整数，表示排序完成后的数组 a。

数据范围
0≤l≤r<n≤1000
输入样例：
5 2 4
4 5 1 3 2
输出样例：
4 5 1 2 3
*/

#include<iostream>
using namespace std;

void sort(int a[], int l, int r){
    for(int i = 0; i < r - l; i++){
        for(int j = l; j < r - i; j++){
            if(a[j] > a[j + 1]) swap(a[j], a[j + 1]);
        }
    }
}

int main(){
    int n, l, r;
    cin >> n >> l >> r;
    int arr[n];
    for(int i = 0; i < n; i++) cin >> arr[i];

    sort(arr, l, r);
    for(int i = 0; i < n; i++) cout << arr[i] << " "; 

    return 0;

}

/*

题目描述
给定一个长度为 nn 的数组 aa 以及两个整数 ll 和 rr，请你编写一个函数，void sort(int a[], int l, int r)void sort(int a[], int l, int r)，将 a[l]a[l] ~ a[r]a[r] 从小到大排序。

输出排好序的数组 aa。

注意，这里的数组下标从 00 开始
样例输入
5 2 4
4 5 1 3 2
样例输出
4 5 1 2 3
哎，难度是困难？那当然是用高端解法来操作啦

算法 11
堆排序 O(nlogn)O(nlogn)
构建大根堆，每次将最大的元素放到最后

C++C++ 代码
#include <stdio.h>

int a[1005];

void swap(int i, int j)  // 技巧：手写交换，传入数组下标
{
    if (i ^ j)           // 特判 i = j 的情况，i ^ j 等价于 i != j
    {
        a[i] ^= a[j];    // 交换 a[i], a[j]
        a[j] ^= a[i];
        a[i] ^= a[j];
    }
}

void down(int l, int r, int p) // 将更小的元素
{
    int t = p;
    if ((p << 1) <= r - l && a[t] < a[(p << 1) - l])
        t = (p << 1) - l;
    if ((p << 1) + 1 - l <= r && a[t] < a[(p << 1) + 1 - l])
        t = (p << 1) + 1 - l;
    if (t != p)
    {
        swap(t, p);
        down(l, r, t);
    }
}

void heap_sort(int l, int r)
{
    for (int i = r - l >> 1; i; i -- ) // O(n)建堆
        down(l, r, i);
    while (r ^ l)        // 排序，同样用 r ^ l 代替 r != l
    {
        swap(1, r -- );  // 每次将最大的元素交换至最后，并在堆中删除
        down(l, r, 1);   // 将交换过来的元素向下交换，使剩余元素重构堆
    }
}

int main()
{
    int n, l, r;
    scanf("%d%d%d", &n, &l, &r);
    for (int i = 1; i <= n; i ++ )
        scanf("%d", &a[i]);

    heap_sort(l, r + 1);

    for (int i = 1; i <= n; i ++ )
        printf("%d ", a[i]);

    return 0;
}
算法 22
归并排序 O(nlogn)O(nlogn)
每次将数组划分成两个部分，分别处理

C++C++ 代码
#include <stdio.h>

const int N = 1005;

int a[N];
int t[N];

void merge_sort(int l,int r)
{
    if (l >= r) return;
    int mid = l + r >> 1;
    merge_sort(l, mid);
    merge_sort(mid + 1, r);
    int i = l, j = mid + 1, k = 0;
    while (i <= mid && j <= r)
        if (a[i] < a[j]) t[k ++ ] = a[i ++ ];
        else    t[k ++ ] = a[j ++ ];
    while (i <= mid) t[k ++ ] = a[i ++ ];
    while (j <= r) t[k ++ ] = a[j ++ ];
    for (int i = l, j = 0; i <= r; i ++, j ++ )
        a[i] = t[j];
}

int main()
{
    int n, l, r;
    scanf("%d%d%d", &n, &l, &r);
    for (int i = 0; i < n; i ++ )
        scanf("%d", &a[i]);

    merge_sort(l, r);

    for (int i = 0; i < n; i ++ )
        printf("%d ", a[i]);

    return 0;
}
// 懒得注释了
算法 33
快速排序 O(nlogn)O(nlogn)
每次将数组划分成两个部分，分别处理

C++C++ 代码
#include <stdio.h>

const int N = 1005;

int a[N];

void swap(int i, int j) // 由于当 i < j 的时候才会 swap，所以不用特判
{
    a[i] ^= a[j];
    a[j] ^= a[i];
    a[i] ^= a[j];
}

void quick_sort(int l,int r)
{
    if (l >= r) return;
    int x = a[l + r >> 1];
    int i = l - 1, j = r + 1;
    while (i < j)
    {
        while (a[ ++ i] < x);
        while (a[ -- j] > x);
        if (i < j) swap(i, j);
    }
    quick_sort(l, j);
    quick_sort(j + 1, r);
}

int main()
{
    int n, l, r;
    scanf("%d%d%d", &n, &l, &r);
    for (int i = 0; i < n; i ++ )
        scanf("%d", &a[i]);

    quick_sort(l, r);

    for (int i = 0; i < n; i ++ )
        printf("%d ", a[i]);

    return 0;
}
这就完了？

算法 44
三向切分快排 O(nlogn)O(nlogn)
用 ii，jj，kk 三个下标将数组切分成四部分。
a[l,i−1]a[l,i−1] 表示小于 xx 的部分，a[i,k−1]a[i,k−1]表示等于 xx 的部分，a[j+1]a[j+1] 表示大于 xx 的部分，而 a[k,j]a[k,j] 表示未判定的元素（即不知道比 xx 大，还是比中轴元素小）。
同时要注意 a[i]a[i] 始终位于等于 xx 部分的第一个元素，a[i]a[i] 的左边是小于 xx 的部分。

C++C++ 代码
#include <stdio.h>

const int N = 1005;

int a[N];

void swap(int i, int j)
{
    if (i ^ j)
    {
        a[i] ^= a[j];
        a[j] ^= a[i];
        a[i] ^= a[j];
    }
}

void quick_sort_3way(int l, int r)
{
    if(l >= r) return;
    int x = a[l];
    int i = l, j = r, k = l + 1;
    while(k <= j)
        if(a[k] < x)swap(i ++ , k ++ );
        else if(a[k] == x) k ++ ;
        else
        {
            while(a[j] > x)
                if( -- j < k)break;
            if (j < k) break;
            if(a[j] == x)
                swap(k ++ , j -- );
            else
            {
                swap(i ++ , j);
                swap(j -- , k ++ );
            }
        }
    quick_sort_3way(l, i - 1);
    quick_sort_3way(j + 1, r);
}

int main()
{
    int n, l, r;
    scanf("%d%d%d", &n, &l, &r);
    for (int i = 0; i < n; i ++ )
        scanf("%d", &a[i]);

    quick_sort_3way(l, r);

    for (int i = 0; i < n; i ++ )
        printf("%d ", a[i]);

    return 0;
}
算法 55
双轴快排 O(nlogn)O(nlogn)
同样，使用 ii，jj，kk 三个变量将数组分成四部分
同时，使用两个轴，通常选取最左边的元素作为 x1x1 和最右边的元素作 x2x2。
首先要比较这两个轴的大小，如果 x1>x2x1>x2，则交换最左边的元素和最右边的元素，以保证 x1<=x2x1<=x2。

神奇的是y总快排那题的数据把这两种优化过但不取中的快排都卡掉了。。。

C++C++ 代码
#include <stdio.h>

const int N = 1005;

int a[N];

void swap(int i, int j)
{
    if (i ^ j)
    {
        a[i] ^= a[j];
        a[j] ^= a[i];
        a[i] ^= a[j];
    }
}

void quick_sort_2(int l, int r)
{
    if(l >= r) return;
    if(a[l] > a[r]) swap(l, r);
    int x1 = a[l], x2 = a[r];
    int i = l, k = l + 1, j = r;
    while(k < j)
        if(a[k] < x1) swap( ++ i, k ++ );
        else if(a[k] >= x1 && a[k] <= x2) k ++ ;
        else
        {
            while(a[ -- j] > x2)
                if(j <= k) break;
            if (j <= k) break;
            if(a[j] >= x1 && a[j] <= x2)
                swap(k ++ , j);
            else
            {
                swap(j, k);
                swap( ++ i, k ++ );
            }
        }
    swap(l, i),swap(r, j);
    quick_sort_2(l, i - 1);
    quick_sort_2(i + 1, j - 1);
    quick_sort_2(j + 1, r);
}

int main()
{
    int n, l, r;
    scanf("%d%d%d", &n, &l, &r);
    for (int i = 0; i < n; i ++ )
        scanf("%d", &a[i]);

    quick_sort_2(l, r);

    for (int i = 0; i < n; i ++ )
        printf("%d ", a[i]);

    return 0;
}

*/

/*

1.快速排序 quick_sort

#include<iostream>
using namespace std;
const int N=1010;
int a[N];
void quick(int *a,int l,int r)
{
    if(l>=r) return;
    int l1=l-1,r1=r+1;
    int x=a[(l+r)>>1];
    while(l1<r1)
    {
        do l1++;while(a[l1]<x);
        do r1--;while(a[r1]>x);
        if(l1<r1) swap(a[l1],a[r1]);
    }
    quick(a,l,r1),quick(a,r1+1,r);
}
int main()
{
    cin.tie(0);
    ios::sync_with_stdio(false);
    int n,l,r;
    cin>>n>>l>>r;
    for(int i=0;i<n;i++) cin>>a[i];
    quick(a,l,r);
    for(int i=0;i<n;i++) cout<<a[i]<<' ';
    return 0;
}
2.希尔排序 shell_sort

#include<iostream>
using namespace std;
const int N=1010;
int a[N];
void shell(int *a,int l,int r)
{
    int step=1;
    if(step<(r-l+1)/3) step=3*(r-l+1)+1;
    while(step>=1)
    {
        for(int i=l+step;i<=r;i++)
        {
            for (int ii = i; ii - step >= l && a[ii-step]>a[ii]; ii -= step)
                swap(a[ii-step],a[ii]);
        }
        step/=2;
    }
}
int main()
{
    cin.tie(0);
    ios::sync_with_stdio(false);
    int n,l,r;
    cin>>n>>l>>r;
    for(int i=0;i<n;i++) cin>>a[i];
    quick(a,l,r);
    for(int i=0;i<n;i++) cout<<a[i]<<' ';
    return 0;
}
3.冒泡排序(未优化版) bubble_sort

#include<iostream>
using namespace std;
const int N=1010;
int a[N];
void bubble(int *a,int l,int r)
{
    for(int i=0;i<r;i++)//第i+1轮
        for(int j=l;j<r-i;j++)
            if(a[j]>a[j+1]) swap(a[j],a[j+1]);
}
int main()
{
    cin.tie(0);
    ios::sync_with_stdio(false);
    int n,l,r;
    cin>>n>>l>>r;
    for(int i=0;i<n;i++) cin>>a[i];
    bubble(a,l,r);
    for(int i=0;i<n;i++) cout<<a[i]<<' ';
    return 0;
}
4.冒泡排序(优化版) bubble_sort

#include<iostream>
using namespace std;
const int N=1010;
int a[N];
void bubble(int *a,int l,int r)
{
    bool is_order=true;
    for(int i=0;i<r;i++)//第i+1轮
    {
        for(int j=l;j<r-i;j++)
            if(a[j]>a[j+1]) swap(a[j],a[j+1]),is_order=false;
        if(is_order) break;//数组有序,不需要再排
    }
}
int main()
{
    cin.tie(0);
    ios::sync_with_stdio(false);
    int n,l,r;
    cin>>n>>l>>r;
    for(int i=0;i<n;i++) cin>>a[i];
    bubble(a,l,r);
    for(int i=0;i<n;i++) cout<<a[i]<<' ';
    return 0;
}
5.选择排序 select_sort

#include<iostream>
using namespace std;
const int N=1010;
int a[N];
void select(int *a,int l,int r)
{
  for(int i=l;i<r;i++) 
  {
      int min=i;
      for(int j=i+1;j<=r;j++)
      {
          if(a[j]<a[min]) min=j;
      }
      if(min!=i) swap(a[min],a[i]);
   }
}
int main()
{
    cin.tie(0);
    ios::sync_with_stdio(false);
    int n,l,r;
    cin>>n>>l>>r;
    for(int i=0;i<n;i++) cin>>a[i];
    select(a,l,r);
    for(int i=0;i<n;i++) cout<<a[i]<<' ';
    return 0;
}
6.插入排序 insert_sort

#include<iostream>
using namespace std;
const int N=1010;
int a[N];
void insert(int *a,int l,int r)
{
    for(int i=l+1;i<=r;i++)
    {
        for(int j=i;j-1>=l && a[j-1]>a[j];j--)
            swap(a[j-1],a[j]);
    }
}
int main()
{
    cin.tie(0);
    ios::sync_with_stdio(false);
    int n,l,r;
    cin>>n>>l>>r;
    for(int i=0;i<n;i++) cin>>a[i];
    insert(a,l,r);
    for(int i=0;i<n;i++) cout<<a[i]<<' ';
    return 0;
}
7.归并排序 merge_sort

#include<iostream>
using namespace std;
const int N=1010;
int a[N],temp[N];
void merge(int a[], int l, int r)
{
    if (l >= r) return ;
    int mid = l+r>>1;
    int t = 0, l1 = l, r1 = mid + 1;
    merge(a, l, mid), merge(a, mid + 1, r);
    while (l1 <= mid && r1 <= r)
        if (a[l1]<a[r1]) temp[t++] = a[l1++];
        else temp[t++] = a[r1++];
    while (l1 <= mid)  temp[t++] = a[l1++];
    while (r1 <= r) temp[t++]=a[r1++];
    for(int i=l,j=0;i<=r;i++,j++) a[i]=temp[j];
}
int main()
{
    cin.tie(0);
    ios::sync_with_stdio(false);
    int n,l,r;
    cin>>n>>l>>r;
    for(int i=0;i<n;i++) cin>>a[i];
    merge(a,l,r);
    for(int i=0;i<n;i++) cout<<a[i]<<' ';
    return 0;
}

*/