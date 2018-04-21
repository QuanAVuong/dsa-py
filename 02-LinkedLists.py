class Node(object):                
  def __init__(self, data):        
    self.data                    = data
    self.nextNode                = None

class LinkedList(object):          
  def __init__(self):              
    self.head                    = None
    self.size                    = 0
  
  # O(1)
  def insertStart(self, data):     
    self.size                   += 1
    newNode                      = Node(data)

    if not self.head:              #            => not None => True; not (self.head object) => False
      self.head                  = newNode
    else:                          
      newNode.nextNode           = self.head  # => point newNode's nextNode property to current head
      self.head                  = newNode  #   => Make newNode the current head

  # O(1)
  def size1(self):                  
    return f"current size: {self.size}"

  # O(n):                          Traversing the Linkedlist
  def sizeN(self):            
    currentNode                  = self.head
    size                         = 0

    while currentNode is not None: 
      size                      += 1
      currentNode                = currentNode.nextNode
    
    return size

  # O(n):                          Traversing LinkedList
  def insertEnd(self, data):       
    self.size                   += 1
    newNode                      = Node(data)
    currentNode                  = self.head

    while currentNode.nextNode is not None: 
      currentNode                = currentNode.nextNode

    currentNode.nextNode         = newNode

  # O(n):                          Traversing LinkedList  
  def traverseList(self):
    print("Traversing the list and displaying nodes: ")
    currentNode = self.head
    
    i = 1
    while currentNode is not None:
      print(f"node #{i}: {currentNode.data}"
            ," <-- Both Head and Tail" if self.size == 1
            else " <-- Current Head" if i == 1
            else " <-- Current Tail" if currentNode.nextNode == None
            else "" )
      currentNode = currentNode.nextNode
      i += 1
		
    print(currentNode)
  
  def remove(self, data):
    if self.head is None:
      return
    
    self.size           -= 1
    
    # Setting up currentNode / previousNode at the beginning
    currentNode         = self.head
    previousNode        = None

    print(f"\nSearching for node containing `{data}` to remove:")
    while currentNode.data != data:
      print(f"currentNode.data {currentNode.data} != {data}")
      previousNode = currentNode
      currentNode  = currentNode.nextNode if currentNode.nextNode != None else break

    print(f"FOUND! currentNode.data {currentNode.data} == {data} ! Removing `{currentNode.data}`")

    # Removal control flow based on found node's location
    if previousNode is None and currentNode.nextNode is None:
      print(f"The only remaining node: {currentNode.data} is both a head and a tail")
      print(f"Poiting this list's only head to None will clear it.")
      self.head = currentNode.nextNode
    elif previousNode is None:
      print(f"Since previousNode is {previousNode}, currentNode: {currentNode.data} is head. \nPointing new head to old head's nextNode: {currentNode.nextNode.data}")
      self.head = currentNode.nextNode
      print(f"old head is still pointing to nextNode: {currentNode.nextNode.data}")
      currentNode.nextNode = None
      print(f"removed old head's nextNode reference, now pointing to: {currentNode.nextNode}")
    elif currentNode.nextNode is None:
      print(f"currentNode: {currentNode.data} is a tail. No need to remove its nextNode reference that is already pointing to None")
      previousNode.nextNode = currentNode.nextNode
      print(f"previousNode: {previousNode.data} is now the new tail pointing to {previousNode.nextNode}")
    else:
      previousNode.nextNode = currentNode.nextNode
      print(f"currentNode.nextNode is still pointing to nextNode: {currentNode.nextNode.data}")
      currentNode.nextNode = None
      print(f"removed currentNode's nextNode reference, now pointing to: {currentNode.nextNode}")
      

linkedlist = LinkedList()
print(linkedlist)

linkedlist.insertStart(12)
linkedlist.insertStart(122)
linkedlist.insertStart("First Head")
linkedlist.insertEnd(31)
linkedlist.insertEnd(-23.34)
linkedlist.insertEnd("First Tail")

linkedlist.traverseList()
print(linkedlist.size1())

linkedlist.remove("First Head")
linkedlist.traverseList()
print(linkedlist.size1())

linkedlist.remove(12)
linkedlist.traverseList()
print(linkedlist.size1())

linkedlist.remove(-23.34)
linkedlist.traverseList()
print(linkedlist.size1())

linkedlist.remove("WhoAmI")
linkedlist.traverseList()
print(linkedlist.size1())

linkedlist.remove(31)
linkedlist.traverseList()
print(linkedlist.size1())

linkedlist.remove("First Tail")
linkedlist.traverseList()
print(linkedlist.size1())

linkedlist.remove(122)
linkedlist.traverseList()
print(linkedlist.size1())