class node:
    def __init__(self, value = None, nextvalue = None):
        self.value = value
        self.nextvalue = nextvalue
    
    def changeValue(self, new_value):
        self.value = new_value
        return

    def printnext(self):
        print(self.next)
        return
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, node, pos):
        assert self.head != None, print('cant insert into empty list')
        currentnode = self.head
        curpos = 0
        while currentnode != None:
            if curpos == pos:
                node.next = currentnode.next
                currentnode.next = node
            curpos += 1

            currentnode = currentnode.next

    def removeValue(self, value):
        currentnode = self.head
        while currentnode.value != None:
            if currentnode.next.value == value:
                currentnode.next == currentnode.next.next
                break
            else:
                currentnode = currentnode.next
    
    def removePos(self, pos):
        currentNode = self.head
        curpos = 0
        while currentNode != None:
            if curpos == pos - 1:
                currentNode.next = currentNode.next.next
                break
            currentNode = currentNode.next
            

    def find(self, value):
        #create a temporary variable called current node, set it to head, which is the first node in our LL
        currentnode = self.head
        #while the value of the current node is not equal to None, or in other words, while we have not reached the end of the list because the last node points to None
        while currentnode.value != None:
            #if our current nodes value is the same as the value we want, then we can just break out of the loop
            if currentnode.value == value:
                break
            #otherwise, we can just keep going, so we set out currentnode to be equal to the pointer of our current node, then repeat
            else:
                currentnode = currentnode.nextvalue
            
            #find method is the most important becausew with it we can do any other operation

    def addfirst(self, node):
        #we have a node, and we need to add it to the first point in the LL
        #the nodes next value gets set to the current head value
        node.next = self.head
        #we relocate the head pointer to be the node we just added
        self.head = node
        #we had a node which we wanted to add to the first location, 
        #we set the nodes next pointer to point at whichever the current head node was
        #we moved the head pointer to the new first node
    
    def printList(self):
        currentNode = self.head
        while currentNode.next != None:
            print(f"Current Node value: {currentNode.value} \n Next Value: {currentNode.next.value}")
        
            currentNode = currentNode.next
    
    def length(self):
        tempNode = self.head
        length = 0
        if self.head == None:
            return 0
        else:
            while tempNode.next != None:
                length += 1
                tempNode = tempNode.next
        
        return length

    
LList = LinkedList()


 
print(LList.length())

