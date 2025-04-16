# Question from ChatGpt

# 🧩 Problem Statement:
# You are given an empty array of size 100 (initialized with 0). Write a Python program to:

# Insert n integers into the array one by one.
# Delete the element at a given index k.
# Print the final array elements (only valid elements).

# 👉 Note:
# You should not use append() or remove().
# You must shift elements manually like in C.
# Handle invalid k gracefully.

# 🎯 Input Format:
# n = 5
# elements = [10, 20, 30, 40, 50]
# k = 2

# 🧾 Expected Output:
# 10 20 40 50


class Array:
    def __init__(self, max_size = 100): # Size 100 given
        self.arr = [None for i in range(100)]
        self.max_size = max_size
        self.current_size  = 0

    def insert(self, ele, index):
        if self.max_size <= self.current_size:
            raise IndexError
        
        # insert_at = self.current_size + 1 # in c with adress it will be "start_location + given_index*4 + 4 "
        if index > self.max_size - 1:
            raise IndexError
        
        if index > self.current_size:
            raise IndexError("Cannot insert at index beyond current size")

        
        for element in range(self.current_size, index,-1):
            self.arr[element] = self.arr[element - 1] 
 
        self.arr[index] = ele
        self.current_size += 1
    
    def delete(self, k):
        if k >= self.current_size or k < 0:
            raise IndexError("Invalid delete position")


        for element in range(k, self.current_size - 1):
            self.arr[element] = self.arr[element + 1] 
        
        self.current_size -= 1

    def __str__(self):
        return ' '.join(str(self.arr[i]) for i in range(self.current_size))
    
if __name__ == "__main__":
    chatgpt = Array() # maxsize 100 by defualt
    for i in range(100):
        chatgpt.insert(i*i,i)
    print(chatgpt)
