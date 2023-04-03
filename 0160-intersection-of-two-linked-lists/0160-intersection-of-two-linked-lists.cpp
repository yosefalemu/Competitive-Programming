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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        int lengthA = 0;
        int lengthB = 0;
        ListNode* tempA = headA;
        ListNode* tempB = headB;
        while(tempA){
            lengthA += 1;
            tempA = tempA->next;
        }
        while(tempB){
            lengthB += 1;
            tempB = tempB->next;
        }
        if(lengthA > lengthB){
            while(lengthA > lengthB){
                headA = headA->next;
                lengthA -= 1;
            }
        }
        if(lengthB > lengthA){
            while(lengthB > lengthA){
                headB = headB->next;
                lengthB -= 1;
            }
        }
        while(headA && headB){
            if(headA == headB){
                return headA;
            }
            headA = headA->next;
            headB = headB->next;
        }
        return 0;
        
    }
};