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
    ListNode* rotateRight(ListNode* head, int k) {
        int length = 0;
        ListNode* temp = head;
        while(temp){
            temp = temp->next;
            length ++;
        }
        if(length == 0){
            return head;
        }
        k = k % length;
        if(k == 0){
            return head;
        }
        temp = head;
        ListNode* dummy = new ListNode();
        ListNode* curr = dummy;
        while(length > k){
            curr->next = temp;
            curr = curr->next;
            temp = temp->next;
            length --;
        }
        curr->next = nullptr;
        head = temp;
        
        while(temp){
            if(temp->next == nullptr){
                temp->next = dummy->next;
                break;
            }
            temp = temp->next;
        }
        return head;
    }
};