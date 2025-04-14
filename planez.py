
planes =["SR71","B2","787","SR72"]
output = []
for x in planes:
    if("7" in x):output.append(x)
print (output)

print("\n")

output2=[]
for model in planes:
    if model.__contains__("7"):output2.append(model);
print(output2)