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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        int length = 1;
        ListNode* dummy = new ListNode();
        ListNode* curr = dummy;
        while(head){
            if(length != left){
                curr->next = head;
                curr = curr->next;
                head = head->next;
            }
            else{
                ListNode* prev = nullptr;
                while(length <= right){
                    ListNode* temp = head->next;
                    head->next = prev;
                    prev = head;
                    head = temp;
                    length ++;
                }
                curr->next = prev;
                while(prev){
                    curr = curr->next;
                    prev = prev->next;
                }
            }
            length ++;
        }
        return dummy->next;
    }
};