// 练习：输入一个n，打印n阶菱形。n是奇数。

#include<iostream>
using namespace std;

int main(){
    int n;
    cin >> n;   //输入n为奇数

    int cx = n / 2, cy = n / 2;

    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if(abs(i - cx) + abs(j - cy) <= n / 2){
                cout << "*";
            }else{
                cout << " ";
            }
        }
        cout << endl;
    }

    return 0;
}