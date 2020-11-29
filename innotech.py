import requests
import vk_api
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from time import sleep
import re
import facebook


# ACESS_TOKIN = "EAAROqpgLuqcBALm7s3cYlw9er9FHaplgoEHlm5PVUGPATx6BAphZBhyvOIDZCuODsWYDrJvh0hSbp3KSUqlY1HeubjZBd0aC2QQ0iJjIithfl5kIkeVZAFA5SUpxsrE4GpP3mUT1ofd5vEl2yJdSC3IgZC7hmdSkjNX4QagikG6IxPiaOZCVeZCDQVtoZArmIxAFfYSK2vrbXF4VElxwMZB2j7W9Lz3ZCMmnuwO5GhuZBbHaVSuyF8JQNqmXarynTEhh0QZD"


def spark(driver, url):
    driver.get(url)
    try:
        if driver.find_element_by_css_selector("body > div.search-result > div.search-result__content > div > div > div > div > span").text == "Ничего не найдено. Попробуйте изменить результаты поиска":
            print("Ничего не найдено. Попробуйте изменить результаты поиска")
            return
    except NoSuchElementException:
        print("Все идет по плану")
    lising = driver.find_elements_by_class_name("search-result-list__item")
    for i in lising:
        title = i.find_element_by_class_name("summary__title").text
        content = i.find_element_by_class_name("summary__body-section").text
        code = i.find_element_by_class_name("code").text
        if INNs or INN_akt:
            start = code.find("ИНН") + 4
            end = code.find("·")
            if not code[start:end] in INNs and not code[start:end] in INN_akt:
                continue
            start = 0
            start = content.find("ИНН") + 4
            end = content.find(")")
            if not content[start:end] in INNs and not content[start:end] in INN_akt:
                continue
        if not name[0] in content:
            continue
        for i in dolzhniki:
            if not i in dolzhniki:
                continue
        print(title)
        print(content)
        print(code)

def egrul(driver, name):
    input_text = driver.find_element_by_css_selector("#query")
    input_text.send_keys(name)
    driver.find_element_by_css_selector("#btnSearch").click()
    try:
        if driver.find_element_by_css_selector("#noDataFound > div > div > p").text == "По заданным критериям поиска данных не найдено.":
                print("По заданным критериям поиска данных не найдено.")
                return
    except NoSuchElementException:
        print("Продолжаем искать :)")
    row = driver.find_elements_by_class_name("res-row")
    for i in  row:
        title = i.find_element_by_class_name("op-excerpt").text
        text = i.find_element_by_class_name("res-text").text
        if dolzhniki:
            for i in dolzhniki:
                if not i in text and not i in title:
                    continue
                else:
                    print(title)
                    print(text)
                    continue
        if INNs:
            for i in INNs:
                if not i in text and not i in title:
                    continue
                else:
                    print(title)
                    print(text)
                    continue
        if OGRNs:
            for i in OGRNs:
                if not i in text and not i in title:
                    continue
                else:
                    print(title)
                    print(text)
                    continue


