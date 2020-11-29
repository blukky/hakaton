from selenium import webdriver
import re
import os
import itertools
import numpy as np
import msvcrt, sys
import requests
import time
import dlib
from skimage import io
from PIL import Image
import shutil
import random
import os
import vk_api
import tensorflow as tf
import tensorflow_hub as hub
from selenium.common.exceptions import NoSuchElementException
from PyQt5.QtWidgets import QMessageBox
from VkIdsParser_1 import parse_vk

# def find_css(driver, css):
#     try:
#         driver.find_element_by_css_selector(css)
#     except NoSuchElementException:
#         return False
#     return True
#
# def find_name(driver, name):
#     try:
#         driver.find_element_by_name(name)
#     except NoSuchElementException:
#         return False
#     return True
#
# def find_class_name(driver, class_name):
#     try:
#         driver.find_element_by_class_name(class_name)
#     except NoSuchElementException:
#         return False
#     return True

# def test_for_working(driver, url):
#     if requests.get(url).status_code == 404:
#         ui_vk.error.setText("Неверная ссылка на страницу!")
#         return False
#     elif find_class_name(driver, "profile_deleted_text"):
#         ui_vk.error.setText("Закрытый профиль! Попробуйте Авторизироваться!")
#         return False
#     elif find_class_name(driver, "profile_blocked page_block"):
#         ui_vk.error.setText("Такого пользователя не существует!")
#         return False
#     elif find_css(driver, "#content > div > div.message_page_body"):
#         ui_vk.error.setText("Страница Удалена!!!")
#         return False
#     elif find_class_name(driver, "page_name")== False:
#         ui_vk.error.setText("Неверная страница")
#         return False
#     elif find_css(driver, "#wide_column > div.page_block.profile_closed_wall_dummy > div"):
#         ui_vk.error.setText("Закрытый аккаунт")
#         return False
#     elif find_css(driver, "#content > h5"):
#         if "подозрительную активность и временно заморозили её, чтобы вырвать из рук злоумышленников." in driver.find_element_by_css_selector("#content > h5").text or "К сожалению, нам пришлось заблокировать страницу" in driver.find_element_by_css_selector("#content > h5").text:
#             ui_vk.error.setText("Страница заблокирована!")
#             return False
#     elif driver.find_element_by_class_name("page_name").text == "Администратор":
#         ui_vk.error.setText("Страница Администратора")
#         return False
#     return True


# def test_for_working_api(driver, url):
#     if requests.get(url).status_code == 404:
#         ui_vk.error.setText("Неверная ссылка на страницу!")
#         return False
#     #elif find_class_name(driver, "profile_deleted_text"):
#        # ui.error.setText("Закрытый профиль! Попробуйте Авторизироваться!")
#        # return False
#     elif find_class_name(driver, "profile_blocked page_block"):
#         ui_vk.error.setText("Такого пользователя не существует!")
#         return False
#     elif find_css(driver, "#content > div > div.message_page_body"):
#         ui_vk.error.setText("Страница Удалена!!!")
#         return False
#     elif find_class_name(driver, "page_name")== False:
#         ui_vk.error.setText("Неверная страница")
#         return False
#     #elif find_css(driver, "#wide_column > div.page_block.profile_closed_wall_dummy > div"):
#        # ui.error.setText("Закрытый аккаунт")
#         #return False
#     elif find_css(driver, "#content > h5"):
#         if "подозрительную активность и временно заморозили её, чтобы вырвать из рук злоумышленников." in driver.find_element_by_css_selector("#content > h5").text or "К сожалению, нам пришлось заблокировать страницу" in driver.find_element_by_css_selector("#content > h5").text:
#             ui_vk.error.setText("Страница заблокирована!")
#             return False
#     elif driver.find_element_by_class_name("page_name").text == "Администратор":
#         ui_vk.error.setText("Страница Администратора")
#         return False
#     return True


def get_string(index):
    category = [('cadet', 0), ('other', 1)]
    for class_string, class_index in category:
        if class_index == index:
            return class_string

#
# def find_id(driver, id):
#     try:
#         driver.find_element_by_id(id)
#     except NoSuchElementException:
#         return False
#     return True


def load_file(vk, name, photo_name, url):
    if not name in os.listdir():
        os.mkdir(name)
    if not os.path.exists(name + "\\" + photo_name + ".jpg"):
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(name + "\\" + photo_name + ".jpg", 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)


