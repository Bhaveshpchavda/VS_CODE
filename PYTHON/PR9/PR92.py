class Stacks:
    s=[]
    def push(self):
        self.ele=int(input("PUSH your Element :- "))
        self.s.append(self.ele)
    def pop(self):
        self.pop_ele=self.s.pop()
        print("POP Element :- ",self.pop_ele)
    def peek(self):
        self.t=self.s[-1]
        print("PEEK Element :- ",self.t)
    def display(self):
        print("Elemnts:",self.s)

obj=Stacks()
print("Operations:")
print("-->1. PUSH\n-->2. POP\n-->3. PEEK\n-->4. DISPLAY")
while(True):
    ch=int(input("=>Enter a Operation above GIVEN: "))
    if ch==1:
        obj.push()
    elif ch==2:
        obj.pop()
    elif ch==3:
        obj.peek()
    elif ch==4:
        obj.display()
    elif ch==5:
        break