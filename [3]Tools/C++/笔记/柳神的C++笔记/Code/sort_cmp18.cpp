#include<iostream>
#include<algorithm>
using namespace std;

struct stu {
    int score;
    int number;
} arr[2] = {{97, 12}, {97, 1}};

bool cmp(stu a, stu b){
	if(a.score != b.score){	// 如果学⽣分数不同，就按照分数从⼤到⼩排列
		return a.score > b.score;
	}else{	// 如果学⽣分数相同，就按照学号从⼩到⼤排列
		return a.number < b.number;
	}
}

/*
bool cmp(stu a, stu b){
	return (a.score != b.score)? a.score > b.score : a.number < b.number;
}
*/

int main(){

	/*
	在调用 sort 函数时，应该传入数组名，而不是类型名。
	可以将 stu 改为一个数组，比如 stu arr[2] = {{97, 12}, {97, 1}}，
	然后使用 sort(arr, arr + 2, cmp) 进行排序。
	stu a = {97, 12};
	stu b = {97, 1};
	*/
	//在调用 sort 函数时，应该传入 cmp 函数名，而不是 cmp()，因为 cmp 是一个函数指针
	sort(arr, arr + 2, cmp);

	for (int i = 0; i < 2; ++i)
	{
		cout << arr[i].score << " " << arr[i].number << endl;
	}

	return 0;

}