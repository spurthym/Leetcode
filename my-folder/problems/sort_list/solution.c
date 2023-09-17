/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

// Function to merge two sorted linked lists
struct ListNode* merge(struct ListNode* list1, struct ListNode* list2) {
    if (list1 == NULL)
        return list2;
    if (list2 == NULL)
        return list1;

    if (list1->val < list2->val) {
        list1->next = merge(list1->next, list2);
        return list1;
    } else {
        list2->next = merge(list1, list2->next);
        return list2;
    }
}

// Function to perform merge sort on a linked list
struct ListNode* mergeSort(struct ListNode* head) {
    if (head == NULL || head->next == NULL)
        return head;

    // Find the middle of the list
    struct ListNode* slow = head;
    struct ListNode* fast = head;
    struct ListNode* prev = NULL;

    while (fast != NULL && fast->next != NULL) {
        prev = slow;
        slow = slow->next;
        fast = fast->next->next;
    }

    // Split the list into two halves
    prev->next = NULL;

    // Recursively sort both halves
    struct ListNode* left = mergeSort(head);
    struct ListNode* right = mergeSort(slow);

    // Merge the sorted halves
    return merge(left, right);
}

struct ListNode* sortList(struct ListNode* head) {
    return mergeSort(head);
}
