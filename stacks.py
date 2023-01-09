class Stack:
  def __init__(self):
    self.items = []

  def push(self, item):
    self.items.append(item)

  def pop(self):
    return self.items.pop()

  def display(self):
    print(self.items)

  def is_empty(self):
    return self.items == []

  def peek(self):
    if not is_empty():
      print(self.items[-1])


