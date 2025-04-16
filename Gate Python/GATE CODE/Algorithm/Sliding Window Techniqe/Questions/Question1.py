# Q. Find the maximum sum of a subarray of size k.
# 📥 Input: arr = [1, 4, 2, 10, 23, 3, 1, 0, 20], k = 4
# 📤 Output: 39 (from subarray [10, 23, 3, 1])

def max_sum(arr, k):
    n = len(arr)
    window_sum = sum(arr[:k]) # [0,k)
    max_sum = window_sum
    for i in range(k, n):
        window_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum, window_sum)
    return max_sum

if __name__ == '__main__':
    arr = [i*i for i in range(0,10)]
    print(arr)
    print(max_sum(arr[:], k=2))