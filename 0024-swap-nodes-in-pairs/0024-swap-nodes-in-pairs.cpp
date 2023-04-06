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
    ListNode* swapPairs(ListNode* head) {
       if(!(head && head->next)){
           return head;
       }
        ListNode* dummy = new ListNode();
        ListNode* curr = dummy;
        while(head && head->next){
            ListNode* temp = head->next->next;
            curr->next = head->next;
            curr = curr->next;
            head->next->next = head;
            curr = curr->next;
            curr->next = nullptr;
            head = temp;
        }
        if(head){
            curr->next = head;
        }
        return dummy->next;
    }
};