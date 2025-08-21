" leetcode 367 , determine if a number is a perfect square number"


def isPerfectSquare(num: int) -> bool:
    return pow(num, 0.5) % 1 == 0

print(isPerfectSquare(14))
print(isPerfectSquare(16))
print(isPerfectSquare(100))