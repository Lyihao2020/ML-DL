#include<iostream>
#include<map>
#include<string>
using namespace std;

int main(){

	map<string,int> m;	//定义一个空的map m,键是string类型的,值是int类型的
	m["Hello"] = 2;	//将key为"hello", value为2的键值(key - value)存入map中
	cout << m["Hello"]	<< endl;	// 访问map中key为"hello"的value, 如果key不存在，则返回0
	cout << m["World"]	<< endl;
	m["World"] = 3;
	m[","] = 1;

	//用迭代器遍历，输出map中所有的元素，键：it->first获取，值：it->second获取
	for(auto it = m.begin(); it != m.end(); it++){
		cout << it->first << " " << it->second << endl;
	}

	//访问map的第一个元素
	cout << m.begin()->first << " " << m.begin()->second << endl;
	//访问map的最后一个元素
	//不是end!!!
	cout << m.rbegin()->first << " " << m.rbegin()->second << endl;

	//输出map中元素的个数
	cout << m.size() << endl;

	return 0;

}