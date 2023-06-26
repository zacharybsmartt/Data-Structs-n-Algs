print("test")

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self):
        # we create the head node, this is the crux of linked list
        self.head = None
