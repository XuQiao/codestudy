#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <cmath>
#include <stdlib.h>     /* atoi */
#include <string>

struct ListNode{
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

void print(ListNode *head){
    ListNode *p = head;
    while(p != NULL){
        std::cout << p->val << " -> ";
        p = p->next;
    }
    std::cout << "NULL" << std::endl;
}

ListNode* reversell(ListNode *head, int m, int n){
    ListNode *newhead = new ListNode(-1);
    newhead->next = head;
    ListNode *pre = newhead;
    for(int i = 0; i < m-1; i++){
        pre = pre->next;
    }
    ListNode *reversedPre = pre;
    pre = pre->next;
    ListNode *cur = pre->next;
    for(int i = m; i < n; i ++){
        pre->next = cur->next;
        cur->next = reversedPre->next;
        reversedPre->next = cur; //reverse the order
        cur = pre->next; //go to next position
    }
    return newhead->next;
}

int main(int argc, char *argv[]){
    ListNode *head = new ListNode(0);
    ListNode *p = head;
    for(int i = 1 ; i < 10; i++){
        p->next = new ListNode(i);
        p = p->next;
    }
    print(head);
    reversell(head, 2, 5);
    print(head);
}