def get_photos_by_id(vk, name, user_id_):
    try:
        request_result = vk.photos.getAll(owner_id=user_id_,
                                          count=50,
                                          no_service_albums=0)
        prev = ''
        flag = 0
        photos = []
        for item in request_result['items']:
            for size in item['sizes']:
                url_ = str(size['url'])
                mas_ = url_.split('/')
                ident = mas_[4]
                if prev != ident:
                    prev = ident
                    flag = 0
                else:
                    flag += 1
                    if flag == 3:
                        photos.append(url_)
        max_flag = 0
        for photo in photos:
            max_flag += 1
            if max_flag < 100:
                load_file(vk, name, name + '_' + str(max_flag), photo)
    except Exception as ex:
        print(ex)



# def sniffer(url):
#     global login, passwd
#     if requests.get(url).status_code == 404:
#         ui_vk.error.setText("Неверная ссылка на страницу")
#         return False
#     driver = webdriver.Chrome()
#     driver.get(url)
#     time.sleep(1)
#     name = driver.find_element_by_class_name("page_name").text
#     name = name.split(" ")
#     name = name[1]
#     if not name in os.listdir():
#         os.mkdir(name)
#     photo_btn = driver.find_elements_by_class_name("page_counter")
#     k = 0
#     for i in range(len(photo_btn)):
#          #print(photo_btn[i].text)
#          if "фотографии" in photo_btn[i].text or "фотографий" in photo_btn[i].text or "фотография" in photo_btn[i].text:
#             k += 1
#             break
#     # print(i)
#     if k==0:
#        ui_vk.error.setText("Фотографий нет")
#        group(driver,url)
#        return 0
#     k=0
#     for i in range(1,15):
#         xpath = "/html/head/link[{}]".format(str(i))
#         id = driver.find_element_by_xpath(xpath).get_attribute("href")
#         if re.search("=",id):
#             id = id.split("=")
#             id = id[1]
#             k+=1
#             break
#     body = str(driver.page_source)
#     if body.find("http://instagram.com") != -1:
#         url_start = body.find("http://instagram.com")
#         url_end = body.find("\"",url_start)
#         print(body[url_start:url_end])
#         sniffer_inst_in_vk(body[url_start:url_end],name)
#     print(os.getcwd())
#     if k!=0:
#         driver.close()
#         token = 'fe4376b10059b99f985c66a2828211ab8908e205fb04d8e9f953b1071cfbdecc992b82cf1c9350e9588f9'
#         VERSION_ID = "7605360"
#         vk_session = vk_api.VkApi(token=token,api_version=vk_api.__version__,app_id=VERSION_ID)
#         vk = vk_session.get_api()
#         get_photos_by_id(vk, name, id)
#         #driver.get(url + "?z=albums" + id)
#         #time.sleep(1)
#         #years = driver.find_element_by_id("pva_content_photos").find_elements_by_class_name("photos_row")
#         #l = 0
#         #photos = webdriver.Chrome()
#         #for i in years:
#             #id_photos = i.get_attribute("data-id")
#             #id_photos = id_photos.split("_")
#             #url_photos = url +"?z=photo{}_{}%2Fphotos{}".format(id_photos[0], id_photos[1],
#                                                                                  #id_photos[0])
#         # print(url_photos)
#             #photos.get(url_photos)
#             #time.sleep(5)
#             #img = photos.find_element_by_css_selector("#pv_photo > img").get_attribute("src")
#         # print(img)
#             #image = requests.get(img)
#             #with open(str(name_dir[1]) + "\\" + name + "_" + str(l) + ".jpg", 'wb') as f:#"photos_vk\\" +
#                 #f.write(image.content)
#         # print(img)
#             #l+=1
#         #photos.close()
#         #driver.close()
#         model = tf.keras.models.load_model("model.h5", custom_objects={'KerasLayer':hub.KerasLayer})
#         detector = dlib.get_frontal_face_detector()
#         predict = []
#         for i in os.listdir(name):
#             im = io.imread(name+ "\\" + i)
#             dets = detector(im,1)
#             print(dets)
#             if not dets:
#                 os.remove(name + "\\" + i)
#                 continue
#             image = Image.open(name+ "\\" +i)
#             img = np.array(image)/255.0
#             img = img.reshape(1,img.shape[0],img.shape[1],img.shape[2])
#             predict.append(get_string(np.argmax(model.predict(img))))
#         if 'cadet' in predict:
#             return 1
#         else:
#             return 0
#
#     if find_css(driver, "#profile_photos_module > a.module_header > div"):
#         driver.find_element_by_css_selector("#profile_photos_module > a.module_header > div").click()
#         time.sleep(1)
#         if "vk.com/login" in driver.current_url:
#             authen()
#             login_input = driver.find_element_by_css_selector(
#                 "#email")
#             paswd_input = driver.find_element_by_css_selector(
#                 "#pass")
#             login_input.send_keys(login)
#             paswd_input.send_keys(passwd)
#             driver.find_element_by_css_selector(
#                 "#login_button").click()
#             time.sleep(1)
#             if find_css(driver, "#login_message > div"):
#                 print("Неверный логин или пароль")
#                 return False
#             sniffer(driver, url)
#     else:
#         driver.find_element_by_css_selector("#wide_column > div:nth-child(1) > div.counts_module > a:nth-child({})".format(str(i+1))).click()
#         time.sleep(3)
#         if find_css(driver, "#box_layer > div.popup_box_container > div" ):#driver.find_element_by_css_selector("#box_layer > div.popup_box_container > div").is_displayed():
#             authen()
#             login_input = driver.find_element_by_css_selector(
#                 "#box_layer > div.popup_box_container > div > div.box_body.box_no_buttons > div > form > input:nth-child(1)")
#             paswd_input = driver.find_element_by_css_selector(
#                 "#box_layer > div.popup_box_container > div > div.box_body.box_no_buttons > div > form > input:nth-child(2)")
#             login_input.send_keys(login)
#             paswd_input.send_keys(passwd)
#             driver.find_element_by_css_selector(
#                 "#box_layer > div.popup_box_container > div > div.box_body.box_no_buttons > div > form > div.LoginBoxForm__buttons > button.flat_button.button_big_text.LoginBoxForm__buttonSignIn").click()
#             time.sleep(3)
#             if find_css(driver, "#login_message > div"):
#                 return False
#             photo_btn = driver.find_elements_by_class_name("page_counter")
#             for i in range(len(photo_btn)):
#                 # print(photo_btn[i].text)
#                 if "фотографии" in photo_btn[i].text or "фотографий" in photo_btn[i].text or "фотография" in photo_btn[i].text:
#                     break
#             # print(i)
#             driver.find_element_by_css_selector(
#                          "#wide_column > div:nth-child(1) > div.counts_module > a:nth-child({})".format(str(i+1))).click()
#     time.sleep(3)
#     years = driver.find_element_by_id("pva_content_photos").find_elements_by_class_name("photos_row")
#     k = 0
#     photos = webdriver.Chrome()
#     for i in years:
#         id_photos = i.get_attribute("data-id")
#         id_photos = id_photos.split("_")
#         url_photos = url +"?z=photo{}_{}%2Fphotos{}".format(id_photos[0], id_photos[1],
#                                                                                  id_photos[0])
#         # print(url_photos)
#         photos.get(url_photos)
#         time.sleep(5)
#         img = photos.find_element_by_css_selector("#pv_photo > img").get_attribute("src")
#         # print(img)
#         image = requests.get(img)
#         with open(str(name_dir[1]) + "\\" + name + "_" + str(k) + ".jpg", 'wb') as f:#"photos_vk\\" +
#             f.write(image.content)
#         # print(img)
#         k+=1
#     photos.close()
#     driver.close()
#     model = tf.keras.models.load_model("model.h5", custom_objects={'KerasLayer':hub.KerasLayer})
#     predict = []
#     detector = dlib.get_frontal_face_detector()
#     for i in os.listdir(name):
#         im = io.imread(name + "\\" + i)
#         dets = detector(im,1)
#         print(dets)
#         if not dets:
#             os.remove(name + "\\" + i)
#             continue
#         img = np.array(Image.open(name+ "\\" + i))/255.0
#         img = img.reshape(1,img.shape[0],img.shape[1],img.shape[2])
#         predict.append(get_string(np.argmax(model.predict(img))))
#     if 'cadet' in predict:
#         return 1
#     else:
#         return 0

