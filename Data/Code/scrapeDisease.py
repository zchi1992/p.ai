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
        diseaseName=driver.find_elements_by_class_name("charcoal")
        return diseaseName

def getPage(driver):
    if "We can\'t seem to find the page" in driver.page_source:
        pager=[]
    else:
        pager=driver.find_elements_by_class_name("pager-item")
    return pager

def nextPage(driver,pager):
    if (len(pager)!=0):
        pager[0].click()
        pager.pop(0)        
#def getSymptom(elementList):
    

#def getDescription(elementList):
    

if __name__ == "__main__":
    driver = webdriver.Chrome('C:/Users/IrisTang/Documents/zzz/aip/chromedriver_win32/chromedriver.exe')
    
    web_catalog = ("http://www.petmd.com/cat/conditions#")
    start_time = time.time()
    driver.get(web_catalog)
    try:
        diseaseElement = getDiseaseName(driver)
    except Exception:
        print "error in getDiseaseName"
    print("---%s seconds ---" % (time.time() - start_time))
    diseaseElement.pop(0)
    print diseaseElement[0].text
    diseaseElement[0].click()
    
    #for element in range(len(diseaseElement)):
        
    