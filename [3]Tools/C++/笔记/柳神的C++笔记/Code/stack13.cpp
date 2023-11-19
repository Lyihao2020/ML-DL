#include<iostream>
#include<stack>
#include<string>
using namespace std;

int main(){

	stack<int> s;	//定义一个空栈
	for (int i = 0; i < 6; ++i)
	{
		s.push(i);
	}

	cout << s.top() << endl;
	s.pop();
	cout << s.top() << endl;
	cout << s.size() << endl;

	return 0;

}