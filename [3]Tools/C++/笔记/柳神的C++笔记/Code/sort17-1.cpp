#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

void printVector(vector<int>& v){
    for (vector<int>::iterator it = v.begin(); it != v.end(); it++){
        cout << *it << " ";
    }
    cout << endl;
}

void printArray(int arr[], int len){
    for (int i = 0; i < len; ++i){
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main(){
    // 使用 vector 初始化列表来初始化 vector
    vector<int> v = {9, 8, 7, 6, 5, 4, 3, 2, 1, 0};
    sort(v.begin(), v.end(), greater<int>());
    printVector(v);

    // 使用数组初始化列表来初始化数组
    int arr[] = {9, 8, 7, 6, 5, 4, 3, 2, 1, 0};
    int len = sizeof(arr)/sizeof(arr[0]);
    sort(arr, arr + len, greater<int>());
    printArray(arr, len);

    return 0;
}
