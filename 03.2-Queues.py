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
print(queue1.isEmpty())

queue1.enqueue(1)
queue1.enqueue(2)
queue1.enqueue(3)
queue1.enqueue(4)
queue1.enqueue(5)
print(queue1.isEmpty())