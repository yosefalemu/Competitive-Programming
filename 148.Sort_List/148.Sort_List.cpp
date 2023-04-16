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
    ListNode* sortList(ListNode* head) {
        if(! head || ! head->next){
            return head;
        }
        ListNode* slow = head;
        ListNode* fast = head->next;
        while(fast && fast->next){
            slow = slow->next;
            fast = fast->next->next;
        }
        ListNode* mid = slow->next;
        slow->next = NULL;
        ListNode* left = sortList(head);
        ListNode* right = sortList(mid);
        
        ListNode* merged = new ListNode();
        ListNode* curr = merged;
        while(left && right){
            if(left->val < right->val){
                curr->next = left;
                left = left->next;
            }
            else{
                curr->next = right;
                right = right->next;
            }
            curr = curr->next;
        }
        if(left){
            curr->next = left;
        }
        if(right){
            curr->next = right;
        }
        return merged->next;
    }
};
