#include<iostream>
#include<string>
using namespace std;

/*
stof (string to float)
stold (string to long double)
stol (string to long)
stoll (string to long long)
stoul (string to unsigned long)
stoull (string to unsigned long long)
*/

int main(){

	//使用stoi(string to int)、stod(string to double)
	//可以将字符串string转化为对应的int型、double型变量
	string s;
	cin >> s;
	int a = stoi(s);
	cout << "(int)a = " << a << endl;
	cin >> s;
	double b = stod(s);
	cout << "(double)b = " << b << endl;
	//stoi如果遇到的是非法输⼊（⽐如stoi(“123.4”)，123.4不是⼀个int型变量）：
	//会自动截取最前面的数字，直到遇到不是数字为止
	//(所以说如果是浮点型，会截取前⾯的整数部分)
	//如果最前面不是数字，会运行时发⽣错误

	//stod如果遇到的是非法输⼊：
	//会⾃动截取最前面的浮点数，直到遇到不满足浮点数为止
	//如果最前面不是数字或者小数点，会运行时发⽣错误
	//如果最前面是小数点，会自动转化后在前⾯补0
	return 0;

}