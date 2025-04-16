# Inplace reversal is O(n) in time & O(1) in space

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def right_rotate(arr, k):
    n = len(arr)
    k %= n
    reverse(arr, 0, n - 1)
    reverse(arr, 0, k - 1)
    reverse(arr, k, n - 1)
    return arr

def left_rotate(arr, k):
    n = len(arr)
    k %= n
    reverse(arr, 0, k - 1)
    reverse(arr, k, n - 1)
    reverse(arr, 0, n - 1)
    return arr

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    # arr[:] - non referencial copy of arr so return is needed in the function
    # if arr is given then the chnages will be direcly made in the original arrray 
    print(right_rotate(arr[:], 3))  # output [4, 5, 1, 2, 3] 
    # print(left_rotate(arr[:], 2))   # output [3, 4, 5, 1, 2]
