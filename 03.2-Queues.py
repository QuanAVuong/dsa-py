class Queue:
  # Implementing class Queue with methods: isEmpty, enqueue, dequeue, peek, sizeQueue, showQueue
  def __init__(self):
    self.queue = []
  
  def isEmpty(self):
    return self.queue == []

  def enqueue(self, data):
    self.queue.append(data)

queue1 = Queue()
print(queue1.isEmpty())