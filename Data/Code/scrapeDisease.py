from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
#import json
import time
#from pdb import set_trace as bp

def saveTxt(content,animal,d_name):
	path = "C:\\Users\\IrisTang\\Documents\\zzz\\aip\\diseaseData\\html\\"+animal+"_"+d_name+".txt"
        text_file = open(path,"w")
	text_file.write(content.encode('utf-8'))
	text_file.close()

def saveData(data,animal):
	path = "C:\\Users\\IrisTang\\Documents\\zzz\\aip\\diseaseData\\"+animal+"Disease.csv"
	with open(path,"wb") as f:
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
        pass

def getContentDict(driver):
    if "We can\'t seem to find the page" in driver.page_source:
        content_dict = {}
    else:
        content = driver.find_elements_by_css_selector('#content-content > div > div.content > *')
        content_1=[]        
        #Create "content_1" to remove page number from text
	for c in content:
            if c.tag_name in ['h2','h3','p','ul']:
                content_1.append(c)
            else:
                pass
        #Get indices of headings
	title_indext=[]
        for i in range(len(content_1)):
            if (content_1[i].tag_name in ['h2','h3']):
                title_indext.append(i)
            else:
                pass
        title_indext.append(len(content_1)-1)
        content_text=[]
        for c in content_1:
            content_text.append(c.text)
        content_dict={}
        for i in range(len(title_indext)-1):
            content_dict[content_text[title_indext[i]]] = content_text[title_indext[i]+1:title_indext[i+1]]
    return content_dict

 

if __name__ == "__main__":
    driver = webdriver.Chrome('C:/Users/Shi/Desktop/aipet/chromedriver.exe')    
    animal_list=["cat","dog","bird","horse","fish","exotic","rabbit","ferret","reptile"]
    for animal in animal_list:
        time_animal_start=time.time()
        web_catalog = ("http://www.petmd.com/"+animal+"/conditions")
        driver.get(web_catalog)    
        diseaseElement = getDiseaseName(driver)
        diseaseElement.pop(0)
        url_list = []
        disease_name = []
        data = []
        for i in range(len(diseaseElement)):
            url_temp=diseaseElement[i].get_attribute('href')
            name_temp=diseaseElement[i].text
            url_list.append((name_temp,url_temp))
            #disease_name.append(name_temp)
        for url in url_list:
            time_disease_start=time.time()
            row = []
            driver.get(url[1])
            content_dict = getContentDict(driver)
            page_n = getPage(driver)
            html_source=driver.page_source
            while (len(page_n)!=0):
                nextPage(driver,page_n)
                dict_temp=getContentDict(driver)
                content_dict.update(dict_temp)
                html_source=html_source+driver.page_source
            row.append(url[0])
            for d in content_dict:
                row.append(d)
                row.append(content_dict[d])
            data.append(row)
            saveTxt(html_source,animal,url[0])
            print url[0]
            print time.time()-time_disease_start
        saveData(data,animal)
        print animal
        print time.time()-time_animal_start
	
'''    
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
    getContentDict(driver)
            
    page_n = getPage(driver)
    driver.close()
'''
