import requests
import vk_api
from selenium import webdriver
from time import sleep
import re
import facebook

# options = webdriver.ChromeOptions()
# options.add_argument('--headless')

# ACESS_TOKIN = "EAAROqpgLuqcBALm7s3cYlw9er9FHaplgoEHlm5PVUGPATx6BAphZBhyvOIDZCuODsWYDrJvh0hSbp3KSUqlY1HeubjZBd0aC2QQ0iJjIithfl5kIkeVZAFA5SUpxsrE4GpP3mUT1ofd5vEl2yJdSC3IgZC7hmdSkjNX4QagikG6IxPiaOZCVeZCDQVtoZArmIxAFfYSK2vrbXF4VElxwMZB2j7W9Lz3ZCMmnuwO5GhuZBbHaVSuyF8JQNqmXarynTEhh0QZD"





driver = webdriver.Chrome()#options=options)


driver.get("https://vk.com/id1")
#main_page = driver.page_source
main_page = driver.find_element_by_tag_name("html")
page = main_page.get_attribute("innerHTML")
#driver.close()
start = page.find("page_name\">") + len("page_name\">")
end = page.find("<a", start)
name = page[start:end]
print( "ФИО: " + name)
if page.find("День рождения") != -1:
    start = page.find("День рождения") + len("День рождения <div class=\"labeled\">") + 10
    start = page.find("\">", start) + 2
    end = page.find("</a>", start)
    birthday = page[start:end]
    if page.find("byear" , end) != -1:
        start = page.find("\">", end) + 2
        end = page.find("</a>", start)
        birthday += " " + page[start:end]
    print("День рождения: " + birthday)
if page.find("Город", end) != -1:
    start = page.find("Город",end) + len("<div class=\"labeled\">") + 20
    start = page.find("\">",start) + 2
    end = page.find("</a>", start)
    city = page[start:end]
    print("Город: " + city)
if page.find("Место работы", end) != -1:
    start = page.find("Место работы",end) + len("<div class=\"labeled\">") + 25
    start = page.find("\">",start) + 2
    end = page.find("</a>", start)
    work = page[start:end]
    print("Место работы: " + work)
if page.find("Языки", end) != -1:
    start = page.find("Языки:", end) + len("<div class=\"labeled\">") + 20
    start = page.find("\">",start) + 2
    end = page.find("</a>", start)
    lang = page[start:end]
    print("Основной язык: " + lang)
if page.find("Instagram", end) != -1:
    start = page.find("Instagram", end)
    start = page.find("<a href=\"",start) + len("<a href=\"")
    end = page.find("\"", start)
    inst = page[start:end]
    print("Instagram: " + inst)
if page.find("Twitter", end) != -1:
    start = page.find("Twitter", end) + len("<div class=\"labeled\">")
    start = page.find("<a href=\"",start) + len("<a href=\"")
    end = page.find("\"", start)
    twitter = page[start:end]
    print("Twitter: " + twitter)
if page.find("Facebook", end) != -1:
    start = page.find("Facebook", end) + len("<div class=\"labeled\">")
    start = page.find("<a href=\"",start) + len("<a href=\"")
    end = page.find("\"", start)
    facebook = page[start:end]
    print("Facebook: " + facebook)


###############
# Парсер Facebook
###############




search_url = "https://www.facebook.com/search/people?q="






####################################
# РОСФИНМОНИТОРИНГ
####################################


name = name.split(" ")
name = ' '.join(reversed(name))
name = re.sub("  ", " ", name)
print(name.upper())

antiterror = [
"http://www.fedsfm.ru/documents/terrorists-catalog-portal-act",
"http://www.fedsfm.ru/documents/terrorists-catalog-portal-add",
"http://www.fedsfm.ru/documents/terrorists-catalog-portal-del"
]
#115085015172389

for i in antiterror:
    driver.get(i)
    main_page = driver.find_element_by_tag_name("html")
    page = main_page.get_attribute("innerHTML")
    start = page.find("title")
    start = page.find("(", start) + 1
    end = page.find(")", start)
    title = page[start:end]
    akt = []
    akt_ur = []
    INN_akt = {}
    k=0
    start = 0
    yur_face_start = page.find("Российские юридические лица")
    yur_face_end = page.find("Российские физические лица")
    # first_name = name.split(" ")[0]
    # last_name = name.split(" ")[1]
    while page.find(name.upper(), start) != -1:
        start = page.find(name.upper(), start)
        end = page.find(",", start)
        if start > yur_face_start and end < yur_face_end:
            akt_ur.append(page[start:end])
            if page.find("ИНН", end) != -1:
                end = page.find(";", start)
                start = page.find("ИНН", start) + 4
                if start < end:
                    INN_akt[akt[k]] = page[start:end]
            k += 1
        else:
            akt.append(page[start:end])
        start += 1



    print(title)
    print(akt)
    print(INN_akt)



