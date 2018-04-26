class Queue:
  # Implementing class Queue with methods: isEmpty, enqueue, dequeue, peek, sizeQueue, showQueue
  def __init__(self):
    self.queue = []
  
  def isEmpty(self):
    return self.queue == []

  def sizeQueue(self):
    return len(self.queue)

  def enqueue(self, data):
    self.queue.append(data)

  

queue1 = Queue()
print("Is the queue empty ?", queue1.isEmpty())
print("Queue's size:", queue1.sizeQueue())

queue1.enqueue(1)
queue1.enqueue(2)
queue1.enqueue(3)
queue1.enqueue(4)
queue1.enqueue(5)
print("Is the queue empty ?", queue1.isEmpty())
print("Queue's size:", queue1.sizeQueue())