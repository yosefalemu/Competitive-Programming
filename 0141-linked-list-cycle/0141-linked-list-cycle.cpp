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
    bool hasCycle(ListNode *head) {
        unordered_map<ListNode*, int>dict;
        while(head != NULL){
            if(dict[head] == 1){
                return true;
            }
            else{
                dict[head] = 1;
            }
            head = head->next;
        }
        return false;
    }
};