def sniffer_with_api(vk, url, driver):
    id = url.split("/")[3][2:]
    main_page = driver.find_element_by_tag_name("html")
    page = main_page.get_attribute("innerHTML")
    start = page.find("page_name\">") + len("page_name\">")
    end = page.find("<a", start)
    name = page[start:end]
    if page.find("Instagram", end) != -1:
        start = page.find("Instagram", end)
        start = page.find("<a href=\"", start) + len("<a href=\"")
        end = page.find("\"", start)
        inst = page[start:end]
        sniffer_inst_in_vk(inst)
    #token = 'fe4376b10059b99f985c66a2828211ab8908e205fb04d8e9f953b1071cfbdecc992b82cf1c9350e9588f9'
    #VERSION_ID = "7605360"
    #vk_session = vk_api.VkApi(token=token,api_version=vk_api.__version__,app_id=VERSION_ID)
    #vk = vk_session.get_api()
    if not name in os.listdir():
        os.mkdir(name)
    get_photos_by_id(vk, name, id)
    model = tf.keras.models.load_model("model.h5", custom_objects={'KerasLayer':hub.KerasLayer})
    predict = []
    for i in os.listdir(name):
        img = np.array(Image.open(name+ "\\" +i))/255.0
        img = img.reshape(1,img.shape[0],img.shape[1],img.shape[2])
        predict.append(get_string(np.argmax(model.predict(img))))
    if 'cadet' in predict:
        return 1
    else:
        return 0




