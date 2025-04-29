from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Uploading a file using Selenium Python is faster than uploading a file using Selenium Java

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options)
driver.get("https://demoqa.com/upload-download")
file_input = driver.find_element(By.CSS_SELECTOR,"#uploadFile")
file_input.send_keys("/Users/mabid/PycharmProjects/PythonProject/resource/dash.jpg")
