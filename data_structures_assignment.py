from collections import deque

class Node:
    '''A single node in a linked list.'''

    def __init__(self, value):
        self.value = value # The data this node holds
        self.next = None # Reference to the next node (none = end of chain)

    def __repr__(self):
        return f"Node ({self.value})"
    
class LinkedList:
    '''A singly linked list.'''

    def __init__(self):
        self.head = None # The list starts empty => No nodes yet

    def insert_at_beginning(self, value):
        '''Add a new node at the front of the list O(1) time'''
        new_node = Node(value)
        new_node.next = self.head # New node points to the old head
        self.head = new_node # New node becomes the new head

    def insert_at_end(self, value):
        '''Add a new node at the end of list O(n) time - must walk to the end.'''
        new_node = Node(value)
        if self.head is None: #if the list is empty, new node is the head
            self.head = new_node
            return
        current = self.head
        while current.next: # Walk through to the last node
            current = current.next
        current.next = new_node # Last node now prints to the new node

    def display(self):
        '''Prints the list in a readable format.'''
        elements = []
        current = self.head
        while current:
            elements.append(str(current.value))
            current = current.next
        print(" ->" .join(elements) + " -> None")

    def search(self, target):
        '''Find a value in the list. Return True/False. O(n) time.'''
        current = self.head
        while current:
            if current.value == target:
                return True
            current = current.next

    def delete(self, target):
        """Remove the first node with the given value. Return True if found, False if not."""
        current = self.head

        if not current: # Check to see if the list is empty
            return False 
        
        if current.value == target: # Checks the first node to see if it matches the target, if not, removes current head and moves to next node
            self.head = current.next
            return True
        
        prev = None
        while current and current.value != target: # Loop through the list while the current value is not equal to the target value
            prev = current
            current = current.next

        if not current: # If the target is not found in the list, return False
            return False

        prev.next = current.next # When a target node is found, relink the previous node to the current node effectively removing the target node from the list
        return True

    def length(self):
        """Return the number of nodes in the list. O(n) time."""
        count = 0
        current = self.head

        while current is not None:
            count += 1
            current = current.next

        return count
    
    def to_list(self):
        """Convert the linked list to a Python list. Returns a list of values."""
        python_list = []
        current = self.head

        while current:
            python_list.append(current.value)
            current = current.next

        return python_list

ll = LinkedList()
for val in [10, 20, 30, 40, 50]:
    ll.insert_at_end(val)

ll.display()           # 10 -> 20 -> 30 -> 40 -> 50 -> None
print(ll.length())     # 5
ll.delete(30)
ll.display()           # 10 -> 20 -> 40 -> 50 -> None
print(ll.to_list())    # [10, 20, 40, 50]

def is_balanced(text):
    """Return True if all brackets in text are properly matched. Handles: (), [], {}"""
    # Define the rules using a Dictionary for matching brackets
    rules = { 
        "]": "[",
        "}": "{",
        ")": "("
    }


    stack = [] # Create an empty stack
    openings = set(["[","{","("]) # Define open brackets

    for ch in text: #Loop through each character in the text
        if ch in openings: # Starts by checking to see if character is in the openings set
            stack.append(ch) # Adds it to the stack if it is 
        elif ch in rules: # Then checks to see if the character is in rules, so it would ignore all other characters
            if not stack: # If the stack is empty, return False
                return False
            last_open = stack.pop() # Defines the last open bracket by using .pop() to take the last character in 
            if last_open != rules[ch]: # Checks to see if the last open is not equal to it's equivalent as defined by the rules
                return False

    return len(stack) == 0 # If the length of the stack gets to 0, it can finally return true because all of the pairs were found

# Tests:
print(is_balanced("()"))           # True
print(is_balanced("({[]})"))       # True
print(is_balanced("(]"))           # False
print(is_balanced("([)]"))         # False
print(is_balanced("hello (world)")) # True

class TaskProcessor:
    """Simple FIFO task queue backed by deque."""

    def __init__(self):
        self.queue = deque()

    def add_task(self, name):
        """Add a task to the end of the queue."""
        self.queue.append(name)

    def process_next(self):
        """Process and return the next task in FIFO order."""
        if not self.queue:
            return None
        return self.queue.popleft()

    def pending_count(self):
        """Return the number of tasks waiting to be processed."""
        return len(self.queue)


def test_task_processor():
    processor = TaskProcessor()

    # Empty queue behavior
    assert processor.process_next() is None
    assert processor.pending_count() == 0

    # FIFO ordering
    processor.add_task("task-1")
    processor.add_task("task-2")
    processor.add_task("task-3")

    assert processor.pending_count() == 3
    assert processor.process_next() == "task-1"
    assert processor.process_next() == "task-2"
    assert processor.pending_count() == 1
    assert processor.process_next() == "task-3"
    assert processor.process_next() is None
    assert processor.pending_count() == 0


test_task_processor()
print("TaskProcessor tests passed")


