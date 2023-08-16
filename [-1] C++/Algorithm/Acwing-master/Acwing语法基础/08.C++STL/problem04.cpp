/*
17. 从尾到头打印链表

输入一个链表的头结点，按照 从尾到头 的顺序返回节点的值。

返回的结果用数组存储。

数据范围
0≤ 链表长度 ≤1000。

样例
输入：[2, 3, 5]
返回：[5, 3, 2]
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

struct ListNode {
    int val;
    ListNode *next;
    // ListNode(int x) : val(x), next(NULL) {}
};

#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

class Solution {
public:
    vector<int> printListReversingly(ListNode* head) {
        vector<int> vec;
        while(head){
            vec.push_back(head->val);
            head = head->next;
        }
        int temp = vec.size() - 1;
        for(int i = 0; i < vec.size()/2; i++){
            swap(vec[i], vec[temp - i]);
        }
        return vec;
    }
};

/*

算法
(遍历链表) O(n)O(n)
单链表只能从前往后遍历，不能从后往前遍历。

因此我们先从前往后遍历一遍输入的链表，将结果记录在答案数组中。
最后再将得到的数组逆序即可。

时间复杂度分析
链表和答案数组仅被遍历了常数次，所以总时间复杂度是 O(n)O(n)。

C++ 代码

class Solution {
public:
    vector<int> printListReversingly(ListNode* head) {
        vector<int> res;
        while (head) {
            res.push_back(head->val);
            head = head->next;
        }
        return vector<int>(res.rbegin(), res.rend());
    }
};

// 法二：递归. 时间:O(n);空间:栈空间O(n). 4ms; 10.8MB
class Solution {
public:
    vector<int> printListReversingly(ListNode* head) {
        if (!head) return {};
        auto res = printListReversingly(head->next);
        res.push_back(head->val);
        return res;
    }
};

// 法三：辅助栈法. 时间:O(n);空间:O(n). 4ms; 8.5MB
class Solution {
public:
    vector<int> printListReversingly(ListNode* head) {
        stack<int> s;
        while (head) {
            s.push(head->val); // 存的是 val
            head = head->next;
        }

        int n = s.size();
        vector<int> res(n);
        for (int i = 0; i < n; i ++ ) {
            res[i] = s.top();
            s.pop();
        }

        return res;
    }
};

*/