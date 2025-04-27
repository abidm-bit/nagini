inp1={1,2,2,1}
inp2={2,2}

inp3={4,9,5}
inp4={9,4,9,8,4}


def intersectionm1(nums1, nums2):
   c=nums1.intersection(nums2)
   print(c)

intersectionm1(inp1,inp2)
intersectionm1(inp3,inp4)

print()

def intersectionm2(nums1, nums2):
    return list(set(nums1) & set(nums2))

print(intersectionm2(inp1,inp2))
print(intersectionm2(inp3,inp4))