// 求斐波那契数列的第n项。f(1)=1, f(2)=1, f(3)=2, f(n)=f(n-1) + f(n-2)

#include<iostream>
using namespace std;
/*
int main(){
    int n;
    cin >> n;

    int a = 1, b = 1, i = 1;
    while(i < n){
        int c = a + b;
        a = b;
        b = c;
        i++;
    }

    cout << a << endl;

    return 0;
}
*/

int main(){
    int n;
    cin >> n;

    int a = 1, b = 1;
    for(int i = 1; i < n; i++){
        int c = a + b;
        a = b;
        b = c;
    }

    cout << a;

    return 0;
}