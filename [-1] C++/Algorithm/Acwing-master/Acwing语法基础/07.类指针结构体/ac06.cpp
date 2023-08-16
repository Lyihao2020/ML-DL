#include<iostream>
#include<cstring>
using namespace std;

const int N = 10000;

struct Node
{
	int val;
	Node *next; 
}*head;

int main() 
{
	for(int i = 1; i <= 5; i++)
	{
		Node *p = new Node();
		p->val = i;
		p->next = head;
		head = p;
	}
	
	for(Node *p = head; p; p = p->next)	cout << p->val << " ";
	cout << endl;
	
	return 0;
}
