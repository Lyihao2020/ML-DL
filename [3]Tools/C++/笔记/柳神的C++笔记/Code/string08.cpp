#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int main(){

	string s = "Hello C++"; //赋值C++
	string s1 = s;
	string s2 = s1 + s;
	string s3;
	cin >> s3;	//读入字符串
	cout << s << endl << s1 << endl << s2 << endl << s3;	//输出字符串

	string s4 = s3;	//定义一个空字符串
	//⽤cin读⼊字符串的时候，是以空格为分隔符的
	//getline(cin, s4);	//读取一行字符串，包括空格
	cout << endl << s4 << endl << s4.length();	//输出s4和s4的长度

	string s5 = s4.substr(4);	//表示从下标4到结束
	string s6 = s4.substr(4, 3); 	//表示从下标4开始，3个字符
	cout << endl << s5 << endl << s6;

	return 0;
}