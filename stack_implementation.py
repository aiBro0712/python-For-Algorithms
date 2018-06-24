class Stack:
    
    
    def __init__(self):
        '''
        initializing Empty list
        '''
        self.items = []
        
        
     
    def isEmpty(self):
        '''
        isEmpty() tests to see whether the stack is empty. 
        It needs no parameters and returns a boolean value. 
        '''
        return self.items == [] 
    
    
        
    def push(self, item):
        '''
        push(item) adds a new item to the top of the stack. 
        It needs the item and returns nothing.
        '''
        return self.items.append(item)
   
  
    
        
    def pop(self):
        '''
        pop() removes the top item from the stack.
        It needs no parameters and returns the item. The stack is modified.
        '''
        return  self.pop()
    
    
    
    def peek(self):
          '''
         peek() returns the top item from the stack but does not remove it. 
         It needs no parameters. The stack is not modifie
          '''
          return self.items[len(self.items)-1]
   
    
    def size(self):
        '''
         size() returns the number of items on the stack.
          It needs no parameters and returns an integer.
        '''
        return len(self.items)