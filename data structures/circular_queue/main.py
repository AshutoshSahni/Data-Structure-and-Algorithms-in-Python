
class CircularQueue:
    def __init__(self, max):
        self.max = max
        self.queue = [None] * max
        self.front = self.rear = -1

    # insert element into circular queue
    def enqueue(self, data):
        if (self.rear + 1) % self.max == self.front:
            print("ERROR: Overflow!")
        elif self.front == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear + 1) % self.max
            self.queue[self.rear] = data

    # delete element from circular queue
    def dequeue(self):
        if self.front == -1:
            print("ERROR: Underflow!")
        elif self.front == self.rear:
            temp = self.queue[self.front]
            self.front = self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.max
            return temp

    # display circular queue
    def display_queue(self):
        if self.front == -1:
            print("Queue is EMPTY!")
        else:
            while self.front <= self.rear:
                print(self.queue[self.front], end=" ")
                self.front = (self.front + 1) % self.max


# main
if __name__ == '__main__':
    c = CircularQueue(8)
    c.enqueue(3)
    c.enqueue(5)
    c.enqueue(9)
    c.enqueue(21)
    c.dequeue()
    c.display_queue()
