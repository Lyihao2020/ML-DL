// Acwing 716. 最大数和它的位置
/*
给定 100 个整数，请你找出其中最大的数字，以及它的输入位置（位置从 1 开始）。

输入格式
共 100 行，每行包含一个整数。

输出格式
第一行输出最大的数字。

第二行输出该数字的输入位置。

数据范围
1≤输入数字≤50000,
保证输入数字互不相同。

输入样例：
22229
48558
24992
4755
11923
...
20213
输出样例：
48558
2
*/

#include<iostream>
using namespace std;

int main(){
    int max = 0, flag = 0, ans;

    for(int i = 0; i < 100; i++){
        cin >> ans;
        if(ans > max){
            max = ans;
            flag = i + 1;
        } 
    }

    cout << max << endl << flag;

    return 0;
}