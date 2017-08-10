from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import csv
import time
import sys

def saveTxt(content,animal,d_name):
    path = "C:\\Users\\ChuyaoShen\\Desktop\\pianzi\\Pet\\Disease\\html\\"+ animal + "\\"+animal+"_"+d_name+".txt"
    text_file = open(path,"w")
    text_file.write(content.encode('utf-8'))
    text_file.close()

def saveData(data,animal):
    path = "C:\\Users\\ChuyaoShen\\Desktop\\pianzi\\Pet\\Disease\\"+animal+"Disease.csv"
    with open(path,"wb") as f:
        writer = csv.writer(f)
        writer.writerows(data)

def getDiseaseName(driver):
    if "We can\'t seem to find the page" in driver.page_source:
        return []
    else:
        diseaseName=driver.find_elements_by_class_name('charcoal')
        return diseaseName

def get_dict(content, elements):
    title_index=[]
    for i in range(len(elements)):
        if (elements[i].tag_name in ['h2','h3']):
            title_index.append(i)
        else:
            pass
    for i in range(title_index[0], len(elements)):
        if i in title_index:
            content.append([elements[i].text.encode('utf-8'),""])
        elif(elements[i].tag_name in ['p', 'ul']):
            content[-1][1] += elements[i].text.encode('utf-8') + "\n"
    return content

def wait(driver, sec):
    find = False
    st = time.time()
    while(not find):
        if(time.time() - st > sec):
            driver.refresh()
            st = time.time()
            print "refreshing ... "
        try:
            elmt = driver.find_elements_by_css_selector("#content-content > div > div.content > *")
        except Exception:
            continue
        find = True


if __name__ == "__main__":
    animal_list=["horse","exotic","reptile","rabbit","ferret","cat","dog"]
    ipt = raw_input("\nChoose the animal you want:\n0 - horse\n1 - exotic\n2 - reptile\n3 - rabbit\n4 - ferret\n5 - cat\n6 - dog\n")
    animal = animal_list[int(ipt)]
    driver = webdriver.Chrome('C:\\Users\\ChuyaoShen\\Desktop\\pianzi\\chromedriver.exe')    
    web_catalog = ("http://www.petmd.com/"+animal+"/conditions")
    driver.get(web_catalog)    
    diseaseElement = getDiseaseName(driver)
    #if (animal == "cat"):
        #diseaseElement.pop(0)
    url_list = []
    for i in range(len(diseaseElement)):
        url_temp=diseaseElement[i].get_attribute('href')
        name_temp=diseaseElement[i].text
        url_list.append((name_temp,url_temp))

    data = []
    ix = 0
    for url in url_list:  
        ix += 1
        print ix
        new_recrd = []
        new_text = ""

        driver.get(url[1])
        wait(driver, 10)

        content = driver.find_elements_by_css_selector('#content-content > div > div.content > *')
        if len(content) == 1:
            content = driver.find_elements_by_css_selector('#content-content > div > div.content > div > div > *')
        new_recrd = get_dict(new_recrd, content)
        new_text += driver.page_source
        while(True):
            try:
                nextbtn = driver.find_element_by_css_selector("#content-content > div > div.content > div.item-list > ul > li.pager-next.last > a")
                nextbtn.click()
                wait(driver, 10)
                
                content = driver.find_elements_by_css_selector('#content-content > div > div.content > *')
                if len(content) == 1:
                    content = driver.find_elements_by_css_selector('#content-content > div > div.content > div > div > *')
                new_recrd = get_dict(new_recrd, content)
                new_text += driver.page_source
            except Exception:
                break
        data.append(new_recrd)
        saveTxt(new_text, animal, url[0].replace('/', '_'))
    saveData(data, animal)
