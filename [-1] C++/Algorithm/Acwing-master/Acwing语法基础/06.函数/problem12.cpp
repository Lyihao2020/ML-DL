// Acwing 817. 数组去重
/*
给定一个长度为 n 的数组 a，请你编写一个函数：

int get_unique_count(int a[], int n);  // 返回数组前n个数中的不同数的个数
输入格式
第一行包含一个整数 n。

第二行包含 n 个整数，表示数组 a。

输出格式
共一行，包含一个整数表示数组中不同数的个数。

数据范围
1≤n≤1000,
1≤ai≤1000。

输入样例：
5
1 1 2 4 5
输出样例：
4
*/

#include<iostream>
using namespace std;

int get_unique_count(int a[], int n){
    int cnt = 0; bool flag;
    for(int i = 0; i < n ; i++){
        flag = true;
        for(int j = i + 1 ; j < n; j++){
            if(a[i] == a[j]){
                flag = false;
                break;
            }
        }
        if(flag) cnt++;
    }
    return cnt;
}

int main(){
    int n; 
    cin >> n;
    int arr[n];
    for(int i = 0; i < n; i++) cin >> arr[i];

    cout << get_unique_count(arr, n) << endl;

    return 0;

}

/*

int get_unique_count(int a[], int n)
{
    for(int i=1;i<=n;i++)
    {
        if(b[a[i]]==0)
        t++,b[a[i]]=1;
    }
    return t;
}
*/

/*

#include <bits/stdc++.h>
using namespace std;
int main(void){
    int n,s[1010];
    cin>>n;
    for(int i=0;i<n;i++)    cin>>s[i];
    sort(s,s+n);
    int t=unique(s,s+n)-s;
    cout<<t;
}

*/ 

/*

 unique（C++）函数的功能是元素去重。即”删除”序列中所有相邻的重复元素(只保留一个)。

 此处的删除，并不是真的删除，就是把重复元素的位置让不重复元素使用。

由于它”删除”的是相邻的重复元素，所以在使用unique函数之前，一般都会将目标序列进行排序。

下面来一道洛谷例题：

题目描述
明明想在学校中请一些同学一起做一项问卷调查，为了实验的客观性，他先用计算机生成了NN个11到10001000之间的随机整数(N≤100)(N≤100)，对于其中重复的数字，只保留一个，把其余相同的数去掉，不同的数对应着不同的学生的学号。然后再把这些数从小到大排序，按照排好的顺序去找同学做调查。请你协助明明完成“去重”与“排序”的工作。

输入格式
输入有两行，第11行为11个正整数，表示所生成的随机数的个数NN

第22行有NN个用空格隔开的正整数，为所产生的随机数。

输出格式
输出也是两行，第11行为11个正整数MM，表示不相同的随机数的个数。

第22行为MM个用空格隔开的正整数，为从小到大排好序的不相同的随机数。

输入输出样例
输入 #1复制

10
20 40 32 67 40 20 89 300 400 15
输出 #1复制

8
15 20 32 40 67 89 300 400
#include<bits/stdc++.h>
using namespace std;
int main()
{
	int n,i;
	cin>>n;
	int a[100000];//我就是定义一个足够大的数组,这里不是重点
	for(i=0;i<n;i++)
	{
		cin>>a[i];
	}
	sort(a,a+n);//这里就是排序
	int x=unique(a,a+n)-a;//关键点来了
	cout<<x<<endl;//x就是排序后没有重复元素的长度
	for(i=0;i<x;i++)
	{
		cout<<a[i]<<" ";
	}
	return 0;

}
*/

/*

C++中unique函数
文章一：
unique是STL中很实用的函数之一，需要#include（感谢各位提醒），下面来简单介绍一下它的作用。

unique的作用是“去掉”容器中相邻元素的重复元素，这里去掉要加一个引号，为什么呢，是因为它实质上是一个伪去除，它会把重复的元素添加到容器末尾，而返回值是去重之后的尾地址（是地址！！），举个例子：

int num[10]={1,1,2,2,2,3,4,5,5,5};
int ans=unique(num,num+10)-num;  //去重函数返回地址为：去重后最后一个不重复元素地址

这时，返回的ans是5，而num中前5项就是1,2,3,4,5，一般使用前需要对容器进行排序，这样才能实现对整个数组去重。

另：如果要对结构体进行这一操作，需要重载运算符"=="，具体要根据自己需要重载。

原文链接：https://blog.csdn.net/u014598631/article/details/34884809

c++ unique函数详解
文章二：
unique是 c++标准模板库STL中十分实用的函数之一，使用此函数需要#include 头文件

该函数的作用是“去除”容器或者数组中相邻元素的重复出现的元素
(1) 这里的去除并非真正意义的erase，而是将重复的元素放到容器的末尾，返回值是去重之后的尾地址。
(2) unique针对的是相邻元素，所以对于顺序顺序错乱的数组成员，或者容器成员，需要先进行排序，可以调用std::sort()函数

使用示例:

#include <iostream>
#include <algorithm>
int main(void){
    int a[8] = {2, 2, 2, 4, 4, 6, 7, 8};
    int c;
    std::sort(a, a + 8);  //对于无序的数组需要先排序
    c = (std::unique(a, a + 8) - a );
    std::cout<< "c = " << c << std::endl;//去重函数返回地址为：去重后最后一个不重复元素地址
    //打印去重后的数组成员
    for (int i = 0; i < c; i++)
        std::cout<< "a = [" << i << "] = " << a[i] << std::endl;
    return 0;
}

运行结果：

返回值c等于5，而a数组的前5项为2、4、6、7、8。

对于容器的操作类似:

std::vector<int> ModuleArr;
//排序
std::sort(ModuleArr.begin(), ModuleArr.end());
//去重
ModuleArr.erase(unique(ModuleArr.begin(), ModuleArr.end()), ModuleArr.end());


*/