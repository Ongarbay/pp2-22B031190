def palindrome(s):
    t = s[::-1]
    if t == s:
        return True
    return False

print("Enter string to check:")
s = input()
print(palindrome(s))
