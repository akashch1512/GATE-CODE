# Q. Find the length of the longest substring that contains at most K distinct characters.

# ✅ Input Format
# s = "eceba"
# k = 2

# 📤 Expected Output
# 3

# 💡 Explanation:

# "ece" has 2 distinct characters (e and c) → length = 3

# "ceba" has 3 distinct → invalid

# So max = 3

def distinct_char_finder(string, k):
    s = set()
    count = 0
    max_count = float('-inf')
    for i in string:
        if not i in s:
            s.add(i)
            count += 1
        else:
            max_count = max(max_count, count)
    
    
    return max(max_count, count)

if __name__ == '__main__':
    print(distinct_char_finder("aka",2))