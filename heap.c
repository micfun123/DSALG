#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h> 



typedef struct minHeap
{
    int *array;
    int size;
} minHeap;

// create a minHeap instance
minHeap* createMinHeap(int capacity)
{
    minHeap* heap = (minHeap*)malloc(sizeof(minHeap));
    heap->array = (int*)malloc(capacity * sizeof(int));
    heap->size = 0;
    return heap;
}

bool isEmpty(minHeap* heap)
{
    return heap->size == 0;
}

void swap(int* a, int* b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}


int getparent(int nodeI){    
    if (nodeI <= 0) return -1;
    return (nodeI - 1) / 2;

}


int leftchildindex(int nodeI, minHeap* heap){
    if(2 * nodeI + 1 > heap->size){return -1;}    
    return 2 * nodeI + 1;
}


int rightchildindex(int nodeI, minHeap* heap){
    if(2 * nodeI + 2 > heap->size){return -1;}    
    return 2 * nodeI + 2;
}


void bubbleup(int nodeI, minHeap* heap){
    int parentI = getparent(nodeI);
    if (parentI == -1) return;
    while ((parentI != -1) && (heap->array[parentI] > heap->array[nodeI])){
        swap(&heap->array[parentI], &heap->array[nodeI]);
        nodeI = parentI;
        parentI = getparent(nodeI);
    }
}

void bubbledown(int nodeI, minHeap* heap){
    int leftI = leftchildindex(nodeI,heap);
    int rightI = rightchildindex(nodeI,heap);
    int smallestI = nodeI;
    if ((leftI != -1) && (heap->array[leftI] < heap->array[smallestI])){
        smallestI = leftI;
    }
    if ((leftI != -1) && (heap->array[rightI] < heap->array[smallestI])){
        smallestI = rightI;
    }
    if(smallestI != nodeI){
        swap(&heap->array[nodeI], &heap->array[smallestI]);
        bubbledown(smallestI,heap);
    }
}

void add(int val,minHeap* heap){
    heap->size = heap->size + 1;
    heap->array = realloc(heap->array, heap->size * sizeof(int));
    heap->array[heap->size -1 ] = val;
    bubbleup(heap->size - 1 ,heap);
}

void pop(minHeap* heap){
    heap->array[0] = heap->array[heap->size - 1];
    heap->size = heap->size - 1;
    heap->array = realloc(heap->array, heap->size * sizeof(int));
    bubbledown(0,heap);
}


int main()
{
    
    minHeap *heap = createMinHeap(10);
    
    printf("Initial size of the heap: %d\n", heap->size);
    printf("\n");

    add(5, heap);
    add(3, heap);
    add(8, heap);
    add(1, heap);
    add(7, heap);
    add(6, heap);
    printf("Size of the heap after adding elements: %d\n", heap->size);

    printf("Elements in the heap:\n");
    for (int i = 0; i < heap->size; i++) {
        printf("%d ", heap->array[i]);
    }
    printf("\n");

    pop(heap);
    printf("Elements in the heap:\n");
    for (int i = 0; i < heap->size; i++) {
        printf("%d ", heap->array[i]);
    }

    return 0;
}
