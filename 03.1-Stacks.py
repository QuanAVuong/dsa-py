class Stack:
  def __init__(self):
    self.stack = []

  def isEmpty(self):
    return self.stack == []

  def push(self, data):
    self.stack.append(data)