#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct Node {
    int data;
    struct Node* left;
    struct Node* right;
};

struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}


void appendNode(struct Node** head_ref, int new_data) {
    struct Node* newNode = createNode(new_data);
    if (*head_ref == NULL) {
        *head_ref = newNode;
        return;
    }

    struct Node* current = *head_ref;
    struct Node* parent = NULL;

    while (current != NULL) {
        parent = current;
        if (new_data < current->data) {
            current = current->left;
        } else {
            current = current->right;
        }
    }

    if (new_data < parent->data) {
        parent->left = newNode;
    } else {
        parent->right = newNode;
    }
}


void printTree(struct Node* node) {
    if (node == NULL) {
        return;
    }
    printTree(node->left);
    printf("%d ", node->data);
    printTree(node->right);
}

void deleteTree(struct Node* node) {
    if (node == NULL) {
        return;
    }
    deleteTree(node->left);
    deleteTree(node->right);
    free(node);
}


int main() {
    struct Node* head = NULL;

    appendNode(&head, 1);
    appendNode(&head, 2);
    appendNode(&head, 3);

    printTree(head);

    deleteTree(head);

    
    return 0;
}
