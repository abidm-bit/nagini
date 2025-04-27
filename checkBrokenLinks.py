import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

def find_broken_links(url):
    driver = webdriver.Chrome()
    driver.get(url)

    links = driver.find_elements(By.CSS_SELECTOR,"#broken-links a")

    broken_links = []

    for link in links:
        href = link.get_attribute("href")
        if href:
            try:
                response = requests.head(href)
                if response.status_code != 200:
                    broken_links.append(href)
            except requests.exceptions.RequestException:
                broken_links.append(href)

    driver.quit()
    return broken_links

if __name__ == "__main__":
    url = "https://testautomationpractice.blogspot.com/"
    broken_links = find_broken_links(url)

    if broken_links:
        print("Broken links found:")
        for link in broken_links:
            print(link)
    else:
        print("No broken links found.")

find_broken_links("https://testautomationpractice.blogspot.com/")