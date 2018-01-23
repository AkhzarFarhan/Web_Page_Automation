from selenium import webdriver
import random

browser = webdriver.Firefox() #Make sure you have Firefox in your PC.
browser.get("##Web address of google forms##") #For opening a browser
for i in range(50): #Do any thing that you want to, it is just an example.
    b1 = browser.find_element_by_css_selector(".freebirdFormviewerViewNavigationButtons")
    b1.click()
    b3 = browser.find_element_by_css_selector("div.quantumWizButtonPaperbuttonEl:nth-child(2) > div:nth-child(2)")
    b3.click()
    text = browser.find_element_by_css_selector(".quantumWizTextinputPapertextareaInput")
    for j in range(30):
        text.send_keys(names[random.randint(0, 11)])
        text.send_keys(words[random.randint(0, 16)])
        text.send_keys(names[random.randint(0, 11)])
    b2 = browser.find_element_by_css_selector("div.quantumWizButtonPaperbuttonEl:nth-child(2) > content:nth-child(3) > span:nth-child(1)")
    b2.click()
    browser.get("##Web address of google forms")
