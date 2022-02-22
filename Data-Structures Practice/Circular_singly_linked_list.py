
class node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next


class CircularSingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
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