driver.get("https://bankrot.fedresurs.ru/DebtorsSearch.aspx")
#  хз почему, но не нажимает на поиск
start = 0
if akt_ur:
    for i in akt_ur:
        #nikname = driver.find_element_by_css_selector("#ctl00_cphBody_tbOrgName")
        INN = driver.find_element_by_css_selector("#ctl00_cphBody_OrganizationCode1_CodeTextBox")
        #nikname.send_keys(i)
        INN.send_keys("2201004591")#INN_akt[i])
        driver.find_element_by_css_selector("#ctl00_cphBody_btnSearch").click()
        sleep(3)
        main_page = driver.find_element_by_tag_name("html")
        page = main_page.get_attribute("innerHTML")
        start = page.find("<th scope=\"col\" style=\"width:5%;\">Категория</th><th scope=\"col\">Должник</th><th scope=\"col\">ИНН</th><th scope=\"col\">ОГРН</th><th scope=\"col\">Регион</th><th scope=\"col\">Адрес</th>")
        end_table = page.find("</table>", start)
        start += len("<th scope=\"col\" style=\"width:5%;\">Категория</th><th scope=\"col\">Должник</th><th scope=\"col\">ИНН</th><th scope=\"col\">ОГРН</th><th scope=\"col\">Регион</th><th scope=\"col\">Адрес</th>")
        while page.find("\">", start) != -1 :
            start = page.find(";\">", start)
            if start > end_table:
                break
            end = page.find("</td>", start)
            print("Категория:" + page[start:end])

            start = page.find("\">", end)
            end = page.find("</a>", start)
            print("Должник:" + page[start:end])

            start = page.find("\">", end)
            end = page.find("</td>", start)
            print("ИНН:" + page[start:end])

            start = page.find("\">", end)
            end = page.find("</td>", start)
            print("ОГРН:" + page[start:end])

            start = page.find("\">", end)
            end = page.find("</td>", start)
            print("ИНН:" + page[start:end])

            start = page.find("\">", end)
            end = page.find("</td>", start)
            print("Регион:" + page[start:end])

            start = page.find("\">", end)
            end = page.find("</td>", start)
            print("Адрес:" + page[start:end])
else:
    name = name.split(" ")
    print(name)
    driver.find_element_by_css_selector("#ctl00_cphBody_rblDebtorType_1").click()
    last_name = driver.find_element_by_css_selector("#ctl00_cphBody_tbPrsLastName")
    first_name = driver.find_element_by_css_selector("#ctl00_cphBody_tbPrsFirstName")
    last_name.send_keys(name[0])
    sleep(0.1)
    first_name.send_keys(name[1])
    driver.find_element_by_css_selector("#ctl00_cphBody_btnSearch").click()
    sleep(3)
    main_page = driver.find_element_by_tag_name("html")
    page = main_page.get_attribute("innerHTML")
    start = page.find("<th scope=\"col\" style=\"width:5%;\">Категория</th><th scope=\"col\">Должник</th><th scope=\"col\">ИНН</th><th scope=\"col\">ОГРНИП</th><th scope=\"col\" style=\"width:7%;\">СНИЛС</th><th scope=\"col\">Регион</th><th scope=\"col\">Адрес</th>")
    end_table = page.find("</table>", start)
    start += len("<th scope=\"col\" style=\"width:5%;\">Категория</th><th scope=\"col\">Должник</th><th scope=\"col\">ИНН</th><th scope=\"col\">ОГРНИП</th><th scope=\"col\" style=\"width:7%;\">СНИЛС</th><th scope=\"col\">Регион</th><th scope=\"col\">Адрес</th>")
    while page.find("\">", start) != -1 :
        start = page.find(";\">", start) + 3
        if start > end_table:
            break
        end = page.find("</td>", start)
        kategory = re.sub("\n", "", page[start:end])
        kategory = re.sub("\t", "", kategory)

        start = page.find("\">", end) + 3
        end = page.find("</a>", start)
        dolzhnik = page[start:end]
        if last_name != dolzhnik.split(" ")[0]:
            start = page.find("</tr>", start)
            continue

        start = page.find("\">", end) +3
        end = page.find("</td>", start)
        INN = re.sub("\n", "",page[start:end])
        INN = re.sub("\t", "", INN)



        start = page.find("\">", end) +3
        end = page.find("</td>", start)
        OGRN = re.sub("\n", "", page[start:end])
        OGRN = re.sub("\t", "", OGRN)


        start = page.find("<td>", end) + 4
        end = page.find("</td>", start)
        SNILS = re.sub("\n", "", page[start:end])
        SNILS = re.sub("\t", "", SNILS)


        start = page.find("\">", end) + 3
        end = page.find("</td>", start)
        area = re.sub("\n", "", page[start:end])
        area = re.sub("\t", "", area)


        start = page.find("\">", end) + 3
        end = page.find("</td>", start)
        adress = re.sub("\n", "", page[start:end])
        adress = re.sub("\t", "", adress)

        print("Категория:" + page[start:end])
        print("Должник:" + dolzhnik)
        print("ИНН:" + INN)
        print("ОГРН:" + OGRN)
        print("СНИЛС:" + SNILS)
        print("Регион:" + area)
        print("Адрес:" + adress)


driver.close()


