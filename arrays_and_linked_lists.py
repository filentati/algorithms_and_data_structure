# Иллюстрация работы массива 
from typing import Any


class Array:
    
    def __init__(self, capacity: int, el_type: Any):
        self.array = [None]*capacity
        self.el_type = el_type
        
    def get(self, index: int):
        return self.array[index]
    
    def append(self, index: int, value: Any):
        if not isinstance(value, self.el_type):
            raise ValueError(f"value is {type(value)}; but must be {type(self.el_type)}")
        
        self.array[index] = value 
    
ar = Array(64, int)

ar.append(0, 1)
ar.append(1, 2)
ar.append(2, 3)

print(ar.get(1))
        
            
# Иллюстрация работы данимаческого массива 

class DynamicArray(object):
    
    def __init__(self):
        self.count = 1
        self.size = 0
        self.capacity = 1
        self.array = self.make_array(self.capacity)
        
    def make_array(self, capacity):
        return [None]*capacity
        
    def cap(self):
        return self.capacity
    
    def resize(self):
        new_cap = self.capacity*2
        new_array = self.make_array(new_cap)
        
        for i in range(self.size):
            self.count += 1
            new_array[i] = self.array[i]
        
        self.array = new_array
        self.capacity = new_cap
    
    def append(self, element: Any):
        if self.size == self.capacity:
            self.resize()
        
        self.array[self.size] = element
        self.size += 1
        

dar = DynamicArray()

dar.append('11')
dar.append('22')
dar.append('33')

print(dar.cap())

# Односвязанный список 

class Node:   
    def __init__(self, element):
        self.data = element 
        self.next = None
        
class LinkedList(object):
    def __init__(self):
        self.head = None
        
    def append_head(self, data):
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            return 
        
        new_node.next = self.head
        self.head = new_node
        
    def append_tail(self, data):
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node 
            return
        
        cur_node = self.head
        
        while cur_node.next:
            cur_node = cur_node.next 
            
        cur_node.next = new_node
        
    def print_list(self):
        cur_node = self.head 
        output = ""
        
        while cur_node is not None:
            output += str(cur_node.data)
        
            if cur_node.next:
                output += "->"
            
            cur_node = cur_node.next
        
        print(output)
        
    def append_mid(self, data, after):
        new_node = Node(data)
        counter = 0 
        cur_node = self.head
        
        while counter < after:
            counter += 1
            cur_node = cur_node.next 
        
        new_node.next = cur_node.next
        cur_node.next = new_node
        
            

            
link_list = LinkedList()

link_list.append_head(1)
link_list.append_head(2)

link_list.append_tail(3)
link_list.append_tail(4)

link_list.append_mid(5, 1)
link_list.append_mid(6, 2)

link_list.print_list()

        
#Двусвязный список 
class Node_2:
    def __init__(self, element):
        self.data = element 
        self.next = None 
        self.prev = None
        
class DoubleLinkedList(object):
    def __init__(self):
        self.head = None 
        
    def append_head(self, data):
        new_node = Node_2(data)
        
        if self.head is None:
            self.head = new_node
            return 
        
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        
    def append_tail(self, data):
        new_node = Node_2(data)
        
        if self.head is None:
            self.head = new_node 
            return 
        
        cur_node = self.head
        while cur_node is not None:
            cur_node = cur_node.next
            
        cur_node.next = new_node 
        new_node.prev = cur_node 
        
        
        
            
        