# LC58: Length of Last Word
# Given a string s consisting of words and spaces, return the length of the last word in the string.


def lengthOfLastWord(s):
    x=s.split()
    return len(x[-1])

print(lengthOfLastWord('hello world'))
print(lengthOfLastWord('   fly me   to   the moon  '))
print(lengthOfLastWord('luffy is still joyboy'))