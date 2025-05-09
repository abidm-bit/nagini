from typing import List


def FizzBuzz(number):
    for i in range(1,number):
        if i % 3 == 0 and i % 5 == 0: print("FizzBuzz")
        elif i % 5 == 0: print("Fizz")
        elif i % 3 == 0: print("Buzz")
        else : print(i)

def FizzBuzz2(number):
    x = []
    for i in range(1,number):
        if i % 3 == 0 and i % 5 == 0: x.append("FizzBuzz")
        elif i % 5 == 0: x.append("Fizz")
        elif i % 3 == 0: x.append("Buzz")
        else : x.append(i)
    print(x)

# LC412 FizzBuzz
def fizzBuzzLC(n: int) -> List[str]:
    y=[]
    for i in range(1,n+1):
        if i % 15 == 0: y.append("FizzBuzz")
        elif i % 5 == 0: y.append("Buzz")
        elif i % 3 == 0: y.append("Fizz")
        else: y.append(str(i))
    return y

FizzBuzz2(15)
# FizzBuzz(15)
print(fizzBuzzLC(15))