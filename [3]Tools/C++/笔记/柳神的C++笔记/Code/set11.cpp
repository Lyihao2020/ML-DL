#include<iostream>
#include<cstdio>
#include<set>
using namespace std;

int main(){

	set<int> s;	//定义一个空集合s
	s.insert(1);	//向集合中插入一个1
	cout << *(s.begin()) << endl;	//输出集合s的第一个元素（前面的星号表示要对指针取值）
	for (int i = 0; i < 6; ++i)
	{
		s.insert(i);
	}

	cout << s.size() << endl;
	//用迭代器便利集合s里面的每一个元素
	for(auto it =s.begin(); it != s.end(); it++){
		cout << *it << " ";
	}
	cout << endl;

	cout << (s.find(2) != s.end()) << endl;
	cout << (s.find(10) != s.end()) << endl;
	cout << (s.find(-1) != s.end()) << endl;

	s.erase(1);	//删除集合s中1这个元素
	cout << (s.find(1) != s.end()) << endl;	//此时应该输出false

	return 0;

}