def parce_open_source(driver, url):

    driver.get(url)
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

    akt = []
    akt_ur = []
    INN_akt = {}
    k=0

    for i in antiterror:
        driver.get(i)
        main_page = driver.find_element_by_tag_name("html")
        page = main_page.get_attribute("innerHTML")
        start = page.find("title")
        start = page.find("(", start) + 1
        end = page.find(")", start)
        title = page[start:end]

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


    if title:
        print(title)
    if akt:
        print(akt)
    if akt_ur:
        print(akt_ur)
    if INN_akt:
        print(INN_akt)
    # if not akt and not akt_ur and not INN_akt:
        # print("Ничего не нашлось")



    driver.get("https://bankrot.fedresurs.ru/DebtorsSearch.aspx")
    start = 0
    kategoryes = []
    dolzhniki = []
    PHIRMA = []
    INNs = []
    OGRNs = []
    SNILSs = []
    areas = []
    adresses =[]
    if akt_ur:
        for i in akt_ur:
            nikname = driver.find_element_by_css_selector("#ctl00_cphBody_tbOrgName")
            INN = driver.find_element_by_css_selector("#ctl00_cphBody_OrganizationCode1_CodeTextBox")
            nikname.send_keys(i.capitalize())
            INN.send_keys(INN_akt[i])
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
                kategory = re.sub("\n", "", page[start:end])
                kategory = re.sub("\t", "", kategory)
                print("Категория:" + page[start:end])


                start = page.find("\">", end)
                end = page.find("</a>", start)
                dolzhnik = re.sub("\n", "", page[start:end])
                dolzhnik = re.sub("\t", "", dolzhnik)
                print("Должник:" + page[start:end])



                start = page.find("\">", end)
                end = page.find("</td>", start)
                INN = re.sub("\n", "", page[start:end])
                INN = re.sub("\t", "", INN)
                print("ИНН:" + page[start:end])

                start = page.find("\">", end)
                end = page.find("</td>", start)
                OGRN = re.sub("\n", "", page[start:end])
                OGRN = re.sub("\t", "", OGRN)
                print("ОГРН:" + page[start:end])

                start = page.find("\">", end)
                end = page.find("</td>", start)
                area = re.sub("\n", "", page[start:end])
                area = re.sub("\t", "", area)
                print("Регион:" + page[start:end])

                start = page.find("\">", end)
                end = page.find("</td>", start)
                adress = re.sub("\n", "", page[start:end])
                adress = re.sub("\t", "", adress)
                print("Адрес:" + page[start:end])


                kategoryes.append(kategory)
                PHIRMA.append(dolzhnik)
                INNs.append(INN)
                OGRNs.append(OGRN)
                SNILSs.append(SNILS)
                areas.append(area)
                adresses.append(adress)


    else:
        name = name.split(" ")
        # print(name)
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
            dolzhnik = re.sub("\n", "", page[start:end])
            dolzhnik = re.sub("\t", "", dolzhnik)
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

            kategoryes.append(kategory)
            dolzhniki.append(dolzhnik)
            INNs.append(INN)
            OGRNs.append(OGRN)
            SNILSs.append(SNILS)
            areas.append(area)
            adresses.append(adress)

            print("Категория:" + page[start:end])
            print("Должник:" + dolzhnik)
            print("ИНН:" + INN)
            print("ОГРН:" + OGRN)
            print("СНИЛС:" + SNILS)
            print("Регион:" + area)
            print("Адрес:" + adress)



    driver.get("https://kad.arbitr.ru/")
    try:
        driver.find_element_by_css_selector("#js > div.b-promo_notification.b-promo_notification--without_link > div.b-promo_notification-popup_wrapper > div > div > div > div > a.b-promo_notification-popup-close.js-promo_notification-popup-close").click()
    except NoSuchElementException:
        print("Выполняется код !;)")
    input_text = driver.find_element_by_css_selector("#sug-participants > div > textarea")
    sydi = []
    input_text.send_keys("Павел Алексеевич Буденко" + ", " + "45326754")
    driver.find_element_by_css_selector("#b-form-submit > div > button").click()
    if PHIRMA and INNs[:len(PHIRMA)]:
        for i, j in PHIRMA, INNs[:len(PHIRMA)]:
            input_text.send_keys(i + ", " + j)
            driver.find_element_by_css_selector("#b-form-submit > div > button").click()
            Istec = driver.find_elements_by_class_name("plaintiff")
            otvetchik = driver.find_elements_by_class_name("respondent")
            num = driver.find_elements_by_class_name("num")
            for k, l, n in Istec, otvetchik, num:
                if k.text != i and l.text != i:
                    continue
                else:
                    sydi.append(n.text)
                    print(n.text)
    elif dolzhniki and INNs[len(PHIRMA):]:
        for i, j in dolzhniki, INNs[len(PHIRMA):]:
            input_text.send_keys(i + ", " + j)
            driver.find_element_by_css_selector("#b-form-submit > div > button").click()
            Istec = driver.find_elements_by_class_name("plaintiff")
            otvetchik = driver.find_elements_by_class_name("respondent")
            num = driver.find_elements_by_class_name("num")
            for k, l, n  in Istec, otvetchik, num:
                if k.text != i and l.text != i:
                    continue
                else:
                    sydi.append(n.text)
                    print(n.text)
    if PHIRMA:
        for i in PHIRMA:
            url = "https://www.spark-interfax.ru/search?Query={}".format(re.sub(" ", "+", i))
            spark(driver, url)
    if INNs:
        for i in INNs:
            url = "https://www.spark-interfax.ru/search?Query={}".format(i)
            spark(driver, url)
    if dolzhniki:
        for i in dolzhniki:
            url = "https://www.spark-interfax.ru/search?Query={}".format(re.sub(" ", "+", i))
            spark(driver, url)
    if OGRNs:
        for i in OGRNs:
            url = "https://www.spark-interfax.ru/search?Query={}".format(i)
            spark(driver, url)



    driver.get("https://egrul.nalog.ru/index.html")
    if PHIRMA:
        for i in PHIRMA:
            egrul(driver, i)
    if INNs:
        for i in INNs:
            egrul(driver, url)
    if dolzhniki:
        for i in dolzhniki:
            egrul(driver, url)
    if OGRNs:
        for i in OGRNs:
            egrul(driver, url)








    driver.close()


