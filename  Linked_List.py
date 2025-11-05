import copy

class SinglyLinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None

    def insert(self,data):
        new_node = self.Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete(self, index):
        if not self.head:
            return

        privous = None
        current = self.head
        count = 0
        while current and count < index:
            privous = current
            current = current.next
            count += 1
        if privous is None:
            self.head = current.next
        elif current:
            privous.next = current.next
        else:
            return
        
    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False
    


def sortSSL(sll):
    sll = copy.deepcopy(sll)
    if sll.head is None or sll.head.next is None:
        return sll
    

    swapped = True
    while swapped:
        swapped = False
        current = sll.head
        while current and current.next:
            if current.data > current.next.data:
                current.data, current.next.data = current.next.data, current.data
                swapped = True
            current = current.next
    return sll


def reverseSSL(sll):
    sll = copy.deepcopy(sll)
    prev = None
    current = sll.head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    sll.head = prev
    return sll


def murgeSortedSSL(sll1, sll2):
    merged_sll = SinglyLinkedList()
    ptr1 = sll1.head
    ptr2 = sll2.head

    while ptr1 and ptr2:
        if ptr1.data <= ptr2.data:
            merged_sll.insert(ptr1.data)
            ptr1 = ptr1.next
        else:
            merged_sll.insert(ptr2.data)
            ptr2 = ptr2.next

    while ptr1:
        merged_sll.insert(ptr1.data)
        ptr1 = ptr1.next

    while ptr2:
        merged_sll.insert(ptr2.data)
        ptr2 = ptr2.next

    return merged_sll


def murgeNSortedSSL(sll_list):
    if not sll_list:
        return SinglyLinkedList()
    
    merged_sll = sll_list[0]
    for i in range(1, len(sll_list)):
        merged_sll = murgeSortedSSL(merged_sll, sll_list[i])
    
    return merged_sll



# Example usage:
sll = SinglyLinkedList()
sll.insert(10)
sll.insert(20)
sll.insert(30)
sll.traverse()  # Output: 10 -> 20 -> 30 -> None
sll.delete(1)
sll.traverse()  # Output: 10 -> 30 -> None
sll.insert(15)
sll.insert(5)
sll.insert(25)
sll.traverse()  
sorted_sll = sortSSL(sll)
sorted_sll.traverse()  # Output: 5 -> 10 -> 15 -> 25 -> 30 -> None
reversed_sll = reverseSSL(sorted_sll)


ssl1 = SinglyLinkedList()
ssl1.insert(1)
ssl1.insert(4)
ssl1.insert(7)

ssl2 = SinglyLinkedList()
ssl2.insert(2)
ssl2.insert(5)
ssl2.insert(8)
merged_sll = murgeSortedSSL(ssl1, ssl2)

ssl3 = SinglyLinkedList()
ssl3.insert(0)
ssl3.insert(3)
ssl3.insert(6)

merged_n_sll = murgeNSortedSSL([ssl1, ssl2, ssl3])
merged_n_sll.traverse()  # Output: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> None