class Queue:
    
    
    def __init__(self):
        '''
        Queue() creates a new queue that is empty. 
        It needs no parameters and returns an empty queue.
        '''
        self.items = []
        
    def isEmpty(self):
        '''
        isEmpty() tests to see whether the queue is empty. 
        It needs no parameters and returns a boolean value.
        '''
        return self.items == []
    
    
    
    def insert_item(self,item):
        '''
        insert_item(item) adds a new item to the rear of the queue. 
        It needs the item and returns nothing.
        '''
        return self.items.insert(0,item)
    
    
    
    def delet_item(self):
        '''
        delet_items() removes the front item from the queue. 
        It needs no parameters and returns the item. The queue is modified.
        '''
        return self.items.pop()
    
    def size(self):
        '''
        size() returns the number of items in the queue. 
        It needs no parameters and returns an integer.
        '''
        return len(self.items)
        
       