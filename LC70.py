def climbStairs(n):
    if (n <= 3):
        return n
    else:
        output = [0, 1]
        for i in range(2, n):
            output.append(output[i - 1] + output[i - 2])
        return output[n + 1]


print(climbStairs(2))
print(climbStairs(4))
