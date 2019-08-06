class Queue:
    def __init__(self, capacity):
        self.front = self.size = 0
        self.rear = capacity-1
        self.capacity = capacity
        self.Q = [None]*capacity

    def isfull(self):
        return self.size == self.capacity

    def isempty(self):
        return self.size == 0

    def frontt(self):
        if self.isempty():
            print('queue is empty')
        print('front value is: ' , self.Q[self.front])

    def rearr(self):
        if self.isempty():
            print('queue is Empty')
        print('Rear value is: ', self.Q[self.rear])

    def Enqueue(self, num):
        if self.isfull():
            print('queue overloaded')
        else:
            self.rear = (self.rear + 1) % self.capacity
            print('now self.rear value is: ' , self.rear)
            self.Q[self.rear] = num
            print('The value of enqueue is: ', num)
            self.size +=1
            print(self.size)
        

    def dequeue(self):
        if self.isempty():
            print('queue is empty')
        else:
            print('the poped number is: ', self.Q[self.front])
            self.front = (self.front + 1) % self.capacity
            print(self.front) 
            self.size -=1
            print(self.size)



if __name__ == "__main__":
    queue = Queue(30)
    print(queue.capacity)
    
    print(queue.rear)
    queue.frontt()
    queue.Enqueue(2)
    queue.Enqueue(4)
    queue.Enqueue(6)
    queue.Enqueue(8)
    print(queue.Q)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.Q)
    print(queue.frontt())
    # queue.Enqueue(4)
    # queue.Enqueue(6)
    # queue.Enqueue(8)
    # queue.dequeue()
    # queue.frontt()
    # queue.rearr()
