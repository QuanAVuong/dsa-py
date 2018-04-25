class Stack:
  def __init__(self):
    self.stack = []

  def isEmpty(self):
    return self.stack == []

  def showStack(self):
    # [print(f"| {self.stack[-i-1]} |") if i < len(self.stack)-1 else print(f"|_{self.stack[-i-1]}_|") for i, v in enumerate(self.stack)]
    for i, v in enumerate(self.stack):
      if i == 0: 
        print(f"| {self.stack[-i-1]} | <--")
      elif i < len(self.stack)-1:
        print(f"| {self.stack[-i-1]} |")
      else:
        print(f"|_{self.stack[-i-1]}_|")
        
      # switcher           = {
      #   0:                print(f"| {self.stack[-i-1]} | <--"),
      #   # len(self.stack)-1: print(f"|_{self.stack[-i-1]}_|"),
      # }
      # switcher.get(i)

  def sizeStack(self):
    return f"Stack's size: {len(self.stack)}"
  
  def push(self, data):
    self.stack.append(data)
    print(f"pushed {data} to the stack: ", f"( list view: {self.stack} )")
    self.showStack()

  def pop(self):
    # data = self.stack[-1]
		# del self.stack[-1]
		# return data
      
    return self.stack.pop()

  def peek(self):
    return self.stack[-1]

    
stack1 = Stack()
stack1.push(1)
stack1.push(2)
stack1.push(3)
stack1.push(4)
stack1.push(5)
print(stack1.sizeStack())
# print("Popped: ", stack1.pop())
# print("Popped: ", stack1.pop())
# print(stack1.sizeStack())
# print("Peek:", stack1.peek())
# print(stack1.sizeStack())