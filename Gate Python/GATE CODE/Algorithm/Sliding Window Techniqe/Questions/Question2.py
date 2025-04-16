# Q. Count how many times a pattern appears as a substring in a given string.

# ✅ Input Format
# s = "ababcabcab"
# pattern = "abc"

# 📤 Expected Output
# 2

def sub_string_finder(string, sub) -> int:
    n = len(string)
    m = len(sub)
    
    count = 0
    for i in range(m,n+1):
        window_str = string[i-m:i]
        if window_str == sub:
            count += 1
    return count

if __name__ == '__main__':
    string = "akaakaakaakaaka"
    sub = "aka"
    print(sub_string_finder(string, sub))
