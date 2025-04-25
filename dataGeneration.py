#Use the Faker library to generate sample data

import pandas as pd
from faker import Faker
f = Faker()

firstName = []
lastName = []

for _ in range(10):
  firstName.append(f.first_name_female())
  lastName.append(f.last_name_female())

#print first names
print(firstName)

#print last names
print(lastName)


# combine the first and last names
names = {firstName[i]:lastName[i] for i in range(10)}
print([names])
df = pd.DataFrame([names])

#  store the generated data in an excel file
#df.to_excel('outputs/names.xlsx',sheet_name='Names',index=False)


"""
I can feed this using TestNG's Data provider as parameters in a test case 
"""