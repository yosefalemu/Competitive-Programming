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
#include <cmath>
class Solution {
public:
    int getDecimalValue(ListNode* head) {
        ListNode* prev = nullptr;
        while(head){
            ListNode* temp = head->next;
            head->next = prev;
            prev = head;
            head = temp;
        }
        int exp = 0;
        int sum = 0;
        while(prev){
            sum += prev->val * pow(2,exp);
            prev = prev->next;
            exp += 1;
        }
        return sum;
    }
   
};