/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        ListNode* dummy = new ListNode();
        ListNode* ans = dummy;
        while (head){
            if(head->val == val){
                dummy->next = head->next;
            }
            else{
                dummy->next = head;
                dummy = head;
            }
            head = head->next;
        }
        return ans->next;
    }
};