def is_palindrome(x: int) -> bool:
    s = str(x)
    return s == s[::-1]


print(is_palindrome(121))
print(is_palindrome(-121))