def sniffer_inst_in_vk(url, name):
    global login, passwd
    if requests.get(url).status_code == 404:
        ui_vk.error.setText("Неверная ссылка на страницу")
        return False
    body = requests.get(url).text
    private = body.find("is_private")+12
    #print(body[private:private+4])
    index_start = 0
    photo_url = []
    if body[private:private+4] == "true":
        return
    #     authen()
    #     driver = webdriver.Chrome()
    #     driver.get("https://instagram.com/")
    #     time.sleep(1)
    #     login_input = driver.find_element_by_css_selector("#loginForm > div > div:nth-child(1) > div > label > input")
    #     password_input = driver.find_element_by_css_selector("#loginForm > div > div:nth-child(2) > div > label > input")
    #     login_input.send_keys(login)
    #     password_input.send_keys(passwd)
    #     driver.find_element_by_css_selector("#loginForm > div.Igw0E.IwRSH.eGOV_._4EzTm.kEKum > div.Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.CovQj.jKUp7.DhRcB").click()
    #     time.sleep(3)
    #     driver.find_element_by_css_selector("#react-root > section > main > div > div > div > div > button").click()
    #     time.sleep(1)
    #     driver.get(url)
    #     time.sleep(1)
    #     last_height = driver.execute_script("return document.body.scrollHeight")
    #     while True:
    # # Scroll down to bottom
    #         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #
    # # Wait to load page
    #         time.sleep(0.5)
    #
    # # Calculate new scroll height and compare with last scroll height
    #         new_height = driver.execute_script("return document.body.scrollHeight")
    #         if new_height == last_height:
    #             break
    #         last_height = new_height
    #     body = str(driver.page_source)
    #     driver.close()
    #     #print(body)
    #     while (body.find("srcset",index_start) != -1 and body.find("240w,",index_start) != -1):
    #         index_start = body.find("srcset",index_start)+8
    #         #print(index_start)
    #         if body.find("150w",index_start) != -1:
    #             index_start = body.find("150w,",index_start)+5
    #         else:
    #             break
    #         if body.find("240w",index_start) != -1:
    #             index_end = body.find("240w,",index_start)-1
    #         else:
    #             break
    #         photo_url.append(body[index_start:index_end])
    #     if not name in os.listdir():
    #         os.mkdir(name)
    #         os.chdir(name)
    #     else:
    #         os.chdir(name)
    #     for i in range(len(photo_url)):
    #         photo_url[i] = photo_url[i].replace("amp;","")
    #         print(photo_url[i])
    #         with open(name + "_" + str(i) + ".jpg",'wb') as f:
    #             f.write(requests.get(photo_url[i]).content)
    else:
        while (body.find("src",index_start)!=-1):
            index_start = body.find("src",index_start)+ 6
            index_end = body.find("\"",index_start)
            photo_url.append(body[index_start:index_end])
        if not name in os.listdir():
            os.mkdir(name)
            os.chdir(name)
        else:
            os.chdir(name)
        for i in range(2, len(photo_url)-8, 6):
            photo_url[i] = photo_url[i].replace("\\u0026","&")
            #print(photo_url[i])
            with open(name + "_" + str(i) + ".jpg",'wb') as f:
                f.write(requests.get(photo_url[i]).content)
    os.chdir("..")


