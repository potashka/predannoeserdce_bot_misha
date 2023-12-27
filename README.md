# Telegram-Бот АНО "Преданное сердце" | Команда Михаила

*Телегам бот, который помогает команде приюта в общении с посетителями и неравнодушными людьми которые поддерживают приют "Преданное сердце".*

## Оглавление
- Возможности
- Команда
- Используемый стек
- Архитектура проекта
- Функциональные цели проекта  
- Требования
- Инструкция по развёртыванию проекта локально
- Инструкция по развёртыванию проекта в контейнерах
- Как запустить тесты
- Рекомендации для разработчиков
- Видеогайд по админке

## Основные возможности бота
- Ответы на частые вопросы посетителей
- Сбор пожертвовании, путем перевода пользователей на страницу с формой
- Перевод на страницу где можно взять котика домой
- Задать вопрос администратору приюте через ТГ
- Сбор контактов людей готовых помочь приюту
- Рассылка сообщений и напоминании всем пользователям бота с фильтром по времени регистрации
- Выгрузка контактных данных людей помогающих приюту для информирования через телефон или email

## Команда
- [Михаил Приселков](https://github.com/BaronFAS "Github page")
- [Roman Tarasenko](https://github.com/tarrim80)
- [Николай Каменский](https://github.com/Rolicat)
- [Алексей Потанин](https://github.com/potashka)
- [Павел Гришанов](https://github.com/nabjiyxxa)
- [Сергей Сабирзянов](https://github.com/Comsomolec)

## Технологии
- Python 3.11
- Django 5.0
- Django REST framework 3.14.0
- Python-telegram-bot 20.7 (ассинхронная)
- Black 23.11.0

## Архитектура проекта

[Блох схема архитектуры в фигма](https://www.figma.com/file/QdebLowg51UKA6qmNXpGyg/predannoeserdce?type=whiteboard&node-id=0%3A1&t=WFJsoxsVOsZ0SRbu-1)

### Основные директории проекта:
 Корневая директория - содержит основную информацию о проекте и для деплоя
 backend - все папки проекта Django, dokerfile, зависимости
 tg_bot - все файлы для работы бота + docker-compose.yml для отдельного запуска бота при необходимости
 gateway - настройки для прокси-сервера nginx
 
### Документация к api:
Доступна после запуска проекта по адресам:
`../api/redoc/`
`../api/swagger/`


## Функциональные цели проекта

1. Предоставление информации: Бот может предоставлять информацию о животных, находящихся в приюте, их истории, возрасте, характере, а также о процессе усыновления.
2. Обратная связь: Возможность для пользователей задавать вопросы и получать обратную связь от бота по поводу процесса усыновления, волонтерства или пожертвований.
3. Уведомления и напоминания: Бот может отправлять уведомления о мероприятиях, акциях, мероприятиях по сбору средств и других событиях, связанных с приютом.
4. Поддержка волонтеров: Предоставление информации о возможностях волонтерской деятельности, регистрация на мероприятия и координация действий волонтеров.
5. Пожертвования: Возможность совершения пожертвований через бота, а также информация о текущих потребностях приюта.

 **Итого:** На 30.12.23 по пунктам 1-3 цели достигнуты, 4-5  запланированы.

## Требования для запуска
**Операционная система:** Сервер должен быть установлен на базе Linux, такой как Ubuntu, CentOS, Debian или другие

**Процессор и память:** Многоядерный процессор с тактовой частотой от 2.0 ГГц и выше, оперативная память от 4 Гб и выше

**Жесткий диск или SSD:** Минимальный объем хранилища данных для установки ОС и программного обеспечения составляет примерно 20 ГБ

## Запуск проекта локально

Клонировать репозиторий:
```
git clone
```

### 1. Запуск TG бота

Перейти в папку tg_bot
```
cd tg_bot
```

Создать файл .env и заполнить его по образцу из файла .env.exapmple
```
code .env
```

Cоздать и активировать виртуальное окружение:
```
python -m venv .venv
```
```
source venv/scripts/activate
```

Установить зависимости из файла requirements.txt
```
pip install -r requirements.txt
```

Обновить pip
```
python -m pip install --upgrade pip
```

Запустить bota:

```
python main.py
```

### 2. Запуск админки

Перейти в папку backend
```
cd backend
```

Создать файл .env и заполнить его по образцу из файла .env.exapmple
```
code .env
```

Cоздать и активировать виртуальное окружение (если активировано виртуальное окружение для tg_bot отключить его командой `deactivate`):
```
python -m venv .venv
```
```
source venv/scripts/activate
```

Установить зависимости из файла requirements.txt
```
pip install -r requirements.txt
```

Обновить pip
```
python -m pip install --upgrade pip
```

Перейти в папку backend/devoted_heart
```
cd devoted_heart
```

Создать миграции:
```
python manage.py makemigrations
```

Выполнить миграции:
```
python manage.py migrate
```

Запустить проект:
```
python manage.py runserver
```

## Запуск проекта в docker

Клонировать репозиторий:
```
git clone
```

Создать файл .env и заполнить его по образцу из файла .env.exapmple
```
code .env
```

Запустить скрипт deploy.sh
```
sudo ./deploy.sh
```

## Запуск тестов

В запущенном виртуальном окружении перейти в папку backend/devoted_heart и выполнить:
```
python manage.py test
```

## Рекомендации для разработчиков

### Соглашение о наименование веток:
- Указываем баг или фича, bot или django и название таски (можно не полностью, достаточно что бы было понятно).
- После того как пул реквест принят ветку обязательно удаляем.
- Мержим ветки от dev, пул реквесты делаем в dev. В master только готовый и протестированный код.

Например:
- feature/bot/task_name_one
- bug/django/task_name_two

### Стиль кода
- Строковые литералы: используем двойные кавычки (")
- Именование переменных: 
	- Используйте нижние подчеркивания для разделения слов в именах переменных (например, user_fullname).
	- Имена переменных должны быть осмысленными и описательными, отражая их предназначение.
- Отступы и пробелы: 
	- Используйте отступы в 4 пробела для каждого уровня отступа.
	- Размещайте пробелы вокруг операторов (например, x = 5, а не x=5).
- Комментарии и документация: избегаем использования комментариев, для всех функций желательно использовать docstring

## Видеогайд по админке
[Смотреть на ю-туб](https://youtu.be/t_DRf-7WP7A)

