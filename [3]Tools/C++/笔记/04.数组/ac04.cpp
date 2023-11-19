// 输入n个数，将这n个数按从小到大的顺序输出
#include<iostream>
#include<algorithm>
using namespace std;

int main(){

    int n, k;
    int a[100];

    cin >> n;
    for(int i = 0; i < n; i++)  cin >> a[i];

    for(int i = 0; i < n; i++)
        for(int j = 0; j < n - i - 1; j++)
            if(a[j] < a[j + 1])
                swap(a[j], a[j + 1]);
    
    for(int i = 0; i < n; i++)  cout << a[i] << " ";

    return 0;
}