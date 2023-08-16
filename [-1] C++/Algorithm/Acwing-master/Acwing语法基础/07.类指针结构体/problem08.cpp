/*
35. 反转链表

定义一个函数，输入一个链表的头结点，反转该链表并输出反转后链表的头结点。

思考题：

请同时实现迭代版本和递归版本。
数据范围
链表长度 [0,30]。

样例
输入:1->2->3->4->5->NULL

输出:5->4->3->2->1->NULL
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* cur = head;
        while(cur){
        	ListNode* next = cur->next;
        	cur->next = prev;
        	prev = cur;
        	cur = next;
		}
		return prev; 
    }
};

/*


class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode *prev = nullptr;
        ListNode *cur = head;
        while (cur)
        {
            ListNode *next = cur->next;
            cur->next = prev;
            prev = cur, cur = next;
        }
        return prev;
    }
};


class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (!head || !head->next) return head;
        ListNode *tail = reverseList(head->next);
        head->next->next = head;
        head->next = nullptr;
        return tail;
    }
};

*/
