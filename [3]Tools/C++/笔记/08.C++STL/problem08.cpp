/*
51. 数字排列
输入一组数字（可能包含重复数字），输出其所有的排列方式。

数据范围
输入数组长度 [0,6]。

样例
输入：[1,2,3]

输出：
      [
        [1,2,3],
        [1,3,2],
        [2,1,3],
        [2,3,1],
        [3,1,2],
        [3,2,1]
      ]
*/

#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

/*
class Solution {
public:
    vector<vector<int>> permutation(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> path;
        vector<bool> used(nums.size(), false);
        // 对输入数组进行排序，方便后面去重
        sort(nums.begin(), nums.end());
        dfs(nums, path, used, res);
        return res;
    }
    
private:
    void dfs(const vector<int>& nums, vector<int>& path, vector<bool>& used, vector<vector<int>>& res) {
        if (path.size() == nums.size()) { // 找到一个排列
            res.push_back(path);
            return;
        }
        for (auto i = 0; i < nums.size(); i++) {
            if (used[i]) continue; // 如果该数字已经被使用，则跳过
            if (i > 0 && nums[i] == nums[i-1] && !used[i-1]) continue; // 对于重复的数字，只选择第一个未使用过的数字
            used[i] = true;
            path.push_back(nums[i]);
            dfs(nums, path, used, res);
            path.pop_back();
            used[i] = false;
        }
    }
};
*/

/*
int main() {
    Solution s;
    vector<int> nums = {1, 1, 2};
    vector<vector<int>> res = s.permutation(nums);
    for (const auto& r : res) {
        for (int i : r) {
            cout << i << " ";
        }
        cout << endl;
    }
    return 0;
}
*/

/*
算法1
(回溯) O(n!)O(n!)
由于有重复元素的存在，这道题的枚举顺序和 Permutations 不同。

先将所有数从小到大排序，这样相同的数会排在一起；
从左到右依次枚举每个数，每次将它放在一个空位上；
对于相同数，我们人为定序，就可以避免重复计算：我们在dfs时记录一个额外的状态，记录上一个相同数存放的位置 start，我们在枚举当前数时，只枚举 start+1,start+2,…,nstart+1,start+2,…,n 这些位置。
不要忘记递归前和回溯时，对状态进行更新。
时间复杂度分析：搜索树中最后一层共 n! 个节点，前面所有层加一块的节点数量相比于最后一层节点数是无穷小量，可以忽略。且最后一层节点记录方案的计算量是O(n)O(n)，所以总时间复杂度是 O(n×n!)O(n×n!)。

C++ 代码
class Solution {
public:
    vector<bool> st;
    vector<int> path;
    vector<vector<int>> ans;

    vector<vector<int>> permutation(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        st = vector<bool>(nums.size(), false);
        path = vector<int>(nums.size());
        dfs(nums, 0, 0);
        return ans;
    }

    void dfs(vector<int>& nums, int u, int start)
    {
        if (u == nums.size())
        {
            ans.push_back(path);
            return;
        }

        for (int i = start; i < nums.size(); i ++ )
            if (!st[i])
            {
                st[i] = true;
                path[i] = nums[u];
                if (u + 1 < nums.size() && nums[u + 1] != nums[u])
                    dfs(nums, u + 1, 0);
                else
                    dfs(nums, u + 1, i + 1);
                st[i] = false;
            }
    }

};
*/

/*
class Solution {
public:
    vector<vector<int>> permutation(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        vector<vector<int>> ret;
        do{
            ret.push_back(nums);
        }while(next_permutation(nums.begin(),nums.end()));
        return ret;
    }
};
*/

