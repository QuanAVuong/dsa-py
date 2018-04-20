class Node(object):                
  def __init__(self, data):        
    self.data                    = data
    self.nextNode                = None;

class LinkedList(object):          
  def __init__(self):              
    self.head                    = None;
    self.size                    = 0;
  
  # O(1)
  def insertStart(self, data):     
    self.size                   += 1
    newNode                      = Node(data)

    if not self.head:              #            => not None => True; not (self.head object) => False
      self.head                  = newNode;
    else:                          
      newNode.nextNode           = self.head  # => point newNode's nextNode property to current head
      self.head                  = newNode  #   => Make newNode the current head

  # O(1)
  def size(self):                  
    return self.size

  # O(n):                          Traversing the Linkedlist
  def sizeSearch(self):            
    currentNode                  = self.head
    size                         = 0

    while currentNode is not None: 
      size                      += 1
      currentNode                = currentNode.nextNode
    
    return size

  def insertEnd(self, data):
    self.size += 1
    newNode = Node(data)
    currentNode = self.head
