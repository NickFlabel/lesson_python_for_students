# MVC -это архитектурный шаблон, организующий структуру приложий, разделяя
# их на три основных компонета: модель, контроллер и view

# Модель - бизнес-логику И данные приложения
# Модель имплементирует паттерн Observer


# Controller - управляет поведением приложения и взаимодействует с моделью, реагируя на
# действия пользователя. Имплементирует паттерн Стратегия

# View - представление - отвечает за визуализацию данных, в классической реализации
# подписывается на события модели и реагирует на ее изменения

# MVC Model 2 

# Модель - больше не Observer
# За связь между моделью и view отвечает controller

# MVC в Django это Model View Template (MVT) - 
# в качестве контроллера в Django выступает view, а в качестве view - template

# Python web frameworks

# Django - решение все в одном, Django предлагает не только непосредственно
# веб-фреймворк, но также много другого функционала - от способов работы
# с БД до полноценной административной панели для пользователей

# FastAPI - несколько более легковесный веб-фреймворк, 
# предлающий решения для создания API и с хорошей поддержкой асинхронности

# Flask - микро веб-фреймворк


# pip install django

# python -m django startproject <название проекта> 

# manage.py - точка входа

# Приложение - отдельный модуль проекта 
# Проект - все наше веб-приложение в целом

# python .\manage.py runserver <порт> - если порт не указан, то 8000

# python .\manage.py startapp <название приложения> - создание приложения

# python .\manage.py makemigrations - создание миграций

'''
>>> from my_app.models import BBoard
>>> b1 = BBoard(title="my_ad")
>>> b1
<BBoard: BBoard object (None)>
>>> b1.my_ad
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'BBoard' object has no attribute 'my_ad'
>>> b1.title
'my_ad'
>>> b1.save()
>>> b1.price = 1.7
>>> b1.save()
>>> b1
<BBoard: BBoard object (1)>
>>> b1.pk
1
>>> b2 = BBoard(title="next_ad")
>>> b2
<BBoard: BBoard object (None)>
>>> b2.pk
>>> b2.save() 
>>> b2.pk     
2
>>> BBoard.objects.all()
<QuerySet [<BBoard: BBoard object (1)>, <BBoard: BBoard object (2)>]>
>>> for obj in BBoard.objects.all():
...     print(obj)
... 
BBoard object (1)
BBoard object (2)
>>> BBoard.objects.filter(title="next_")  
<QuerySet []>
>>> BBoard.objects.filter(title="next_ad") 
<QuerySet [<BBoard: BBoard object (2)>]>
>>> BBoard.objects.get(pk=2)
<BBoard: BBoard object (2)>
>>> BBoard.objects.get(pk=3) 
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "C:\Users\SelinN\Documents\lesson\my_venv\Lib\site-packages\django\db\models\manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\SelinN\Documents\lesson\my_venv\Lib\site-packages\django\db\models\query.py", line 649, in get
    raise self.model.DoesNotExist(
my_app.models.BBoard.DoesNotExist: BBoard matching query does not exist.
>>> BBoard.objects.filter(title="next_")   
<QuerySet []>
>>> b2.delete()
(1, {'my_app.BBoard': 1})
'''


# python .\manage.py createsuperuser - создание администратора
