class Stack:
    def __init__(self):
        self.stack = []

    def view_stack(self):             #Uses For Loop To Print Stack
        for i in range(len(self.stack)):
            print self.stack[i]

    def push(self, item):
        self.stack.append(item)       #Adds item to stack

    def pop(self):
        if not self.stack:            #If Stack is Empty then False is returned
            return False
        return self.stack.pop()       #pops the item on the right hand side of the list

    def peek(self):
        return self.stack[-1]         #Peeks The Top Value on Stack

    def isEmpty(self):                #If Stack is Empty then returns True
        if not self.stack:
            return True

    def __del__(self):                #Destructor Frees the memory by deleting stack
        del self.stack
