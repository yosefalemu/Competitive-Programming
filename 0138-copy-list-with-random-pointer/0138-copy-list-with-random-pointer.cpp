/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        unordered_map<Node*,Node*>dict1;
        Node* curr = head;
        while(curr){
            Node* temp = new Node(curr->val);
            dict1[curr] = temp;
            curr = curr->next;
        }
        curr = head;
        while(curr){
            dict1[curr]->next = dict1[curr->next];
            dict1[curr]->random = dict1[curr->random];
            curr = curr->next;
        }
        return dict1[head];
    }
};