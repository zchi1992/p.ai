from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from string import ascii_uppercase
import time
import pandas as pd

def unicodetoascii(text):
    uni2ascii = {
            ord('\xe2\x80\x99'.decode('utf-8')): ord("'"),
            ord('\xe2\x80\x9c'.decode('utf-8')): ord('"'),
            ord('\xe2\x80\x9d'.decode('utf-8')): ord('"'),
            ord('\xe2\x80\x9e'.decode('utf-8')): ord('"'),
            ord('\xe2\x80\x9f'.decode('utf-8')): ord('"'),
            ord('\xc3\xa9'.decode('utf-8')): ord('e'),
            ord('\xe2\x80\x9c'.decode('utf-8')): ord('"'),
            ord('\xe2\x80\x93'.decode('utf-8')): ord('-'),
            ord('\xe2\x80\x92'.decode('utf-8')): ord('-'),
            ord('\xe2\x80\x94'.decode('utf-8')): ord('-'),
            ord('\xe2\x80\x94'.decode('utf-8')): ord('-'),
            ord('\xe2\x80\x98'.decode('utf-8')): ord("'"),
            ord('\xe2\x80\x9b'.decode('utf-8')): ord("'"),
            ord('\xe2\x80\x90'.decode('utf-8')): ord('-'),
            ord('\xe2\x80\x91'.decode('utf-8')): ord('-'),
            ord('\xe2\x80\xb2'.decode('utf-8')): ord("'"),
            ord('\xe2\x80\xb3'.decode('utf-8')): ord("'"),
            ord('\xe2\x80\xb4'.decode('utf-8')): ord("'"),
            ord('\xe2\x80\xb5'.decode('utf-8')): ord("'"),
            ord('\xe2\x80\xb6'.decode('utf-8')): ord("'"),
            ord('\xe2\x80\xb7'.decode('utf-8')): ord("'"),
            ord('\xe2\x81\xba'.decode('utf-8')): ord("+"),
            ord('\xe2\x81\xbb'.decode('utf-8')): ord("-"),
            ord('\xe2\x81\xbc'.decode('utf-8')): ord("="),
            ord('\xe2\x81\xbd'.decode('utf-8')): ord("("),
            ord('\xe2\x81\xbe'.decode('utf-8')): ord(")"),
                            }
    return text.decode('utf-8').translate(uni2ascii).encode('ascii','ignore')

def saveTxt(content,animal,d_name):
    path = "C:\\Users\\ChuyaoShen\\Desktop\\pianzi\\Pet\\Vetarycom\\HTML\\"+animal+"_"+d_name+".txt"
    text_file = open(path,"w")
    text_file.write(content.encode('utf-8'))
    text_file.close()

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
            diseaseLink_list.append([element.find_element_by_css_selector('a').text, element.find_element_by_css_selector('a').get_attribute('href')])
    return diseaseLink_list

def GetDiseaseDetail(driver):
    Symptoms_Key = unicodetoascii(driver.find_element_by_css_selector("#article-info-wrapper-mobile > div > div.col.article-info-details > div.most-common-symptoms > div > ul").text.encode('utf-8').replace("\n","/"))
    Introduction = unicodetoascii(driver.find_element_by_css_selector("#mobile-reminder-scroll-thresh > div > div.main-content-col > div:nth-child(3)").text.encode('utf-8').split('\n',1)[1])
    try:
        Symptoms_Detailed1 = unicodetoascii(driver.find_element_by_css_selector("#symptoms-target > div.section-body").text.encode('utf-8'))
    except Exception:
        Symptoms_Detailed1 = ""
    try:
        Symptoms_Detailed2 = unicodetoascii(driver.find_element_by_css_selector("#symptoms-target > div.section-body > ul").text.encode('utf-8'))
    except Exception:
        Symptoms_Detailed2 = ""
    try:
        Causes = unicodetoascii(driver.find_element_by_css_selector("#causes-target > div.section-body").text.encode('utf-8'))
    except Exception:
        Causes = ""
    try:
        Diagnosis = unicodetoascii(driver.find_element_by_css_selector("#diagnosis-target > div.section-body").text.encode('utf-8'))
    except Exception:
        Diagnosis = ""
    try:
        Treatment = unicodetoascii(driver.find_element_by_css_selector("#treatment-target > div.section-body").text.encode('utf-8'))
    except Exception:
        Treatment = ""
    try:
        Recovery = unicodetoascii(driver.find_element_by_css_selector("#recovery-target > div.section-body").text.encode('utf-8'))
    except Exception:
        Recovery = ""
    try:
        Cost = unicodetoascii(driver.find_element_by_css_selector("#cost-target > div.section-body").text.encode('utf-8'))
    except Exception:
        Cost = ""
    return [Symptoms_Key, Introduction, Symptoms_Detailed1, Symptoms_Detailed2, Causes, Diagnosis, Treatment, Recovery, Cost]

def wait(driver, sec):
    find = False
    st = time.time()
    while(not find):
        if(time.time() - st > sec):
            driver.refresh()
            st = time.time()
            print "refreshing ... "
        try:
            Symptoms_Key = driver.find_element_by_css_selector("#article-info-wrapper-mobile > div > div.col.article-info-details > div.most-common-symptoms > div > ul")
                                                                #article-info-wrapper-mobile > div > div.col.article-info-details > div.most-common-symptoms > div > ul
        except Exception:
            continue
        find = True
        time.sleep(1)

if __name__ == "__main__":
    chromeOptions = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images":2}
    chromeOptions.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome('C:\\Users\\ChuyaoShen\\Desktop\\pianzi\\chromedriver.exe', chrome_options=chromeOptions)

    alphabet_link = getablink()  
    diseaseLink_list = getdiseaseLink(alphabet_link)

    clean_data = pd.DataFrame(columns = ["Category", "ID", "Disease", "Symptoms_Key", "Introduction", "Symptoms_Detailed1", "Symptoms_Detailed2", "Causes", "Diagnosis", "Treatment", "Recovery", "Cost"])
    for i in range(1654, len(diseaseLink_list)):
        Category = "dog"
        ID = i
        Disease = diseaseLink_list[i][0]
        print i,Disease
        driver.get(diseaseLink_list[i][1])
        wait(driver, 10)
        [Symptoms_Key, Introduction, Symptoms_Detailed1, Symptoms_Detailed2, Causes, Diagnosis, Treatment, Recovery, Cost] = GetDiseaseDetail(driver)
        clean_data.loc[len(clean_data)] = [Category, ID, Disease, Symptoms_Key, Introduction, Symptoms_Detailed1, Symptoms_Detailed2, Causes, Diagnosis, Treatment, Recovery, Cost]
        saveTxt(driver.page_source, Category, Disease.replace('/', '_'))
    clean_data.to_csv("C:\\Users\\ChuyaoShen\\Desktop\\pianzi\\Pet\\Vetarycom\\Data.csv", index = False)
