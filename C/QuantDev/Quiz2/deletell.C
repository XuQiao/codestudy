#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <cmath>
#include <stdlib.h>     /* atoi */
#include <string>

//using two pointers, one pointer remains here and another pointer goes to the next next position then link these two positions.

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

ListNode* deletell(ListNode *head, int n){
    ListNode *p = head;
    for(int i = 0; i < n; i ++){
       p = p->next;
    }
    ListNode *q = p->next->next;
    p->next = q;
    return head;
}

int main(int argc, char *argv[]){
    ListNode *head = new ListNode(0);
    ListNode *p = head;
    for(int i = 1 ; i < 10; i++){
        p->next = new ListNode(i);
        p = p->next;
    }
    print(head);
    deletell(head, 5);
    print(head);
}