/*
C++代码

class Solution {
public:
    vector<int> path;  //记录每一个坑放的数
    vector<vector<int>> ans;
    vector<bool> st;   //记录每一个数是否被用过
    vector<vector<int>> permutation(vector<int>& nums) {
        st = vector <bool>(nums.size(), false);
        path = vector<int>(nums.size());
        dfs(nums, 0);
        return ans;
    }
    void dfs(vector<int>& nums, int u)  //递归的深度,初始为第0层
    {
        if(u == nums.size())
        {
            ans.push_back(path);
            return ;
        }
        //枚举每一个可以用的数
        for(int i = 0; i < nums.size(); i ++)
        {
            if(!st[i])
            {
                st[i] = true;
                path[u] = nums[i];
                dfs(nums, u + 1);
                st[i] = false;
                //path[u] = 0;

            }
        }
    }
};
从中我们可以看到
1. 我们事先挖好了坑,将数放入.
2. 我们需要设置判重数组，递归的过程每次都对每个数进行枚举，找到未被用过的数，即每个坑在选不同的数

相同的题

题目描述

把 1∼n 这 n 个整数排成一行后随机打乱顺序，输出所有可能的次序。

C++代码

#include <bits/stdc++.h>
using namespace std;
const int N = 15;
bool st[N];
int a[N];
int n;
void dfs(int u)
{
    if(u > n)
    {
        for(int i = 1; i <= n; i ++)
        {
            printf("%d ", a[i]);
        }
        puts("");
        return ;
    }
    for(int i = 1; i <= n; i ++)
    {
        if(!st[i])
        {
            st[i] = true;
            a[u] = i;
            dfs(u + 1);
            st[i] = false;
        }
    }
}
int main()
{
    cin >> n;
    dfs(1);
    return 0;
}
二、Permutations II
题目描述

给定一堆整数，可能包含相同数，返回其所有不同的全排列。
与之前不同的在于 排列中有相同的数

求解思路
先将所有数从小到大排序(特别重要)，这样相同的数会排在一起,用sort()函数即可实现
我们对数无需判重,取而代之的是,枚举数的顺序是从前往后的,这里可以结合递归的层数的顺序实现，即数在选坑。
从左到右依次枚举每个数，每次将它放在一个空位上
为什么要做出如上的变化,是因为我们要人为的规定数选坑的规则。
因此我们要对每一个坑都开一个判重数组，是否被用过？
那么规则的制定是怎么样的呢？
我们在dfs时记录一个额外的状态，记录上一个相同数存放的位置 start，我们在枚举当前数时，只能枚举 start+1,start+2,…,nstart+1,start+2,…,n这些位置,在上一个数的后面，如果上一个数和当前数是不同的,那么当前数就可以从start = 0 开始选，选到没有被用过坑填入即可。

值得注意的是，我们在枚举数时要保证下一个数不能出界了,也就是说只能枚举到倒数第二个位置
即代码中的 u + 1 < nums.size()

那如果枚举到了最后一个数怎么办呢？此时所有的坑已经填完了所有的数,所以直接进入递归,然后return即可。
c++代码
class Solution {
public:
    vector<int> path;  //每一个坑填的数字是几
    vector<vector<int>> ans;
    vector<bool> st;  //每一个坑是否被用过
    vector<vector<int>> permutation(vector<int>& nums) {
        sort(nums.begin(), nums.end());  // 至关重要
        st = vector<bool>(nums.size(), false);
        path = vector<int>(nums.size());  //开出这么多坑
        dfs(nums, 0, 0);
        return ans;
    }
    //u->表示递归到第几个坑
    //start->从哪个坑开始填起
    void dfs(vector<int> & nums, int u, int start)
    {
        if(u == nums.size())
        {
            ans.push_back(path);
            return ;
        }
        for(int i = start; i < nums.size(); i ++)
        {
            if(!st[i])
            {
                st[i] = true;
                path[i] = nums[u];
                if(u + 1 < nums.size() && nums[u] == nums[u + 1])
                    dfs(nums, u + 1, i + 1);
                        // 二是，如果前后两个元素不相等
                else // 双重含义，一所有坑都被填满了,已经指向最后一个元素
                    dfs(nums, u + 1, 0);
                st[i] = false;  //还原现场
                //path[]无需还原，因为下一次会被覆盖，相当于还原。

            }
        }
    }
};
类似的题
问题描述

从 1∼n 这 n 个整数中随机选出 m 个，输出所有可能的选择方案。

c++ 代码
#include <bits/stdc++.h>
using namespace std;
const int N = 35;
int a[N];
int n, m;
void dfs(int u, int start)
{
    if(u > m)
    {
        for(int i = 1; i <= m; i ++)
        {
            printf("%d ", a[i]);
        }
        puts("");
        return ;
    }
    for(int i = start; i <= n; i ++)
    {
        a[u] = i;
        dfs(u + 1, i + 1);
    }
}
int main()
{
    cin >> n >> m;
    dfs(1, 1);
    return 0;
}
*/