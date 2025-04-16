def prefix_sum(arr, l ,r):
    prefix = [0]*(r-l)

    prefix[0] = arr[l]
    for i,k in enumerate(range(l+1, r),start=1):
        prefix[i] = prefix[i-1] + arr[k]
    return prefix

# if __name__ == "__main__":
#     arr = [ ele*10 for ele in range(1, 11) ]
#     print(arr)
#     print(prefix_sum(arr[:], 3, 6))


n = 6
diff = [0]*n

# Add +10 to range [1, 3]
diff[1] += 10
if 4 < n:
    diff[4] -= 10

# Add +5 to range [2, 5]
diff[2] += 5
if 6 < n:
    diff[6] -= 5

# Final array using prefix sum
for i in range(1, n):
    diff[i] += diff[i-1]

print(diff)  # Final updated values
