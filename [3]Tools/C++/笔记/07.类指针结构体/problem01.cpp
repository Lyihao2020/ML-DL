
#include<iostream>
using namespace std;

class Solution {
public:
    int Fibonacci(int n) {
        if(n == 0){
        	return 0;
		}else if(n == 1 || n == 2){
			return 1; 
		}else{
			return Fibonacci(n - 1) + Fibonacci(n - 2);
		}
    }
}sl;

/*
class Solution {
public:
    int Fibonacci(int n) {
        int a = 0, b = 1;
        while (n -- ) {
            int c = a + b;
            a = b, b = c;
        }
        return a;
    }
};
*/

int main(){
	int n;
	cin >> n;
	
	cout << sl.Fibonacci(n) << endl;
	
	return 0;
}
