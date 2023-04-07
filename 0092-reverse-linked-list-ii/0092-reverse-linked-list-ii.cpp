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
        ListNode* leftpt;
        ListNode* rightpt;
        ListNode* nextpt;
        ListNode* temp;
        ListNode* dummy = new ListNode();
        ListNode* curr = dummy;
        while(head){
            if(length == left){
                leftpt = head;
            }
            else if(length == right){
                rightpt = head;
                nextpt = head->next;
                break;
            }
            else if(length < left){
                curr->next = head;
                curr = curr->next;
            }
            length ++;
            head = head->next;
        }
        ListNode* prev = nullptr;
        int numREV = 0;
        while(numREV <= right - left){
            temp = leftpt->next;
            leftpt->next = prev;
            prev = leftpt;
            leftpt = temp;
            numREV ++;
        }
        curr->next = prev;
        while(curr->next){
            curr = curr->next;
        }
        curr->next = temp;
        return dummy->next;
        
        
    }
};