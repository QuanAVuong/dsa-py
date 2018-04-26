class Queue:
  # Implementing class Queue with methods: isEmpty, enqueue, dequeue, peek, sizeQueue, showQueue
  def __init__(self):
    self.queue = []
  
  def isEmpty(self):
    return self.queue == []



queue1 = Queue()
print(queue1.isEmpty())