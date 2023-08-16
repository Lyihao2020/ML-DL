#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<vector>
using namespace std;

void printVector(vector<int>& v){

	//auto == vector<int>::iterator
	for(auto it = v.begin(); it != v.end(); it++){
		cout << *it << " ";
	}
	cout << endl;

}

int main(){
	vector<int> a;	//定义的时候不指定a的大小
	cout << a.size() << endl;	// size =0
	for (int i = 0; i < 10; ++i)
	{
		a.push_back(i);	//在a的末尾添加元素i
	}
	cout << a.size() << endl;
	printVector(a);

	vector<int> b(15);	//定义的时候指定vector大小，元素默认为0
	cout << b.size() << endl;
	for (int i = 0; i < b.size(); ++i)
	{
		b[i] = 15;
	}
	printVector(b);

	vector<int> c(20, 2);
	printVector(c);

	return 0;

}