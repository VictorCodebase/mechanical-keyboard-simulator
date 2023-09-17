class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def pop(self, value):
        if not self.head:
            raise Exception("LinkedList is empty")
        
        # If the head node contains the value to pop
        if self.head.data == value:
            popped_element = self.head
            self.head = self.head.next
            popped_element.next = None
            return popped_element.data
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    
    def length(self):
        current = self.head
        length = 0
        while current:
            length += 1
            current = current.next
        return length
    
    #creare a function that returns an array of all elements in the linked list
    def toString(self):
        current = self.head
        array = []
        while current:
            array.append(current.data)
            current = current.next
        return ''.join(array)

# Create a linked list
my_linked_list = LinkedList()

# Append elements to the linked list
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)

# Display the linked list
my_linked_list.display()
