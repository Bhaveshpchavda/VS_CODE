class Stack:
    def __init__(self, size):
        self.S = []
        self.size = size
        
    def push(self, data):
        if len(self.S) < self.size:
            self.S.append(data)
        else:
            print("Stack is full! [OVERFLOW]")
 
    def pop(self):
        try:
            return self.S.pop()
        except IndexError:
            print("Stack is empty! [UNDERFLOW]")
 
    def peek(self):
        if len(self.S) > 0:
            return self.S[len(self.S)-1]
        else:
            print("Stack is empty!")
 
    def display(self):
        print(self.S)
        
S = Stack(3)
S.push(1)
S.push(2)
S.push(3)
S.display()
print("Element on TOS:",S.peek())
S.push(4)
print("Element Popped:",S.pop())
S.display()
print("Element Popped:",S.pop())
print("Element Popped:",S.pop())
S.display()
print("Element Popped:",S.pop())
