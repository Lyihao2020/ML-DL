/*

68. 0到n-1中缺失的数字

一个长度为 n−1 的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围 0 到 n−1 之内。

在范围 0 到 n−1 的 n 个数字中有且只有一个数字不在该数组中，请找出这个数字。

数据范围
1≤n≤1000
样例
输入：[0,1,2,4]

输出：3

*/

#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int getMissingNumber(vector<int>& nums) {
        int cnt = 0;
        vector<int>::iterator it = nums.begin();
        for(; it != nums.end(); it++){
            if(*it != cnt)    return cnt;
            cnt++;
        }
        return cnt;
    }
};

/*
算法
(二分) O(logn)O(logn)
这道题目给定的是递增数组，假设数组中第一个缺失的数是 xx，那么数组中的数如下所示；


从中可以看出，数组左边蓝色部分都满足nums[i] == i，数组右边橙色部分都不满足nums[i] == i，因此我们可以二分出分界点 xx 的值。

另外要注意特殊情况：当所有数都满足nums[i] == i时，表示缺失的是 nn。

时间复杂度分析
二分中的迭代只会执行 O(logn)O(logn) 次，因此时间复杂度是 O(logn)O(logn)。

C++ 代码
class Solution {
public:
    int getMissingNumber(vector<int>& nums) {
        if (nums.empty()) return 0;

        int l = 0, r = nums.size() - 1;
        while (l < r)
        {
            int mid = l + r >> 1;
            if (nums[mid] != mid) r = mid;
            else l = mid + 1;
        }

        if (nums[r] == r) r ++ ;
        return r;
    }
};
--------------------------------------------------------
class Solution {
public:
    int getMissingNumber(vector<int>& nums) {
        int cnt = 0;
        for(int x : nums)
        {
            if(x == cnt) cnt++;
        }
        return cnt;
    }
};
--------------------------------------------------------
class Solution {
public:
    int getMissingNumber(vector<int>& nums) {
        int l=0,r=nums.size();
        while(l<r){
            int m=(l+r)>>1;
            if(nums[m]==m) l=m+1;
            else r=m;
        }
        return l;
    }
};
*/