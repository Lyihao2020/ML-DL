// 输入一个n，再输入n个整数。
// 将这个数组逆时针旋转k(k <= n)次，最后将结果输出。

#include<iostream>
#include<algorithm>
using namespace std;

/*

我们可以使用数学归纳法来证明这个结论。

当k=1时，假设原数组为a0, a1, ..., an-1，则顺时针旋转后得到的数组为an-1, a0, a1, ..., an-2。按照上述步骤进行操作，可以得到如下结果：

1. 将前n-1个元素逆序排列，得到a(n-2), a(n-3), ..., a1, a0；
2. 将后1个元素逆序排列，得到a(n-1)；
3. 将整个数组逆序排列，得到an-1, a0, a1, ..., a(n-3), a(n-2)。

可以发现，这个结果与顺时针旋转后得到的数组相同，因此对于k=1时，结论成立。

假设对于任意的k（1<=k<=n），都有将前n-k个元素逆序排列、将后k个元素逆序排列和将整个数组逆序排列三步操作可以得到正确的结果。那么对于k+1，我们需要将前n-(k+1)个元素逆序排列，将后(k+1)个元素逆序排列，以及将整个数组逆序排列。具体来说，可以先将前n-k个元素逆序排列，再将后1个元素逆序排列，接着将前n-(k+1)个元素逆序排列，最后将整个数组逆序排列。这样一来，就可以得到正确的结果。

因此，根据数学归纳法，对于任意的1<=k<=n，将前n-k个元素逆序排列、将后k个元素逆序排列和将整个数组逆序排列三步操作可以得到正确的顺时针旋转k次后的结果。

*/

int main(){

    int n, k;
    int a[100];

    cin >> n >> k;
    for(int i = 0; i < n; i++)  cin >> a[i];

    /*
    数组的旋转是指将数组中的元素按照一定规则进行移动。常见的有两种方式：

    顺时针旋转：将数组中的元素向右移动k个位置，即将最后k个元素移到数组的前面。

    逆时针旋转：将数组中的元素向左移动k个位置，即将前k个元素移到数组的后面。

    在这个代码中，数组的旋转是通过三次reverse()实现的。这里简单解释一下reverse()函数的用法：

    reverse(begin, end)：该函数可以将序列从begin到end之间的元素按照相反的顺序重新排列。

    具体实现上，我们可以先将前k个元素进行翻转，再将后面n-k个元素进行翻转，最后再将整个序列再次进行翻转。这样就能够实现顺时针旋转k次的效果。

    举个例子：假设原始序列为1 2 3 4 5，要求将其顺时针旋转2次，即将序列变为4 5 1 2 3。那么可以先将前两个元素进行翻转，得到2 1 3 4 5，
    
    然后将剩下的三个元素进行翻转，得到2 1 5 4 3，最后将整个序列再次进行翻转，得到3 4 5 1 2，即为所求的结果。
    */

    reverse(a, a + k);
    reverse(a + k, a + n);
    reverse(a, a + n);

    for(int i = 0; i < n; i++)  cout << a[i] << " ";

    return 0;
}

/* 顺时针旋转代码
#include <iostream>
#include <algorithm>
using namespace std;

const int MAXN = 100005;
int a[MAXN];

int main() {
    int n, k;
    cin >> n; // 输入n
    for (int i = 0; i < n; i++) {
        cin >> a[i]; // 输入n个整数
    }
    cin >> k; // 输入k

    reverse(a, a + n - k);     // 翻转数组的前n-k个元素
    reverse(a + n - k, a + n); // 翻转数组的后k个元素
    reverse(a, a + n);         // 翻转整个数组

    // 输出结果
    for (int i = 0; i < n; i++) {
        cout << a[i] << " ";
    }
    cout << endl;

    return 0;
}
*/

/* 不使用reverse()
#include <iostream>
using namespace std;

const int MAXN = 100005;
int a[MAXN];

int main() {
    int n, k;
    cin >> n; // 输入n
    for (int i = 0; i < n; i++) {
        cin >> a[i]; // 输入n个整数
    }
    cin >> k; // 输入k

    // 将前n-k个元素逆序排列
    for (int i = 0, j = n - k - 1; i < j; i++, j--) {
        swap(a[i], a[j]);
    }

    // 将后k个元素逆序排列
    for (int i = n - k, j = n - 1; i < j; i++, j--) {
        swap(a[i], a[j]);
    }

    // 将整个数组逆序排列
    for (int i = 0, j = n - 1; i < j; i++, j--) {
        swap(a[i], a[j]);
    }

    // 输出结果
    for (int i = 0; i < n; i++) {
        cout << a[i] << " ";
    }
    cout << endl;

    return 0;
}
*/