class circular_list:
    def __init__(self , num):
        self.front = self.rear = -1
        self.size = 0
        self.q = [None for i in range(num)]
        self.capacity = num
        print(self.size)
        print(self.q)

    def isfull(self):
        if (self.capacity == self.size):
            print('queue is full')

    def isempty(self):
        if (self.size == 0):
            print('queue is empty')

    def enqueue(self , data):
        print('hey')
        if (self.front == -1):
            print('hey2')
            self.front = 0
            self.rear = 0
            self.q[self.rear] = data
            self.size +=1

        elif (self.isfull()):
            print('queue is full')
            return

        else:
            print('hey1')
            print(self.rear)
            self.rear = (self.rear + 1) % self.capacity
            print('rear value is:')
            print(self.rear)
            self.q[self.rear] = data
            print(self.q[self.rear])
            self.size += 1
            print(self.size)
            #print(self.q[self.rear])
            print(self.q)
            

    def dequeue(self):
        print('hh')
        if self.isempty():
            print('queue is empty')

        elif (self.front == self.rear):
            temp = self.q[self.front]
            self.front = -1
            self.rear = -1
            print('qwertyui')

        else:
            print('hy')
            temp = self.q[self.front]
            self.front = self.front + 1
            print(temp)
            return temp

        print('dequeue element is: ') 

if __name__ == "__main__":
    queue = circular_list(5)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(2)
    print(queue.front)
    print(queue.rear)
    print(queue.q)
    queue.dequeue()
    queue.dequeue()
    print(queue.q)

