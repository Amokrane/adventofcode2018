class Stack:
  def __init__(self):
    self.__storage = []

  def isEmpty(self):
    return len(self.__storage) == 0

  def push(self,p):
    self.__storage.append(p)

  def pop(self):
    return self.__storage.pop()

  def peek(self):
      return self.__storage[-1]

  def size(self):
      return len(self.__storage)
  
  def __str__(self):
      return str(self.__storage)

