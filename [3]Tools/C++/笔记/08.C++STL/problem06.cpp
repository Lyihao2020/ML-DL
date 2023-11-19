/*

53. 最小的k个数

输入 n 个整数，找出其中最小的 k 个数。

注意：

输出数组内元素请按从小到大顺序排序;
数据范围
1≤k≤n≤1000
样例
输入：[1,2,3,4,5,6,7,8] , k=4

输出：[1,2,3,4]

*/

#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

class Solution {
public:
    vector<int> getLeastNumbers_Solution(vector<int> input, int k) {
        vector<int> vec;
        sort(input.begin(), input.end());
        for(int i = 0; i < k; i++)  vec.push_back(input[i]);
        return vec;
    }
};

/*
class Solution {
public:
    vector<int> getLeastNumbers_Solution(vector<int> input, int k) {
        sort(input.begin(),input.end());
        input.erase(input.begin() + k,input.end());
        return input;
    }
};
*/

/*
算法1
(快速选择) O(klogn)O(klogn)
运用快速排序的思想，每次快速选择会将一个数放置到正确的位置（即满足左边的数都比它小，右边的数都比它大），因此我们可以对原数组做k次快速选择。

时间复杂度分析：一次快速选择的时间复杂度是O(logn)O(logn)，进行k次，时间复杂度为O(klogn)O(klogn)
C++ 代码
class Solution {
public:
    vector<int> getLeastNumbers_Solution(vector<int> input, int k) {
        vector<int> res;
        for(int i = 1;i <= k;i++)
            res.push_back(quick_select(input,0,input.size()-1,i));
        return res;
    }

    int quick_select(vector<int>& q,int l,int r,int k)
    {
        if(l >= r) return q[l];
        int i = l-1,j = r+1,x = q[l+r >> 1];
        while(i < j)
        {
            do i++;while(q[i] < x);
            do j--;while(q[j] > x);
            if(i < j) swap(q[i],q[j]);
        }
        if(k <= j-l+1) return quick_select(q,l,j,k);
        else return quick_select(q,j+1,r,k-(j-l+1));
    }

};
算法2
(堆排序) O(nlogk)O(nlogk)
维护一个大小为k的大根堆，将数组元素都push进堆，当堆中的数大于k时弹出堆顶元素。注意弹出堆顶的顺序是从大到小的k个数，要进行逆序操作

时间复杂度分析：建堆的时间复杂度是O(logk)O(logk)，要进行n次建堆的操作。

C++ 代码
class Solution {
public:
    vector<int> getLeastNumbers_Solution(vector<int> input, int k) {
        vector<int> res;
        priority_queue<int> heap;
        for(auto x : input)
        {
            heap.push(x);
            if(heap.size() > k) heap.pop(); 
        }
        while(heap.size())
        {
            res.push_back(heap.top());
            heap.pop();
        }
        reverse(res.begin(),res.end());
        return res;
    }
};

算法3:
class Solution {
public:
    vector<int> getLeastNumbers(vector<int>& input, int k) {
        vector<int> res(k, 0);
        quick_select(input, 0, input.size() - 1, k - 1);
        for(int i = 0; i < k; ++i) //用++i更快
        {
            res[i] = input[i];
        }
        return res;
    }

    void quick_select(vector<int>& q, int l, int r, int k)
    {
        if(l >= r) return k; 
        int i = l - 1, j = r + 1, x = q[(l + r) >> 1];
        while(i < j)
        {
            do i++; while(q[i] < x);
            do j--; while(q[j] > x);
            if(i < j) swap(q[i], q[j]);
        }
        if(k <= j) quick_select(q, l, j, k);
        else quick_select(q, j + 1, r, k);
    }

};
*/