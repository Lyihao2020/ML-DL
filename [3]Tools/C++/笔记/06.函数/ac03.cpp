/*

return 语句终止当前正在执行的函数并将控制权返回到调用该函数的地方。return语句有两种形式：
return;
return expression;

3.1	无返回值函数
没有返回值的return语句只能用在返回类型是void的函数中。返回void的函数不要求非得有return语句，因为在这类函数的最后一句后面会隐式地执行return。
通常情况下，void函数如果想在它的中间位置提前退出，可以使用return语句。return的这种用法有点类似于我们用break语句退出循环。
		void swap(int &v1, int &v2)
{
    // 如果两个值相等，则不需要交换，直接退出
    if (v1 == v2)
        return;
    // 如果程序执行到了这里，说明还需要继续完成某些功能
    
    int tmp = v2;
    v2 = v1;
    v1 = tmp;
    // 此处无须显示的return语句
}

3.2 函数递归

*/

#include<iostream>
using namespace std;

int fact(int n){
    if(n == 1 || n == 0){
        return 1;
    }else{
        return n * fact(n - 1);
    }
}
int main(){
    int n;
    cin >> n;

    cout << fact(n) << endl;

    return 0;
    
}