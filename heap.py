
class minheap:
    def __init__(self):
        self.heap = []

    def getmin(self):
        if len(self.heap) > 0: return self.heap[0]
        else: return None

    def getparent (self, index):
        if index == 0: return None
        return (index - 1) // 2
    
    def leftchildindex (self, index):
        left = 2 * index + 1
        if left >= len(self.heap): return None
        return left
    
    def rightchildindex (self, index):
        right = 2 * index + 2
        if right >= len(self.heap): return None
        return right
    
    def bubbleup(self,nodeI):
        pairentI = self.getparent(nodeI)
        while ((pairentI != None) and (self.heap[pairentI] > self.heap[nodeI]) ):
            self.heap[pairentI], self.heap[nodeI] = self.heap[nodeI], self.heap[pairentI]
            nodeI = pairentI
            pairentI = self.getparent(nodeI)

    def bubbledown(self,nodeI):
        leftI = self.leftchildindex(nodeI)
        rightI = self.rightchildindex(nodeI)
        smallestI = nodeI

        if (leftI != None) and (self.heap[leftI] < self.heap[smallestI]):
            smallestI = leftI
        if (rightI != None) and (self.heap[rightI] < self.heap[smallestI]):
            smallestI = rightI
        if smallestI != nodeI:
            self.heap[smallestI], self.heap[nodeI] = self.heap[nodeI], self.heap[smallestI]
            self.bubbledown(smallestI)
    
    def add(self, data):
        self.heap.append(data)
        currlen = len(self.heap) - 1
        if currlen == 0: return
        self.bubbleup(currlen)

    def remove(self):
        element = self.heap.pop(0)
        self.heap.insert(0, self.heap.pop(len(self.heap)-1))
        self.bubbledown(0)
        return element
      

heap = minheap()
print(heap.getmin())

heap.add(5)
heap.add(3)
heap.add(8)
heap.add(9)
heap.add(2)


print(heap.heap)
print(heap.getmin())
print(heap.heap[heap.leftchildindex(0)])
print(heap.heap[heap.rightchildindex(0)])
print(heap.remove())
print(heap.heap)