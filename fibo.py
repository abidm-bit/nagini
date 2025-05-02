
#       numb: numbers to print in the fibonacci sequence

def fiboSequence(numb):
    output=[0,1]
    for i in range(2,numb):
        output.append(output[(i-1)]+(output[i-2]));
    print(output)

fiboSequence(7) # thats a spike
print()
fiboSequence(8)
print()
fiboSequence(9) # breakdown game, 8 mile fame
