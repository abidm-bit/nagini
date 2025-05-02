from typing import List

myList = [8,10.7,17.1,11.2,13.5,9.9,14.9,9.4,9.4,3.1,12.7]
size = len(myList)
print(size) # Output: 11

print()

def count_peaks(values: List[float]) -> int:
    nb_peaks = 0
    for i in range(1, len(values)-1):
        if values[i-1]-5>values[i] and values[i+1]-5<values[i]:
            nb_peaks += 1
        elif values[i-1]+5>values[i] and values[i+1]+5<values[i]:
            nb_peaks += 1
    return nb_peaks
print(count_peaks(myList))


count_peaks(myList)
