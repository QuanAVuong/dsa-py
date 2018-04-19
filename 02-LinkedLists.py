class Node(object):
  def __init__(self, data):
    self.data     = data
    self.nextNode = None;

class LinkedList(object):
  def __init__(self):
    self.head = None;
    self.size = 0;
  
  def insertStart(self, data):
    self.size += 1
    newNode = Node(data)

    if not self.head: # not None => True; not (self.head object) => False
      self.head = newNode;
    else: 
      newNode.nextNode = self.head      # point newNode's nextNode property to current head
      self.head = newNode     # Make newNode the current head

  def size(self):
    return self.size