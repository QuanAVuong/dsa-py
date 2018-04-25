class Stack:
  def __init__(self):
    self.stack = []

  def isEmpty(self):
    return self.stack == []

  def showStack(self, operation=""):
    for i, v in enumerate(self.stack):
      if i == 0 and operation == "push": 
        print("|___|" if self.sizeStack() == 1 else "|   |", f"<-- {self.stack[-i-1]}")
      elif i == 0 and operation == "pop": 
        print(f"|   | --> {self.stack[-1]}")
      elif i < len(self.stack)-1:
        print(f"| {self.stack[-i-1]} |")
      else:
        print(f"|_{self.stack[-i-1]}_|")

  def sizeStack(self):
    return len(self.stack)
  
  def push(self, data):
    self.stack.append(data)
    print(f"pushing {data} to the stack: ", f"( list view: {self.stack} )")
    self.showStack("push")

  def pop(self):
    data = self.stack[-1]
    print(f"Popped last item {data} from stack:  (list view: {self.stack} )")
    self.showStack("pop")
    del self.stack[-1]
    return data
    # return self.stack.pop()

  def peek(self):
    return self.stack[-1]

    
stack1 = Stack()
stack1.push(1)
stack1.push(2)
stack1.push(3)
stack1.push(4)
stack1.push(5)
print("Stack's size:", stack1.sizeStack())

stack1.pop()
stack1.pop()
print("Stack's size:", stack1.sizeStack())

print(f"Peeking...(  ~  .o) | {stack1.peek()} |")