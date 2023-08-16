/*
26. 二进制中1的个数

输入一个 32 位整数，输出该数二进制表示中 1 的个数。

注意：

负数在计算机中用其绝对值的补码来表示。
数据范围
−100≤ 输入整数 ≤100
样例1
输入：9
输出：2
解释：9的二进制表示是1001，一共有2个1。
样例2
输入：-2
输出：31
解释：-2在计算机里会被表示成11111111111111111111111111111110，
      一共有31个1。
*/

#include<iostream>
#include<bitset>
using namespace std;

class Solution {
public:
    int NumberOf1(int n) {
        bitset<32> binary(n);
        int ones_count = binary.count();
        return ones_count;
    }
};

/*
unsigned int count_set_bits(unsigned int num) {
    unsigned int count = 0;
    while (num > 0) {
        if (num & 1 == 1) {
            count++;
        }
        num >>= 1;
    }
    return count;
}
*/
/*
(位运算) O(logn)O(logn)
迭代进行如下两步，直到 nn 变成0为止：

如果 nn 在二进制表示下末尾是1，则在答案中加1；
将 nn 右移一位，也就是将 nn 在二进制表示下的最后一位删掉；
这里有个难点是如何处理负数。
在C++中如果我们右移一个负整数，系统会自动在最高位补1，这样会导致 n 永远不为0，就死循环了。
解决办法是把 n 强制转化成无符号整型，这样 n 的二进制表示不会发生改变，但在右移时系统会自动在最高位补0。

时间复杂度
每次会将 n 除以2，最多会除 logn 次，所以时间复杂度是 O(logn)。

C++ 代码
class Solution {
public:
    int NumberOf1(int n) {
        int res = 0;
        unsigned int un = n; 
        while (un) res += un & 1, un >>= 1;
        return res;
    }
};
*/
/*
int x=0;
for(int i=0,j=1;i<32;++i,j<<=1) x+=(bool)(j&n);
return x;
*/
/*
NO.1 循环（固定次数）
一个intint类型的变量有3232位，想要取出第ii位就是n >> i & 1，因为11的二进制是000…01000…01所以和任何数进行&运算结果都只可能是00或11。

代码：
class Solution {
public:
    int NumberOf1(int n) {
        int res = 0;
        for (int i = 0; i < 32; i ++)
            res += n >> i & 1;//如果n的第i位是1，则res+1；否则什么也不会发生
        return res;
    }
};
NO.2 循环（不固定次数）
在第一种方法的基础上，我们可以用while来做这道题，先看一眼代码：

class Solution {
public:
    int NumberOf1(int n) {
        unsigned int x = n;
        int res = 0;
        while (x) res += x & 1, x >>= 1;
        return res;
    }
};
这边有一个问题是，如果是负数的话，每次右移运算都会在左边补11，这会造成循环永远不终止，所以这边可以给它转成无符号整型，这就不会出现问题了。

NO.3 lowbitlowbit
先说一下lowbitlowbit是什么东西。

lowbit(x)lowbit(x)表示xx的最后一位11，比如1010的二进制表示是10101010，那lowbit(x)lowbit(x)就应该是(10)2(10)2也就是22。

那lowbit(x)lowbit(x)怎么求呢？

其实很简单，只要返回x&(-x)就行了。可又为什么呢？

是因为C++C++中的负数使用补码表示的，而补码等于反码（就是把xx的二进制中的每一位都取反）+1+1，所以x&(-x)=x&(~x+1)。

要证明x&(~x+1)的正确性，可以先看下图：


很明显，红色数字左边的原码与补码都是相反的，而红色数字右边的原码与补码都是00，所以最后只有红色数字一个11，故x&(-x)是成立的。

那么这道题可以让nn反复减去lowbit(n)lowbit(n)直到nn为00，减去的次数就是答案。

代码:
class Solution {
public:
    //返回x的lowbit值
    int lowbit(int x)
    {
        return x & (-x);
    }
    int NumberOf1(int n) {
        int res = 0;
        while (n)
        {
            n -= lowbit(n);//每次减去lowbit(n)
            res ++;
        }
        return res;
    }
};
*/