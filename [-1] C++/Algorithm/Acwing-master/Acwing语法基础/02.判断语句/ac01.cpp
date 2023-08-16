/*
简单计算器输入两个数，以及一个运算符+, -, *, /，输出这两个数运算后的结果。
当运算符是/，且除数是0时，输出”Divided by zero!”; 
当输入的字符不是+, -, *, /时，输出”Invalid operator!”。

*/
#include<iostream>
using namespace std;

int main(){
    double a, b;
    char c;
    cin >> a >> b >> c;

    if(c == '+'){
        cout << a + b << endl;
    }else if(c == '-'){
        cout << a - b << endl;
    }else if(c == '*'){
        cout << a * b << endl;
    }else if(c == '/'){
        if(b == 0){
            cout << "Divided by zero!" << endl;
        }else{
            cout << a / b << endl;
        }
    }else{
        cout << "Invalid operator!" << endl;
    }

    return 0;

}