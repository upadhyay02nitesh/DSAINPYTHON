class Queue:
    def __init__(self) :
        self.queue=[]
    def Enqueue(self,item):
        self.queue.append(item)
    def isEmpty(self):
        if (len(self.queue))==0:
            return True
    def Dequeue(self):
        if(self.isEmpty()):
            print("Underflow condition")
        else:
            self.queue.pop(0)
    def display(self):
        print(self.queue)
    
s=Queue()
s.Enqueue(10)
s.Enqueue(20)
s.Enqueue(30)
s.display()
s.Dequeue()
s.display()
s.Dequeue()
s.display()

s.Dequeue()
s.display()
s.Dequeue()