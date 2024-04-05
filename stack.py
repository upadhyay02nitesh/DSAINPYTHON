class Stack:
    def __init__(self) :
        self.stack=[]
    def push(self,item):
        self.stack.append(item)
    def isEmpty(self):
        if (len(self.stack))==0:
            return True
    def pop(self):
        if(self.isEmpty()):
            print("Underflow condition")
        else:
            self.stack.pop()
    def display(self):
        print(self.stack)
    def topElement(self):
        if (len(self.stack))==0:
            print("Underflow condition")
            return True
        else:
            print(self.stack[(len(self.stack)-1)])
s=Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()
s.pop()
s.pop()
s.display()
s.topElement()
