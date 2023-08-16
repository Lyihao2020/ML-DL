#include<iostream>
#include<cstdio>
#include<vector>
using namespace std;

/*
之前C语言里面用int arr[]定义数组，它的缺点是数组的长度不能随心所欲的改变
⽽C++⾥⾯有⼀个能完全替代数组的动态数组vector
它能够在运行阶段设置数组的长度、在末尾增加新的数据、在中间插⼊新的值、长度任意被改变
很好用，它在头文件# include <vector>⾥⾯，也在命名空间std⾥⾯
所以使用的时候要引入头文件vector和using namespace std; 
vector、stack、queue、map、set这些在C++中都叫做容器，这些容器的大小都可以⽤ .size() 取到
就像string s的长度⽤ s.length() 获取⼀样
string其实也可以⽤ s.size() 
不过对于vector、stack、queue、map、set这样的容器我们⼀般讨论它的大小size
字符串⼀般讨论它的长度length，其实string⾥⾯的size和length两者是没有区别、可以互换使⽤的。
*/

int main(){

	vector<int> v1;	//定义了一个vector v1， 定义的时候没有分配大小
	cout << v1.size();
	/*
	vector可以⼀开始不定义大小
	之后⽤resize分配大小，也可以⼀开始就定义大小
	之后还可以对它插入删除动态改变它的大小
	⽽且不管在main函数⾥还是在全局中定义，它都能够直接将所有的值初始化为0
	（不⽤显式地写出来，默认就是所有的元素为0）*/

	vector<int> v2(10);	//直接定义⻓度为10的int数组，默认这10个元素值都为0
	vector<int> v3;
	v3.resize(8); //先定义⼀个vector变量v1，然后将⻓度resize为8，默认这8个元素都是0
	// 在定义的时候就可以对vector变量进⾏初始化
	vector<int> v4(100, 9);// 把100⻓度的数组中所有的值都初始化为9
	// 访问的时候像数组⼀样直接⽤[]下标访问即可(也可以⽤迭代器访问，下⾯会讲)
	v4[1] = 2; 
	int count = 0;
	for(vector<int>::iterator it = v4.begin(); it != v4.end(); it++){
		if(count % 5 == 0)	cout << endl;
		cout << *it << " ";
		count++;
	}


	return 0;

}