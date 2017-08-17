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

def getdiseaseLink(alphabet_link):
    diseaseLink_list = []
    for link in alphabet_link:
        driver.get(link)
        elements = driver.find_elements_by_css_selector("body > div.wrap > div.outer-main-body > div > div:nth-child(2) > ul > *")
        for element in elements:
            diseaseLink_list.append([elements[0].find_element_by_css_selector('a').text, element.find_element_by_css_selector('a').get_attribute('href')])
    return diseaseLink_list

def GetDiseaseDetail(link):
    driver.get(link)
    Symptoms_Key = driver.find_element_by_css_selector("#article-info-wrapper-mobile > div > div.col.article-info-details > div.most-common-symptoms > div > ul").text.replace("\n","/")
    Introduction = driver.find_elements_by_css_selector("#mobile-reminder-scroll-thresh > div > div.main-content-col > div:nth-child(3) > *")


if __name__ == "__main__":
    chromeOptions = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images":2}
    chromeOptions.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome('C:\\Users\\ChuyaoShen\\Desktop\\pianzi\\chromedriver.exe', chrome_options=chromeOptions)


    driver = webdriver.Chrome('C:\\Users\\ChuyaoShen\\Desktop\\pianzi\\chromedriver.exe')
    alphabet_link = getablink()  

    diseaseLink_list = getdiseaseLink(alphabet_link)

    clean_data = pd.DataFrame(columns = ["Category", "ID", "Disease", "Symptoms_Key", "Introduction", "Symptoms_Detailed", "Causes", "Diagnosis", "Treatment", "Recovery", "Cost"])
    for i in diseaseLink_list:
        Category = "dog"
        ID = i
        Disease = diseaseLink_list[i][0]
        [Symptoms_Key, Introduction, Symptoms_Detailed, Causes, Diagnosis, Treatment, Recovery, Cost] = GetDiseaseDetail(diseaseLink_list[i][1])
