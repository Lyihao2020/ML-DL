#include<iostream>
#include<cstdio>
#include<cstdlib>
using namespace std;

// 传⼊的是n的引⽤，相当于直接对n进⾏了操作，只不过在func函数中换了个名字叫a
void func(int &a){
	//这个引⽤符号&要和C语⾔⾥⾯的取地址运算符&区分开来，他们没有什么关系
	//C++里面的引⽤是指在变量名之前加⼀个&符号，⽐如在函数传⼊的参数中int &a，
	//那么对这个引⽤变量a做的所有操作都是直接对传入的原变量进⾏的操作，
	//并没有像原来int a⼀样只是拷⻉⼀个副本（传值
	a = 99;
}

// 传⼊的是0这个值，并不会改变main函数中的n
void func1(int a){
	a = 99;
}

int main(){

	struct stu{
		int grade;
		float score;
	};

	int n = 0;
	struct stu arr1[10];	//C语言里面需要写struct
	stu arr2[10];	//C++里面不用写
	func(n);	// n由0变成了99

	cout << n;

	return 0;

}