#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

bool cmp(int a, int b){
	return a > b;
}

void printVector(vector<int>& v){

	for(vector<int>::iterator it = v.begin(); it != v.end(); it++){
		cout << *it << " ";
	}
	cout << endl;

}

/*
在 printArray() 函数中，数组应该被声明为 int[] 而不是 int&。
在 C++ 中，数组名本身就是一个指向第一个元素的指针，
因此将数组传递给函数时，无需使用引用。
void printArray(int& arr){
*/
void printArray(int arr[], int len){
	//在 printArray() 函数中，应该使用 arr[i] 来访问数组元素，而不是 arr(i)。
	//void printArray(int[] arr, int len){	错误

	for (int i = 0; i < len; ++i)
	{
		cout << arr[i] << " ";
	}
	cout << endl;

}

int main(){
	/*
	1.在 vector 的初始化中，创建了一个大小为 10 的 vector，
	然后又使用 push_back() 方法插入了 10 个数值，
	导致实际上 vector 大小为 20，其中前 10 个元素的值是未定义的。
	vector<int> v(10);*/
	vector<int> v;
	for (int i = 0; i < 10; ++i)
	{
		v.push_back(10 - i);
	}
	//注意：sort函数的cmp必须按照规定来写，即必须只是 > 或者 <
	sort(v.begin(), v.end());
	printVector(v);

	int arr[10];
	for (int i = 0; i < 10; ++i)
	{
		arr[i] = i;
	}
	int len = sizeof(arr) / sizeof(arr[0]);
	/*
	在 main() 函数中，vector 的排序使用了默认的排序算法，
	而对于基本类型（如 int）的降序排序，可以使用 greater<int>() 函数对象来代替
	sort(arr, arr + 10, cmp);
	*/
	sort(arr, arr + len, greater<int>());
	printArray(arr, len);

	return 0;

}