class Queue:
  # Implementing class Queue with methods: isEmpty, enqueue, dequeue, peek, sizeQueue, showQueue
  def __init__(self):
    self.queue = []
  
  def isEmpty(self):
    return self.queue == []

  def showQueue(self):
    queueWall = "_" * ( 4 * self.sizeQueue() - 2 )
    print(queueWall + "\n")
    for i, v in enumerate(self.queue):
      print(f"{v} ", end="  ") if i < self.sizeQueue() - 1 else print(f"{v} <--")
    print(f"\n{queueWall}\n")

  def sizeQueue(self):
    return len(self.queue)

  def enqueue(self, data):
    self.queue.append(data)
    print(f"adding {data} to the queue:")
    self.showQueue()

  def dequeue(self):
    data = self.queue[0]
    del self.queue[0]
    return data

  def peek(self):
    return self.queue[0]

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

print("Removing", queue1.dequeue(), "from the queue")
print("Queue's size:", queue1.sizeQueue())
print("Removing", queue1.dequeue(), "from the queue")
print("Queue's size:", queue1.sizeQueue())
print("Removing", queue1.dequeue(), "from the queue")
print("Queue's size:", queue1.sizeQueue())

print("peeking:", queue1.peek())