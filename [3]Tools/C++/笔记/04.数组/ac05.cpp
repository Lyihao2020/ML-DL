// 计算2的N次方。N <= 10000
// 使用高精度算法
#include<iostream>
#include<algorithm>
using namespace std;

/*
`memset` 是 C/C++ 语言中的一个函数，用于将一段内存空间的值设置为指定的字符或整数。它的函数原型如下：

void *memset(void *s, int c, size_t n);

其中，`s` 是要设置的目标内存空间的起始地址，`c` 是要设置的值，`n` 是要设置的字节数。

例如，以下代码将数组 `arr` 中的所有元素设置为 0：

int arr[10];
memset(arr, 0, sizeof(arr));

在上面的例子中，`arr` 是要设置的目标内存空间的起始地址，0 是要设置的值，`sizeof(arr)` 表示要设置的字节数（即数组的大小）。

需要注意的是，`memset` 并不会自动检测目标内存空间的边界，如果超出了目标内存空间的范围，可能会导致程序崩溃或其他异常情况。因此，在使用 `memset` 的时候，需要确保目标内存空间的大小和起始地址都是正确的。
*/

int main(){

    int a[10000], size = 1, n;
    a[0] = 1;
    cin >> n;

    while(n--){
        int t = 0;
        for(int i = 0; i < size; i++)
        {
            t += a[i] * 2;
            a[i] = t % 10;
            t /= 10;
        }
        if(t) a[size++] = t;
    }

    for(int i = size - 1; i >= 0; i--)  cout << a[i] << " ";
    cout << endl;

    return 0;
}