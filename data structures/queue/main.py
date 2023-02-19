# Name              :   Queue Data Structure
# Version           :   Python 3.x
# Description       :   Implementation of Stack
# Time Complexity   :   For Array/List based implementation O(1)

class Queue:
    # create a queue
    def __init__(self):
        self.queue = []

    # insert into queue
    def enqueue(self, data):
        self.queue.append(data)
        print(data, "inserted to queue")

    # remove element from queue
    def dequeue(self):
        if len(self.queue) == 0:
            print("ERROR: Underflow")
        else:
            self.queue.pop(0)
            print("element removed!")

    # display queue
    def display_queue(self):
        print(self.queue)

    # is queue empty?
    def is_empty(self):
        if len(self.queue) == 0:
            print("Queue is EMPTY")
        else:
            print("Queue is not empty")

    # peek
    def get_peek(self):
        return self.queue[len(self.queue) - 1]


# main
if __name__ == '__main__':
    q = Queue()
    q.enqueue(4)
    q.enqueue(23)
    q.enqueue(8)
    q.enqueue(2)
    q.dequeue()
    q.display_queue()
    print(q.get_peek())
    q.is_empty()
