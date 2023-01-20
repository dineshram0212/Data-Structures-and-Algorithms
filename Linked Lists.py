# Defining a class to create Node datatype
class Node:
    def __init__(self, data):   # Constructor with data to be passed as parameter
        self.data = data        # Denotes the data present in the NODE
        self.next = None        # Stores the reference to the next NODE(None by default)

class LinkedList:
    def __init__(self):
        self.head = None            # Creates the head which points to the first Node(None when the list is empty)

    # To insert node in the first place of the LinkedList (Arg: Data to be pushed)
    def push(self, value):
        new_node = Node(value)      # Creates a node with the data given as parameter 
        new_node.next = self.head   # Next of the new node refers to what head was referring previously
        self.head = new_node        # Head refers to the node that was inserted

    # To insert node at a specfic location in the LinkedList (Args: Data to be inserted, Node after which the data needs to be inserted)
    def insertAt(self, value, prevNode):
        # If the previous node doesn't exist
        if prevNode is None:
            print("Previous Node doesn't exist!")
        new_node = Node(value)          # Creates node
        new_node.next = prevNode.next   # Next of new node refers to the Next of the previous node
        prevNode.next = new_node        # Next of the previos node refers to the new node
    
    # To insert a node at the end of the LinkedList (Args: Data to appended)
    def append(self, value):
        new_node = Node(value)          # Creates node
        # Case 1 - When the list is empty
        if self.head is None:           # If the Linkedlist is empty (When head points to NULL)
            # new_node.next = self.head   # Next of new node points to None that head was referring (next is None by default)
            self.head = new_node        # Head refers to the new node
            return

        # Case 2 - When the list is not empty
        last = self.head                # Consider head as the last value 
        while(last.next):               # Traverse through the list until finding the last node(last node refers to NULL)
            last = last.next            # Update the last variable
        
        last.next = new_node            # Last value refers to the new node appended

    # To print the elements in the List
    def printList(self):
        temp = self.head        # Create temporary variable pointing to head
        while(temp):            # Traverse the list until last node
            print(temp.data)    # Print the value stored in the node
            temp = temp.next    # Increment the temporary variable that points to the next node

    def deleteNode(self, key):
        temp = self.head        # reate temporary variable that points to head

        #Case 1 - When the node to be deleted is the first node
        if(temp is not None):           # When the LinkedList is not empty
            if(temp.data == key):       # If the first element is the key
                self.head = temp.next   # Head refers to next node of the deleted node
                temp = None             # Delete the node
                return

        #Case 2 - When the node is in any other place of the LinkedList
        while(temp is not None):        # When the LinkedList is not empty
            if(temp.data==key):         # If the data is key
                break                   # Break 
            prev = temp                 # Update previous node as temp
            temp = temp.next            # Update temp to next node

        #Case 3 - When the node doesn't exist
        if(temp is None):               # If there are no elements, return nothing
            return
        
        prev.next = temp.next           # Previous node points to the node after the deleted node
        temp = None                     # Remove the temp

    # Delete entire list
    def deleteList(self):
        curr = self.head            # Start from the head
        while(curr):                # Traverse the list until current doesn't exist 
            nextNode = curr.next    # Store the node after current to a variable
            del curr.data           # Delete the data from the current node
            curr = nextNode         # Now the next node will be your current node

    # Count the length of the list
    def countNode(self, node):
        if(not node):       
            return 0                                # Return 0 when there is no node
        else:
            return 1 + self.countNode(node.next)    # Increment the count
    
    def getCount(self):
        return self.countNode(self.head)            # Passing head as argument in the countNode method  

    # Reverse the elements in the list
    def reverseList(self):
        prev = None                 # Create n set variable "prev" to NULL
        current = self.head         # Set head as current 
        
        while(current is not None):         # While current is not last node
            next = current.next             # Set the next of current to "next" variable
            current.next = prev             # Set previous node of current to its next (Reversing the path)
            prev = current                  # Set current node to prev variable
            current = next                  # Set next node as current node
        self.head = prev            # Set last node as head



llist = LinkedList()
llist.append(5)
llist.append(6)
llist.append(7)
print(llist.getCount())
llist.printList()
llist.reverseList()
llist.printList()
