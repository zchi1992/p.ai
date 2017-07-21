from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import time

def saveTxt(content,i):
    text_file = open("C:\\Users\\ChuyaoShen\\Desktop\\pianzi\\Pet\\data\\QAid=" + "%06d"%i + ".txt", "w")
    text_file.write(content.encode('utf-8'))
    text_file.close()

def saveData(data):
    with open("C:\\Users\\ChuyaoShen\\Desktop\\pianzi\\Pet\\QADatabase.csv", "wb") as f:
        writer = csv.writer(f)
        writer.writerows(data)

def getCategory(driver):
    if "We can\'t seem to find the page" in driver.page_source:
        return "Empty"
    else:
        try:
            category = driver.find_element_by_css_selector(".category")
            return category.text
        except Exception:
            return "Empty"

def getQuestion(driver):
    if "We can\'t seem to find the page" in driver.page_source:
        return "Empty"
    else:
        question = driver.find_element_by_css_selector("h1.title")
        return question.text

def getAnswer(driver):
    if "We can\'t seem to find the page" in driver.page_source:
        return "Empty"
    else:
        if "No Answers yet" in driver.page_source:
            return "Empty"
        else:
            answer = driver.find_element_by_css_selector(".questionDetail__answer:nth-child(1) > p:nth-child(2)")
            return answer.text



if __name__ == "__main__":
    driver =webdriver.Chrome('C:\\Users\\ChuyaoShen\\Desktop\\pianzi\\chromedriver.exe')
    data = []
    for i in range(332500):
        row =[str(i)]
        web = "https://www.petcoach.co/question/?id=" + str(i)
        driver.get(web)
        find = False
        start_time = time.time()
        while(not find):
            if(time.time()-start_time > 8):
                driver.get(web)
                start_time = time.time()
                print "Freshing...."
            try:
                Answer = getAnswer(driver)
                Question = getQuestion(driver)
                Category = getCategory(driver)
            except Exception:
                continue
            find = True
        row.append(Category)
        row.append(Question)
        row.append(Answer)
        print row
        data.append(row)
        saveTxt(driver.page_source, i)

    saveData(data)
