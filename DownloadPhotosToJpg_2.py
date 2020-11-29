import shutil
import os
import requests
import codecs
import vk_api


def load_file(name, url):
    if not os.path.exists('jpg/' + str(name) + '.jpg'):
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open('jpg/' + str(name) + '.jpg', 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)


def get_photos_by_id(user_id_):
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
            if max_flag < 10:
                load_file(str(user_id_) + '_' + str(max_flag), photo)
    except Exception as ex:
        print(ex)

def downloadPhotos():

    token = 'fe4376b10059b99f985c66a2828211ab8908e205fb04d8e9f953b1071cfbdecc992b82cf1c9350e9588f9'
    VERSION_ID = "7605360"
    vk_session = vk_api.VkApi(token=token, api_version=vk_api.__version__, app_id=VERSION_ID)
    vk = vk_session.get_api()

    ff = codecs.open(u'ids.txt', 'r', encoding='utf8')

    e = 0
    for x in ff:
        e += 1
        print(e)
        mas = x.split('|')
        user_id = int(mas[0])
        get_photos_by_id(user_id)

ff.close()