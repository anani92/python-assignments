from node import Node

class singly_linked_list:
  def __init__(self, value=None):
    self.head = Node(value)

  def get_head_node(self):
    return self.head

  def add_to_front(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head)
    self.head = new_node
    return self

  def add_to_back(self, val):
    if self.head == None:
      self.add_to_front(val)
      return self
    new_node = Node(val)
    current_node = self.head
    while (current_node.next_node != None):
      current_node = current_node.get_next_node()
    current_node.set_next_node(new_node)
    return self

  def print_values(self):
    runner = self.head
    while (runner):
      if runner.value != None:
        print(runner.get_value())
      runner = runner.next_node
    return self

  def remove_from_front(self):
    current_head = self.head
    self.head = current_head.next_node
    return self
  def remove_from_back(self):
    current_node = self.head
    while current_node:
      current_node = current_node.get_next_node()
      if current_node.next_node.next_node == None:
        current_node = current_node.set_next_node(None)
    return self
  def remove_by_value(self, value_to_remove):
    current_node = self.head
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
    while current_node:
      next_node = current_node.get_next_node()
      if next_node.value == value_to_remove:
        current_node.set_next_node(next_node.get_next_node())
        current_node = None
      else:
        current_node = next_node
    return self

my_list = singly_linked_list()
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()
# my_list.remove_from_back().print_values()

my_list.remove_by_value('are').print_values()