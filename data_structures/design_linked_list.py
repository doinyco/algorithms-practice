class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        
class SinglyLL:
    def __init__(self):
        self.head = None
        
    def print_linked_list(self):
        current = self.head
        
        while current:
            print(current.val, end="->")
            current = current.next
        print(None)
        
    def add_firt(self, val):
        new_node = Node(val, self.head)
        new_node.next = self.head
        self.head = new_node
        
    def get_node(self, index):
        if index < 0:
            return -1
        
        current = self.head
        current_index = 0
        
        while current:
            if current_index == index:
                return current.val

            current = current.next
            current_index += 1
        return - 1
        
    def get_first(self):
        if self.head is None:
            return None
        return self.head.val
        
    def add_at_index(self, index, val):
        if index < 0:
            return
        
        new_node = Node(val)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            
        current = self.head
        current_index = 0
        
        while current:
            if current_index == index - 1:
                new_node.next = current.next
                current.next = new_node
            current = current.next
            current_index += 1
        
        # If index is greater than the lenght of the list
        if current_index == index - 1:
            current.next = new_node
    
    def get_size(self):
        if self.head is None:
            return 0
            
        current = self.head
        count = 0
        
        while current:
            count += 1
            current = current.next
            
        return count
        
    def add_last(self, val):
        new_node = Node(val)
        
        if self.head is None:
            self.head = new_node
            return
            
        current = self.head
        
        while current.next:
            current = current.next
            
        current.next = new_node
    
    def delete_at_index(self, index):
        if index < 0 or not self.head:
            return 
        
        if index == 0:
            self.head = self.head.next
            return
        
        current = self.head
        previous = None
        current_index = 0
        
        while current:
            if current_index == index:
                previous.next = current.next
                return
            
            previous = current
            current = current.next
            current_index += 1
            

my_list = SinglyLL()
# my_list.add_firt(10)
# my_list.add_firt(20)
# my_list.add_firt(30)
# my_list.add_firt(40)
# my_list.add_firt(50)
# my_list.add_firt(60)

# get_val = my_list.get_node(index)
# print(get_val)
# get_first_node = my_list.get_first()
# print(get_first_node)

# my_list.add_at_index(0, 5)
# my_list.print_linked_list()
# get_size_of_ll = my_list.get_size()
# print(get_size_of_ll)

my_list.add_last(10)
my_list.add_last(20)
my_list.add_last(30)
my_list.add_last(40)
# my_list.print_linked_list()

my_list.delete_at_index(3)
my_list.print_linked_list()