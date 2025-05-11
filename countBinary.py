def CountBinary(biNum):
    onez = biNum.count("1")
    zeroez = biNum.count("0")
    print("there are "+ str(onez) + " ones")
    print("there are "+ str(zeroez) + " zeros")

CountBinary("110110001100111000110000101101000")

"""
there are 15 ones
there are 18 zeros
"""