def sniffer_inst():
    global auth, login, passwd, ui_log
    id = ui_insta.id.text()
    url = "https://instagram.com/" + id
    if requests.get(url).status_code == 404:
        ui_vk.error.setText("Неверная ссылка на страницу")
        return False
    body = requests.get(url).text
    private = body.find("is_private")+12
    #print(body[private:private+4])
    index_start = 0
    photo_url = []
    if body[private:private+4] == "true":             
        auth = QtWidgets.QWidget()
        ui_log = Ui_Login()
        ui_log.setupUi(auth)
        auth.setWindowModality(QtCore.Qt.ApplicationModal)
        auth.show()
        ui_log.auth.clicked.connect(data)
        driver = webdriver.Chrome()
        driver.get("https://instagram.com/")
        time.sleep(1)
        login_input = driver.find_element_by_css_selector("#loginForm > div > div:nth-child(1) > div > label > input")
        password_input = driver.find_element_by_css_selector("#loginForm > div > div:nth-child(2) > div > label > input")
        login_input.send_keys(login)
        password_input.send_keys(passwd)
        driver.find_element_by_css_selector("#loginForm > div.Igw0E.IwRSH.eGOV_._4EzTm.kEKum > div.Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.CovQj.jKUp7.DhRcB").click()
        time.sleep(3)
        driver.find_element_by_css_selector("#react-root > section > main > div > div > div > div > button").click()
        time.sleep(1)
        driver.get(url)
        time.sleep(1)
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
    # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
            time.sleep(0.5)

    # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        body = str(driver.page_source)
        driver.close()
        #print(body)
        while (body.find("srcset",index_start) != -1 and body.find("240w,",index_start) != -1):
            index_start = body.find("srcset",index_start)+8
            #print(index_start)
            if body.find("150w",index_start) != -1:
                index_start = body.find("150w,",index_start)+5
            else:
                break
            if body.find("240w",index_start) != -1:
                index_end = body.find("240w,",index_start)-1
            else:
                break
            photo_url.append(body[index_start:index_end])
        if not id in os.listdir():
            os.mkdir(id)
            os.chdir(id)
        else:
            os.chdir(id)
        for i in range(len(photo_url)):
            photo_url[i] = photo_url[i].replace("amp;","")
            print(photo_url[i])
            with open(id + "_" + str(i) + ".jpg",'wb') as f:
                f.write(requests.get(photo_url[i]).content)
    else:
        while (body.find("src",index_start)!=-1):
            index_start = body.find("src",index_start)+ 6
            index_end = body.find("\"",index_start)
            photo_url.append(body[index_start:index_end])
        if not id in os.listdir():
            os.mkdir(id)
            os.chdir(id)
        else:
            os.chdir(id)
        for i in range(2, len(photo_url)-8, 6):
            photo_url[i] = photo_url[i].replace("\\u0026","&")
            #print(photo_url[i])
            with open(id + "_" + str(i) + ".jpg",'wb') as f:
                f.write(requests.get(photo_url[i]).content)
    os.chdir("..")
    model = tf.keras.models.load_model("model.h5", custom_objects={'KerasLayer':hub.KerasLayer})
    predict = []
    for i in os.listdir(id):
        img = np.array(Image.open(id+ "\\" +i))/255.0
        img = img.reshape(1,img.shape[0],img.shape[1],img.shape[2])
        predict.append(get_string(np.argmax(model.predict(img))))
    msg = QMessageBox()
    msg.setWindowTitle("Результат")
    
    #msg.setWindowIcon(QtGui.QIcon("vk_test.png"))
    msg.resize(200,200)
    if 'cadet' in predict:
        msg.setText("Военнослужащий или связан с военной службой")
    else:
        msg.setText("Не военнослужащий")
    msg.exec()



def group(driver, url):
    driver.get(url)
    time.sleep(1)
    try:
        driver.find_element_by_css_selector("#profile_idols > a > div").click()
    except NoSuchElementException:
        return 0
    group = driver.find_element_by_css_selector("#fans_rowsidols").text
    group = group.lower()
    if "армия" in group or "adecvation" in group or "курсант" in group or "казармем" in group or "курсанты" in group or "можайка" in group:
        return 1
    else:
        return 0

def api(url):
    token = 'fe4376b10059b99f985c66a2828211ab8908e205fb04d8e9f953b1071cfbdecc992b82cf1c9350e9588f9'
    VERSION_ID = "7605360"
    vk_session = vk_api.VkApi(token=token,api_version=vk_api.__version__,app_id=VERSION_ID)
    vk = vk_session.get_api()
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    photo = sniffer_with_api(vk,url,driver)
    social = group(driver, url)
    parce_open_source(driver, url)
    if photo == 0 and social == 0:
       print("Не военнослужащий")
    elif photo == 0 and social == 1:
       print("Военнослужащий или связанн с военной службой ")
    elif photo == 1 and social == 0:
       print("Военнослужащий или связаен с военной службой ")
    elif photo == 1 and social == 1:
       print("Военнослужащий")
    


if __name__ == '__main__':
    urls = parse_vk(image_url)
    for i in urls:
        api(i)

