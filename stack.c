#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct StackNode {
    int data;
    struct StackNode* next;
};


struct StackNode* createStackNode(int data) {
    struct StackNode* newNode = (struct StackNode*)malloc(sizeof(struct StackNode));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

void push(struct StackNode** top_ref, int new_data) {
    struct StackNode* newNode = createStackNode(new_data);
    newNode->next = *top_ref;
    *top_ref = newNode;
}
int pop(struct StackNode** top_ref) {
    if (*top_ref == NULL) {
        printf("Stack underflow\n");
        exit(EXIT_FAILURE);
    }
    struct StackNode* temp = *top_ref;
    int popped = temp->data;
    *top_ref = (*top_ref)->next;
    free(temp);
    return popped;
}