/*

在函数中对数组中的值的修改，会影响函数外面的数组。

一维数组形参的写法：
		// 尽管形式不同，但这三个print函数是等价的
		void print(int *a) { … }
		void print(int a[]) { … }
		void print(int a[10]) { … }

多维数组形参的写法：
		// 多维数组中，除了第一维之外，其余维度的大小必须指定
		void print(int (*a)[10]) { … }
		void print(int a[][10]) { … }

*/

#include<iostream>
using namespace std;

/*
void print(int a[]){
    for(int i = 0; i < 10; i++) cout << a[i] << endl;
}
*/

void print(int a[][10]){
    for(int i = 0; i < 10;i ++){
        for(int j = 0; j < 10; j++){
            cout << a[i][j] << " ";
        }
        cout << endl;
    }
}
int main(){

    int a[10][10];

    for(int i = 0; i < 10; i++){
        for(int j = 0; j < 10; j++){
            a[i][j] = j;
        }
    }

    print(a);

    return 0;

}
