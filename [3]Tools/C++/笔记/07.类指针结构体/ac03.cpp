#include<iostream>
using namespace std;

int main(){
	int a = 10;
	int *p = &a;
	*p += 5;
	cout << *p << endl;
	
	return 0;
	
} 
