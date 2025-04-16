# only for left rotation

def left_rotate(arr, k):
    n = len(arr)
    k = k % n  # In case k > n
    return arr[k:] + arr[:k]

if __name__ == "__main__":
    arr = [1 , 2, 3, 4, 5]
    print(left_rotate(arr, k = 2))