def isPalindrome(s: str) -> bool:
    m = s.lower().replace('[^a-zA-Z0-9]', '')
    return m == m[::-1]

def isPalindrome2(s: str):
    m = s.lower().replace('[a-zA-Z0-9]', '')
    return m[::-1]

print(isPalindrome2("A man, a plan, a canal: Panama"))