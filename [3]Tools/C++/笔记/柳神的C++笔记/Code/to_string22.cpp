#include<string>
#include<iostream>
using namespace std;

int main(){

	string s1 = to_string(123);
	cout << s1 << endl;
	string s2 = to_string(4.5);
	cout << s2 << endl;
	cout << s1 + s2 << endl;
	cout << s1 + s1 << endl;	//将两个字符串拼接起来输出
	printf("%s\n", (s1 + s2).c_str());	
	// 如果想⽤printf输出string，得加⼀个.c_str()
	return 0;

}