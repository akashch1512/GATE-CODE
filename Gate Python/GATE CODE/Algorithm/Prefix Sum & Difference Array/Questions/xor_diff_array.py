# Question 1 from https://youtu.be/96RG7EBF8LI?si=WiUHPDsqOVsS46bQ

def diff_XOR(diff, l, r, x):
    diff[l] ^= x # add differneces to array here start point 
    if r + 1 < len(diff): # checks if not r+1 is  the rigth  element  is end most elemet 
        diff[r + 1] ^= x # sets last element as end point at r+1


# Original array
arr = [0 for i in range(1, 10)]  # [1, 2, 3, ..., 9]
n = len(arr) # 
diff = [0] * (n + 1) # creates the array length of n=1 ( +! to handle end condtion )

# Perform K operations (still O(K))
operations = [
    (1, 2, 3), # [1to8] sqare bracket
    (1, 3, 1), # [2to5] sqare bracket 
    # (0, 3, 2), # [0to3] sqare bracket
]
for l, r, x in operations:
    diff_XOR(diff, l, r, x) # creates the differences in the 0 arrray so prefix array can be runned

# Single loop: prefix sum + applying updates to arr

ele = 0
for i in range(n-1): 
    ele ^= diff[i] # gets the XOR of that elemet one by one and put it to prefix 
    arr[i] ^= ele # prefix adds the all addstion until this into currunt array

print(arr)
