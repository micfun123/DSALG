#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h> 

#define FLOORDIV(a,b) \
((a)/(b) - (((a)%(b) != 0) && (((a)%(b) > 0) != ((b) > 0))))



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
    if (nodeI <= 0) return NULL;
    return FLOORDIV((nodeI - 1), 2);

}


void bubbleup(int nodeI, minHeap* heap){
    int parentI = getparent(nodeI);
    if (parentI == NULL) return;
    while ((parentI != NULL) && (heap->array[parentI] > heap->array[nodeI])){
        swap(&heap->array[parentI], &heap->array[nodeI]);
        nodeI = parentI;
        parentI = getparent(nodeI);
    }
}

void add(int val,minHeap* heap){
    heap->size = heap->size + 1;
    heap->array = realloc(heap->array, heap->size);
    heap->array[heap->size -1 ] = val;
    bubbleup(heap->size,heap);
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




    return 0;
}