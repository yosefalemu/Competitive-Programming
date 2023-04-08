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
    ListNode *detectCycle(ListNode *head) {
        unordered_map<ListNode*, int>dict1;
        while(head){
            if(dict1.find(head) != dict1.end()){
                return head;
            }
            dict1[head] = 1;
            head = head->next;
        }
        return NULL;
        
    }
};