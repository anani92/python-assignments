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
      current_node = current_node.next_node
    current_node.set_next_node(new_node)
    print(current_node.value)
    return self

  def print_values(self):
    runner = self.get_head_node()
    while (runner):
      if runner.get_value() != None:
        print(runner.get_value())
      runner = runner.next_node
    return self

my_list = singly_linked_list()
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()