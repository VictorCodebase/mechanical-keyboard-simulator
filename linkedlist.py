


#! trying to understand how linked list works
class Node:
    def __init__(self, data = None, next = None):
        self.data = data # the data the node holds. This can be integers, numbers or complex objects
        self.next = next #a pointer to the next node
    
class LinkedList:
    def __init__(self):
        self.head = None #this will point to the head of the linked list

    def insert(self, data): #! Insert will add to the front
        node = Node(data, self.head) #So when we create a new node, it will point to the existing head
        self.head = node #then here; it becomens the current head

    def append(self, data): #! append will add to the back
        if self.head == None:
            self.head = Node(data, None) #This node points to none - obviously
            return
        #Youll have to eiterate through the linked list to the very end, then insert the new node. 
        #So we'll do something like what we did in print_linked_list()
        temp = self.head
        while temp.next: #here we want to make sure there is a next value before assigning temp
            temp = temp.next
        
        #Now that we are at the last element which points to None, we want to point it to the new node
        temp.next = Node(data, None)

    def insert_multiple(self, data_list):
        for data in data_list:
            self.insert_behind(data)
    
    def clear_list(self):
        self.head = None
    
    def pop(self, index):
        if index < 0 or index >= self.length():
            raise Exception("invalid index")
        
        if index == 0: #trying to remove the head
            self.head = self.head.next
            return
        
        count = 0
        temp = self.head
        while temp:
            if count == index - 1:
                temp.next = temp.next.next #Here is a nifty little trick. If you remove the reference to the next value you are essentially leaving it to the gabbage collector
                break
            temp = temp.next
            count += 1

    def to_string(self):
        if self.head is None:
            return '_'
        
        temp = self.head
        llstr = ''
        while temp:
            llstr += str(temp.data)
            temp = temp.next
        return llstr
    


    def insert_val_at(self, index, data):
        if index < 0 or index >= self.length():
            raise Exception("invalid index")
        if index == 0:
            self.insert_infront(data)
            return
        
        count = 0
        temp = self.head
        while temp:
            if count == index - 1: #we need to modify the pointer to the new data to point to its location
                node = Node(data, temp.next) #create a new node pointing to the next value
                temp.next = node # point to the new node
            temp = temp.next
            count += 1




    def length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count
    
    def display(self):
        if self.head is None:
            print ("empty")
            return
        
        temp = self.head
        llstr = ''
        while temp:
            llstr += str(temp.data)
            temp = temp.next #while temp.next (a pointer to the next node) exists...
        print(llstr)
        

