/*
75. 和为S的两个数字

输入一个数组和一个数字 s，在数组中查找两个数，使得它们的和正好是 s。

如果有多对数字的和等于 s，输出任意一对即可。

你可以认为每组输入中都至少含有一组满足条件的输出。

数据范围
数组长度 [1,1002]。

样例
输入：[1,2,3,4] , sum=7

输出：[3,4]

*/
#include<iostream>
#include<vector>
#include<set>
#include<algorithm>
using namespace std;

class Solution {
public:
    vector<int> findNumbersWithSum(vector<int>& nums, int target) {
        set<int> s;
        for(int x: nums) s.insert(x);
        for(int i = 0; i < nums.size(); i++){
            if(s.find(target - nums[i]) != s.end()){
                int x = nums[i], y = target - nums[i];
                // if (x != y) return {x, y};
            }
        }
        // return {};
    }
};

/*
class Solution {
public:
    vector<int> findNumbersWithSum(vector<int>& nums, int target) {
        unordered_map<int, int> cnt;
        for (int x : nums) cnt[x]++;
        for (int x : nums) {
            cnt[x]--;
            if (cnt[target - x] > 0) return {x, target - x};
        }
        return {};
    }
};
*/

/*
暴力解法
此题最先想到的是暴力解法。
穷举出每一种情况，如果两数之和等于target的，输出答案。

1. i指向数对的第一个数字，从0到nums.size() - 2;
2. j指向数对的第二个数字，从nums.size() - 1到i+1;
3. 如果nums[i] + nums[j] == target, 返回[nums[i], nums[j]]。

代码：

class Solution {
public:
    vector<int> findNumbersWithSum(vector<int>& nums, int target) 
    {
        for(int i = 0; i < nums.size() - 1; i++)//i指向数对的第一个数字，从0到nums.size()-2
        {
            for(int j = nums.size() - 1; j > i; j--)//j指向数对的第二个数字，从nums.size()-1到i+1
            {

                if(nums[i] + nums[j] == target)//如果两数之和等于target
                    return vector<int>{nums[i], nums[j]};//返回数对
            }
        }
        return vector<int>{-1, -1};//穷举完没有答案，返回[-1,-1]
    }
};
两个遍历数组的循环，所以时间复杂度是O(n^2)；没有开辟与数组大小相关的空间，所以空间复杂度是O(1)

哈希表：对于数x,目的是找到target - x
暴力法的时间复杂度较高的原因是寻找 target - x 的时间复杂度过高。需要一种更优秀的方法，能够快速寻找数组中是否存在目标元素。如果存在，[x, target - x] 即为答案。

使用哈希表，可以将寻找 target - x 的时间复杂度降低到从O(N) 降低到 O(1)。

创建一个哈希表，对于每一个 x，我们首先查询哈希表中是否存在target - x，如果有返回[x, target - x]。如果没有，将 x 插入到哈希表中。

//cpp
class Solution {
public:
    vector<int> findNumbersWithSum(vector<int>& nums, int target) 
    {
        unordered_map<int, int> hash;//创建哈希表
        for (int i = 0; i < nums.size(); ++i) {
            if(hash[target - nums[i]] == 0)//如果哈希表中没有target - nums[i]
                hash[nums[i]]++;//nums[i]出现次数加1
            else//如果哈希表中有target - nums[i]
                return {nums[i], target - nums[i]};//返回答案
        }
        return {};

    }
};
在i从0到nums.size() - 1过程总，j只遍历了一次，所以时间复杂度O(n)；开辟了数组大小的哈希表，所以空间复杂度是O(n)

*/

/*
class Solution{
public:
    vector<int> findNumbersWithSum(vector<int>& nums, int target) {
        unordered_map<int, int> hash;
        for (int i = 0; i < nums.size(); ++i)
        {
            if(hash[target - nums[i]] == 0)
                hash[nums[i]]++;
            else
                return {nums[i], target - nums[i]};
        }
        return {};

    }
};
*/
