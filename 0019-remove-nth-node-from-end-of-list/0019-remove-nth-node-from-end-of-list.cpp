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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* curr = head;
        int length = 0;
        while(curr){
            curr = curr->next;
            length ++;
        }
        if(length == 1){
            return NULL;
        }
        int position = length - n + 1;
        if(position == 1){
            return head->next;
        }
        int index = 0;
        curr = head;
        while(index < position - 2){
            curr = curr->next;
            index ++;
        }
        curr->next = curr->next->next;
        return head;
    }
};