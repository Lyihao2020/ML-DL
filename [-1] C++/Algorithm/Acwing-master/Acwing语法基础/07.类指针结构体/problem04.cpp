/*
28. 在O(1)时间删除链表结点

给定单向链表的一个节点指针，定义一个函数在O(1)时间删除该结点。

假设链表一定存在，并且该节点一定不是尾节点。

数据范围
链表长度 [1,500]。

样例
输入：链表 1->4->6->8
      删掉节点：第2个节点即6（头节点为第0个节点）

输出：新链表 1->4->8
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
    void deleteNode(ListNode* node) {
        auto p = node->next;
        
        node->val = p->val;
        node->next = p->next;
        
        delete p;
        
    }
};

/*
算法
(链表) O(1)
由于是单链表，我们不能找到前驱节点，所以我们不能按常规方法将该节点删除。
我们可以换一种思路，将下一个节点的值复制到当前节点，然后将下一个节点删除即可。

时间复杂度
只有常数次操作，所以时间复杂度是 O(1)。

class Solution {
public:
    void deleteNode(ListNode* node) {

        auto p = node->next;

        node->val = p->val;
        node->next = p->next;
        // *node = *(node->next);

        delete p;
    }
};

*/
