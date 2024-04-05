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
            max=self.queue[0]
            ind=0
            for i in range(len(self.queue)):
                if(self.queue[i]>max):
                    max=self.queue[i]
                    ind=i

            self.queue.pop(ind)                
    def display(self):
        print(self.queue)
    
s=Queue()
s.Enqueue(50)
s.Enqueue(20)
s.Enqueue(60)
s.display()
s.Dequeue()
s.display()
s.Dequeue()
s.display()

s.Dequeue()
s.display()
s.Dequeue()