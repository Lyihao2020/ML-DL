/*
67. 数字在排序数组中出现的次数

统计一个数字在排序数组中出现的次数。

例如输入排序数组 [1,2,3,3,3,3,4,5] 和数字 3，由于 3 在这个数组中出现了 4 次，因此输出 4。

数据范围
数组长度 [0,1000]。

样例
输入：[1, 2, 3, 3, 3, 3, 4, 5] ,  3

输出：4
*/

#include<vector>
#include<iostream>
using namespace std;

class Solution {
public:
    int getNumberOfK(vector<int>& nums , int k) {
        int cnt = 0;
        for(vector<int>::iterator it = nums.begin(); it != nums.end(); it++){
            if(*it == k)    cnt++;
        }
        return cnt;
    }
};

/*
0:
int num = count(nums.begin(), nums.end(), k);

题解一：使用有序多重集合multiset
class Solution {
public:
    int getNumberOfK(vector<int>& nums , int k) {
        multiset<int> s;

        for(int x : nums) s.insert(x);

        return s.count(k);
    }
};
题解二：遍历vector，计数
class Solution {
public:
    int getNumberOfK(vector<int>& nums , int k) {
        int cnt = 0;
        for(int x : nums)
            if(x == k)
                cnt++;
        return cnt;
    }
};
题解三：使用lower_bound和upper_bound,指针运算得出次数
class Solution {
public:
    int getNumberOfK(vector<int>& nums , int k) {

        auto l = lower_bound(nums.begin(), nums.end(), k);  
        //在排好序的数组中，利用二分搜索找到指向满足nums >= k的nums的最小指针
        auto r = upper_bound(nums.begin(), nums.end(), k);
        //在排好序的数组中，利用二分搜索找到指向满足nums > k的nums的最小指针
        return r - l;
    }
};

*/

