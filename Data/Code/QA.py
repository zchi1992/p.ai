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
        try:
            try:
                answer = driver.find_element_by_css_selector(".questionDetail__answer:nth-child(1) > p:nth-child(2)")
            except Exception:
                answer = driver.find_element_by_css_selector(".questionDetail__answer > p:nth-child(2)")
            return answer.text
        except Exception:
            return "Empty"


if __name__ == "__main__":
    driver =webdriver.Chrome('C:\\Users\\ChuyaoShen\\Desktop\\pianzi\\chromedriver.exe')
    data = []
    for i in range(332500):
        row =[str(i)]
        web = "https://www.petcoach.co/question/?id=" + str(i)
        driver.get(web)
        time.sleep(3)
        row.append(getCategory(driver))
        row.append(getQuestion(driver))
        row.append(getAnswer(driver))
        print row
        data.append(row)
        saveTxt(driver.page_source, i)

    saveData(data)



