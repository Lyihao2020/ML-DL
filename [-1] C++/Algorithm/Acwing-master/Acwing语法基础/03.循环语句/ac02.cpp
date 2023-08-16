// init-statement可以定义多个变量，expression也可以修改多个变量。
// 例如求 1 * 10 + 2 * 8 + 3 * 7 + 4 * 6：

#include<iostream>
using namespace std;

int main(){
    int sum = 10;

    for(int i = 2, j = 8; i <= 4; i++, j--){
        sum += i * j;

    }

    cout << sum;

    return 0;
}
