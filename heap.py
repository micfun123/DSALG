
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
    
    def add(self, data):
        self.heap.append(data)
        currlen = len(self.heap) - 1
        if currlen == 0: return
        pairentI = self.getparent(currlen)
        while ((pairentI != None) and (self.heap[pairentI] > self.heap[currlen]) ):
            self.heap[pairentI], self.heap[currlen] = self.heap[currlen], self.heap[pairentI]
            currlen = pairentI
            pairentI = self.getparent(currlen)



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