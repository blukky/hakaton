import requests
import vk_api
from selenium import webdriver



options = webdriver.ChromeOptions()
options.add_argument('--headless')

driver = webdriver.Chrome(options=options)


driver.get("https://vk.com/id1")
#main_page = driver.page_source
main_page = driver.find_element_by_tag_name("html")
page = main_page.get_attribute("innerHTML")
driver.close()
start = page.find("page_name\">") + len("page_name\">")
end = page.find("<a", start)
name = page[start:end]
print(name)
if page.find("День рождения") != -1:
    start = page.find("День рождения") + len("День рождения <div class=\"labeled\">") + 10
    start = page.find("\">", start) + 2
    end = page.find("</a>", start)
    birthday = page[start:end]
    if page.find("byear" , end) != -1:
        start = page.find("\">", end) + 2
        end = page.find("</a>", start)
        birthday += " " + page[start:end]
    print(birthday)
if page.find("Город", end) != -1:
    start = page.find("Город",end) + len("<div class=\"labeled\">") + 20
    start = page.find("\">",start) + 2
    end = page.find("</a>", start)
    city = page[start:end]
    print(city)
if page.find("Место работы", end) != -1:
    start = page.find("Место работы",end) + len("<div class=\"labeled\">") + 25
    start = page.find("\">",start) + 2
    end = page.find("</a>", start)
    work = page[start:end]
    print(work)
if page.find("Языки", end) != -1:
    start = page.find("Языки:", end) + len("<div class=\"labeled\">") + 20
    start = page.find("\">",start) + 2
    end = page.find("</a>", start)
    lang = page[start:end]
    print(lang)
if page.find("Instagram", end) != -1:
    start = page.find("Instagram", end)
    start = page.find("<a href=\"",start) + len("<a href=\"")
    end = page.find("\"", start)
    inst = page[start:end]
    print(inst)
if page.find("Twitter", end) != -1:
    start = page.find("Twitter", end) + len("<div class=\"labeled\">")
    start = page.find("<a href=\"",start) + len("<a href=\"")
    end = page.find("\"", start)
    facebook = page[start:end]
    print(facebook)
if page.find("Facebook", end) != -1:
    start = page.find("Facebook", end) + len("<div class=\"labeled\">")
    start = page.find("<a href=\"",start) + len("<a href=\"")
    end = page.find("\"", start)
    facebook = page[start:end]
    print(facebook)






