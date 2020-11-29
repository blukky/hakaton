# Star Trek

https://drive.google.com/file/d/1KvYa6icvMmRCs_6H96dbboZdGnN7AzbQ/view?usp=sharing

https://drive.google.com/file/d/1Q1I3gmlOhFko2dod69z8BjhC8p4dZJLj/view?usp=sharing


Бизнес кейс: при посещении банка идентифицировать клиента по фото и получить его финансовый профиль для того, чтобы предложить максимально подходящие ему продукты.
Задача: Создать решение, которое сможет:
- по фотографии найти человека в социальных сетях(VK,FB);
- получить максимальное количество данных по нему: фамилия, имя, отчество, номер телефона, e-mail и др;
- зная эти данные, из открытых источниках сформировать его финансовый профиль. 

# Установка

```
virtualenv venv --python=python3.8
source venv/bin/activate  
pip install django
python3 manage.py makemigrations app_pet 
python3 manage.py migrate   
python manage.py runserver 0.0.0.0:8888  
```
