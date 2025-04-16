def stack_using_list():
    # Stack using Python's list
    print("Stacks using Python's list")
    stack_list = []
    
    stack_list.append(10)  # Inserts an element into the stack
    stack_list.append(30)
    stack_list.append(40)

    size = len(stack_list)
    print(size)

    print(stack_list)

    print(stack_list.pop())  # Pops out the element in LIFO order
    print(stack_list.pop())
    print(stack_list.pop())

    print(stack_list)

# ✅ Fast push & pop (O(1))
# ✅ Dynamically resizable
# ❌ Not thread-safe in multithreading
# ❌ No built-in size limit

def stack_using_collection_module():
    # Stack using collections.deque
    print("\nStacks using inbuilt function collections.deque")
    from collections import deque

    stack_coll = deque()

    stack_coll.append(10)  # Insert an element into the stack
    stack_coll.append(20)

    print(stack_coll)
    print(stack_coll.pop())  # Remove an element from the stack
    print(stack_coll.pop())
    print(stack_coll)

# ✅ Thread-safe (useful in multithreading)
# ✅ Optimized for stack operations
# ❌ Slightly slower due to internal locking mechanisms

def stack_using_queue_module():
    # Stack using queue.LifoQueue module
    print("\nStack using queue.LifoQueue module")
    from queue import LifoQueue

    stack_queue = LifoQueue(maxsize=10)  # Initialize stack with max size

    stack_queue.put(10)  # Insert an element
    stack_queue.put_nowait(20)  # Insert an element without waiting
    
    print(stack_queue.empty())  # Checks if empty
    print(stack_queue.full())  # Checks if full
    
    print(stack_queue.get())  # Removes element (waits if empty)
    print(stack_queue.get_nowait())  # Removes element (raises error if empty)
    
    print(stack_queue.qsize())  # Returns stack size

# ✅ Thread-safe
# ✅ Built-in maxsize control
# ❌ Slightly slower due to internal locking
# ❌ No direct element access

# Node class for Linked List Stack
class Node:
    def __init__(self, value):
        self.value = value  # Store value
        self.next = None  # Pointer to the next node

# Stack class using Linked List
class Stack:
    def __init__(self):
        self.top = None  # Points to the top node (initially empty)
        self.size = 0  # Track number of elements

    def __str__(self):
        cur = self.top
        out = ""
        while cur:
            out += str(cur.value) + " -> "
            cur = cur.next
        return out[:-4] if out else "Stack is empty"

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.top is None

    def peek(self):
        if self.isEmpty():
            return None  # Stack is empty
        return self.top.value

    def push(self, value):
        node = Node(value)  # Create a new node
        node.next = self.top  # New node points to current top
        self.top = node  # Update top to new node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack underflow! Cannot pop from an empty stack")
        remove = self.top  # Store the top node
        self.top = self.top.next  # Move top pointer
        self.size -= 1
        return remove.value  # Return removed value

# Driver Code
if __name__ == "__main__":
    print("\nUsing Stack with Linked List:")
    stack = Stack()

    for i in range(1, 6):
        stack.push(i)
    print(f"Stack after pushing: {stack}")

    for _ in range(3):  # Pop 3 times
        popped_value = stack.pop()
        print(f"Popped: {popped_value}")
    
    print(f"Stack after popping: {stack}")

    # Call different stack implementations
    stack_using_list()
    stack_using_collection_module()
    stack_using_queue_module()
