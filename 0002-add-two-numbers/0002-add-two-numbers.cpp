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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int carry = 0;
        int num1 = 0;
        int num2 = 0;
        ListNode* dummy = new ListNode();
        ListNode* temp = dummy;
        while(l1 || l2 || carry){
            if(l1){
                num1 = l1->val;
                l1 = l1->next;
            }
            else{
                num1 = 0;
            }
            if(l2){
                num2 = l2->val;
                l2 = l2->next;
            }
            else{
                num2 = 0;
            }
            int sum = num1 + num2 + carry;
            int result = sum % 10;
            carry = sum / 10;
            ListNode* newNode = new ListNode(result);
            temp->next = newNode;
            temp = temp->next;
        }
        return dummy->next;
    }
};