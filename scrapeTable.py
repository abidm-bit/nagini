# Scrape a webtable using Python & Selenium (parse & extract data)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
from tabulate import tabulate

options = Options()
options.add_argument("-headless")
driver = webdriver.Chrome(options)
driver.get("https://www.w3schools.com/html/html_tables.asp")

#   stored headers
tblhdr = driver.find_elements(By.CSS_SELECTOR, "#customers tbody tr th")
headers = []
[headers.append(a.text) for a in tblhdr]
headers.insert(0,"#")

#   stored companies
company = driver.find_elements(By.CSS_SELECTOR, "#customers tbody tr td:nth-of-type(1)")
companies =[]
[companies.append(z.text) for z in company]

#   stored contacts
contact = driver.find_elements(By.CSS_SELECTOR, "#customers tbody tr td:nth-of-type(2)")
contacts =[]
[contacts.append(y.text)for y in contact]

#   stored countries
country= driver.find_elements(By.CSS_SELECTOR, "#customers tbody tr td:nth-of-type(3)")
countries = []
[countries.append(x.text) for x in country]

for lmnt in companies: print(lmnt)
print("\n")
for lmnt2 in contacts: print(lmnt2)
print("\n")
for lmnt3 in countries: print(lmnt3)


whole_table= {'Companies':companies, 'Contacts':contacts, 'Countries':countries}
df= pd.DataFrame(whole_table)
print(tabulate(df,headers,tablefmt='psql'))

""" 
# store in an excel sheet
df.to_excel('outputs/output.xlsx',sheet_name='W3 Schools HTML Table',index=False)

# store in a csv file , index=False won't print the #
df.to_csv('outputs/W3Tableoutput.csv',index=False)
driver.quit
"""