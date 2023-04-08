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
    void reorderList(ListNode* head) {
        ListNode* curr = head;
        stack<ListNode*>arr;
        int length = 0;
        while(curr){
            arr.push(curr);
            curr = curr->next;
            length ++;
        }
        curr = head;
        int lengthHalf = length / 2;
        while(lengthHalf > 0){
            ListNode *element = arr.top();
            arr.pop();
            element->next = curr->next;
            curr->next = element;
            curr = curr->next->next;
            lengthHalf --;
        }
        
        curr->next = nullptr;
    }
};