class LRUCache {
public:
    class Node{
        public:
            int key;
            int val;
            Node* prev;
            Node* next;
            Node(int key, int val){
                this->key = key;
                this->val = val;
            }
    };
    
    Node* head = new Node(-1,-1);
    Node* tail = new Node(-1,-1);
    int capacity;
    unordered_map<int,Node*> dict1;
    
    LRUCache(int capacity) {
        this->capacity = capacity;
        head->next = tail;
        tail->prev = head;
    }
     void addNode(Node* curNode){
        curNode->next = head->next;
        curNode->prev = head;
        curNode->next->prev = curNode;
        head->next = curNode;
    }
    void deleteNode(Node* curNode){
        Node* prevNode = curNode->prev;
        Node* nextNode = curNode->next;
        prevNode->next = nextNode;
        nextNode->prev = prevNode;
    }
    
    
    int get(int key) {
        if(dict1.find(key) != dict1.end()){
            Node* temp = dict1[key];
            int value = temp->val;
            dict1.erase(key);
            deleteNode(temp);
            addNode(temp);
            dict1[key] = head->next;
            return value;
        }
        return -1;
    }
    
    void put(int key, int value) {
        if(dict1.find(key) != dict1.end()){
            Node* temp = dict1[key];
            dict1.erase(key);
            deleteNode(temp);
        }
        if(dict1.size() == capacity){
            dict1.erase(tail->prev->key);
            deleteNode(tail->prev);
        }
        addNode(new Node(key, value));
        dict1[key] = head->next;
        
    }
};


/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */