/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
    struct ListNode* dummy=(struct ListNode*)malloc(sizeof(struct ListNode));

    dummy->val=-1;
    dummy->next=head;


    
    struct ListNode* fast=head;
    struct ListNode* slow=dummy;

   

    while (n>0 && fast!=NULL){
        
        fast=fast->next;
        n--;


    }

    while(fast!=NULL){
        slow=slow->next;
        fast=fast->next;
    }
   
    slow->next=slow->next->next;
    
    return dummy->next;
}