import vk_api
import time
import codecs
from DownloadPhotosToJpg_2 import downloadPhotos
from JpgToNpy_3 import get_face_descriptorf
from FindIntoNpy_4 import find_face_vk
from NpyToEmbeddingsBin_5 import NpyToEbeding
from FindFaceInEmbeddingsBin_6 import print_url


def parse_vk(image_url):
    # Заходим ВКонтакте под своим логином
    token = 'fe4376b10059b99f985c66a2828211ab8908e205fb04d8e9f953b1071cfbdecc992b82cf1c9350e9588f9'
    VERSION_ID = "7605360"
    vk_session = vk_api.VkApi(token=token, api_version=vk_api.__version__, app_id=VERSION_ID)
    vk = vk_session.get_api()

    # Пишем возраст от и до людей которых надо спарсить
    age = 20
    age_max = 35

    # Номер города
    city_number = 104

    # 1 - девушки, 2 - парни
    gender = 2

    # Открываем файл для записи результатов
    ff = codecs.open('ids.txt', 'w', encoding='utf8')

    # Перебор возрастов

    while age <= age_max:
        month = 1
        # Перебор месяцев рождения
        while month <= 12:
            # Пауза для API
            time.sleep(4)
            # Пишем какую группу людей качаем
            print('Download ID: ' + str(age) + ' age, born in ' + str(month))
            # Получаем 1000 юзеров - их ФИО, айди, и фотку
            z = vk.users.search(count=2000,
                                fields='id, photo_max_orig, has_photo, '
                                       'first_name, last_name',
                                city=city_number,
                                sex=gender,
                                age_from=age,
                                age_to=age,
                                birth_month=month)
            month = month + 1
            print('Peoples count: ' + str(z['count']))
            for x in z['items']:
                if x['has_photo'] == 1:
                    # Записываем данные о юзере в файл разделяя черточкой |
                    s = str(x['id']) + '|' + str(x['photo_max_orig']) + '|' + str(
                        x['first_name']) + ' ' + str(x['last_name']) + '\n'
                    ff.write(s)
        age = age + 1

    ff.close()

    downloadPhotos()
    get_face_descriptor()
    find_face_vk(image_url)
    NpyToEbeding()
    urls = print_url(image_url)
    return urls