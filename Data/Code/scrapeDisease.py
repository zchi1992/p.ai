from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
#import json
import time
#from pdb import set_trace as bp

def saveTxt(content,i):
	text_file = open("path\\name.txt","w")
	text_file.write(content.encode('utf-8'))
	text_file.close()

def saveData(data):
	with open("path\\name.csv","wb") as f:
		writer = csv.writer(f)
		writer.writerows(data)

def getDiseaseName(driver):
    if "We can\'t seem to find the page" in driver.page_source:
        return []
    else:
        diseaseName=driver.find_elements_by_class_name('charcoal')
        return diseaseName

def getPage(driver):
    if "We can\'t seem to find the page" in driver.page_source:
        pager=[]
    else:
        pager=driver.find_elements_by_class_name('pager-item')
    return pager

def nextPage(driver,pager):
    if (len(pager)!=0):
        temp_ul=pager[0].find_element_by_class_name('active').get_attribute('href')
        driver.get(temp_ul)
        pager.pop(0)
    else:
        print "This is the last page!"

def getContent(driver):
    if "We can\'t seem to find the page" in driver.page_source:
        content = {}
    else:
        #contentEle=driver.find_element_by_class_name('content')
        content = {}
    return content

#def getDescription(elementList):
 

if __name__ == "__main__":
    driver = webdriver.Chrome('C:/Users/Shi/Desktop/aipet/chromedriver.exe')    
    web_catalog = ("http://www.petmd.com/cat/conditions#")    
    driver.get(web_catalog)    
    diseaseElement = getDiseaseName(driver)   
    diseaseElement.pop(0)
    url_list = []
    for i in range(len(diseaseElement)):
        url_temp=diseaseElement[i].get_attribute('href')
        url_list.append(url_temp)
#--------------------------------test----------------------------------------    
    ul=url_list[0]
    driver.get(ul)
    print driver.find_element_by_id('content-content').find_element_by_class_name('content').text
    page_n = getPage(driver)
# Maybe try find element by XPath???    
# Maybe try manipulating/split text after download the whole page content???
    
    
    #for element in range(len(diseaseElement)):
        
    
