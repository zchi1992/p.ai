from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from string import ascii_uppercase

def getablink():
    link_list = []
    for alphabet in ascii_uppercase:
        link_list.append("https://www.vetary.com/dog/conditions/" + alphabet)
    return link_list

def getdiseaseLink():
    diseaseLink_list = []
    for link in alphabet_link:
        driver.get(link)
        elements = driver.find_elements_by_css_selector("body > div.wrap > div.outer-main-body > div > div:nth-child(2) > ul > *")
        for element in elements:
            diseaseLink_list.append([elements[0].find_element_by_css_selector('a').text, element.find_element_by_css_selector('a').get_attribute('href')])
    return diseaseLink_list

if __name__ == "__main__":
    chromeOptions = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images":2}
    chromeOptions.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome('Z:\\WebDriver\\chromedriver.exe', chrome_options=chromeOptions)

    alphabet_link = getablink()  

    diseaseLink_list = getdiseaseLink(alphabet_link)
