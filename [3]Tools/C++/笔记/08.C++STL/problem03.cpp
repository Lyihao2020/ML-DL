/*
32. 调整数组顺序使奇数位于偶数前面

输入一个整数数组，实现一个函数来调整该数组中数字的顺序。

使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分。

数据范围
数组长度 [0,100]。
数组内元素取值范围 [0,100]。

样例
输入：[1,2,3,4,5]

输出: [1,3,5,2,4]
*/

#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    void reOrderArray(vector<int> &array) {
        int l = 0, r = array.size() - 1;
        while(l < r){
            while(l < r && array[r] % 2 == 0) r--;
            while(l < r && array[l] % 2 == 1) l++;
            if(l != r) swap(array[l], array[r]);
        }
    }
};
/*
bool cmp(const int &a,const int &b){
    return (a&1)==(b&1)?0:(a&1);
}
class Solution {
public:
    void reOrderArray(vector<int> &array) {
         sort(array.begin(),array.end(),cmp);
    }
};
*/
/*
算法
(双指针扫描) O(n)O(n)
用两个指针分别从首尾开始，往中间扫描。扫描时保证第一个指针前面的数都是奇数，第二个指针后面的数都是偶数。

每次迭代时需要进行的操作：

第一个指针一直往后走，直到遇到第一个偶数为止；
第二个指针一直往前走，直到遇到第一个奇数为止；
交换两个指针指向的位置上的数，再进入下一层迭代，直到两个指针相遇为止；
时间复杂度
当两个指针相遇时，走过的总路程长度是 nn，所以时间复杂度是 O(n)O(n)。

C++ 代码
class Solution {
public:
    void reOrderArray(vector<int> &array) {
         int l = 0, r = array.size() - 1;
         while (l < r) {
             while (l < r && array[l] % 2 == 1) l ++ ;
             while (l < r && array[r] % 2 == 0) r -- ;
             if (l < r) swap(array[l], array[r]);
         }
    }
};

*/