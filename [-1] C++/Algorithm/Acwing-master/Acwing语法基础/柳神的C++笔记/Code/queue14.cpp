#include<iostream>
#include<queue>
#include<string>
using namespace std;

int main(){

	queue<int> q;
	for (int i = 0; i < 6; ++i)
	{
		q.push(i);
	}
	// 访问队列的队⾸元素和队尾元素
	cout << q.front() << " " << q.back() << endl;
	cout << q.size() << endl;
	q.pop();	//出队，移除队列的队首元素

	return 0;

}