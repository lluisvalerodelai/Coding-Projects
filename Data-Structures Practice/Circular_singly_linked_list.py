class node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next


class CircularSingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        if not self.head:
            return None
        
        curNode = self.head
        while curNode != self.tail:
            yield curNode.value
            curNode = curNode.next
        yield curNode.value
    
    def create(self, node):
        self.head = node
        self.tail = node
        node.next = node
    
    def insert(self, node, index):
        if index == 0:
            node.next = self.head
            self.head = node
            self.tail.next = node
            return 'done'
        elif index == -1:
            node.next = self.tail.next
            self.tail.next = node
            self.tail = node
            return 'done'
        else:
            curNode = self.head
            pos = 0
            while pos != index:
                curNode = curNode.next
                pos += 1
            
            node.next = curNode.next
            curNode.next = node
            return 'done'
        return 'error maybe?'
    
    def isin(self, node_Value):
        if not self.head:
            return False
        elif self.head.value == node_Value:
            return True
        else:
            curNode = self.head
            while curNode.value != node_Value:
                if curNode == self.tail:
                    return False
                else:
                    curNode = curNode.next
            return True
    
    def delete(self, location):
        if self.head is None:
            return 'done'
        elif location == 0:
            if self.head == self.tail:
                self.head.next = None
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.tail.next = self.head
        elif location == -1:
            if self.head == self.tail:
                self.head.next = None
                self.head = None
                self.tail = None
            else:
                node = self.head
                while node is not None:
                    if node.next == self.tail:
                        break
                    node = node.next
                node.next = self.head
                self.tail = node
        else:
            tempNode = self.head
            index = 0
            while index < location - 1:
                tempNode = tempNode.next
                index += 1
            nextNode = tempNode.next
            tempNode.next = nextNode.next
    def deletAll(self):
        self.head == None
        self.tail.next == None
        self.tail == None
        
