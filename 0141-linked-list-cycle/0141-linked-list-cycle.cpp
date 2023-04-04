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
            if(dict.find(head) == dict.end()){
                dict[head] = 1;
                head = head->next;
            }
            else{
                return true;
            }
        }
        return false;
    }
};