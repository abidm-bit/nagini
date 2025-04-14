
# palindrome 


y = "civic"
x = y[::-1]

if (y==x): print("ya this is a palindrome")
else: print("nop this is not a palindrome")
    
    #shorthand if/else "ternary":
print("ya "+ str(y)+" is a palindrome") if (y==x) else print("nop "+ str(x)+" is not a palindrome")


a = "radar"
b = a[::-1]
print("ya "+ str(a)+" is a palindrome") if (a==b) else print("nop "+ str(a)+ " is not a palindrome")



m = 2002
m= str(m)
a = m[::-1]
print("ya " + str(m) +" is a palindrome") if (m==a) else print("nop "+ str(m)+" is not a palindrome")


y = 3005
y= str(y)
n = y[::-1]
print("ya "+ str(y)+  " is a palindrome") if (y==n) else print("nop "+ str(y)+" is not a palindrome")



def isPalindrome(x):
    if(str(x)==(str(x)[::-1])):print(str(x) + " iz a palindrome")
    else:print(str(x)+" iz not a palindrome" )
        
isPalindrome("radar")
isPalindrome("cat")
isPalindrome("lol")


def isPalindromee(x):
    if(str(x)==(str(x)[::-1])):print(True)
    else: print(False)
        
isPalindromee("wow")
isPalindromee("3005")
isPalindromee("1001")