﻿class MainMessage:
    START = (
        "Привет, я кот Фуражкин, "
        "могу рассказать вам про приют для животных «Преданное сердце»"
    )
    MENU_BTN = "Для возврата в главное меню нажмите кнопку"
    MENU = "Сейчас вы в меню, выберите что вы хотите узнать"
    ALERT_MSG = (
        "Извините, это сообщение я пока не понимаю :( \n"
        "Если хотите задать мне вопрос - выберите в меню "
        'раздел "Частые вопросы"'
    )
    FAQ = "Выберите вопрос, который вас интересует:"
    URL = "Нажмите на кнопку, чтобы перейди на сайт."
    SERVER_ERROR = "Ошибка. Нажмите, чтобы сообщить администратору"


class ConversationTextMessage:
    COMMUNICATION_WAY = "Выберите способ общения:"
    WRITE_FULLNAME = "Пожалуйста, представьтесь. \nНапишите Имя и Фамилию."
    WRITE_EMAIL = "Приятно познакомиться!\nТеперь напишите свой e-mail."
    WRITE_PHONE = (
        "Напишите номер своего телефона в формате 7ХХХХХХХХХХ или 8XXXXXXXXXX."
    )
    WRITE_SUBJECT = "Введите тему сообщения."
    WRITE_QUESTION = (
        "Отправьте своё сообщение.\n"
        "Соблюдайте вежливость, а не то я поцарапаю."
    )
    SEND_QUESTION_TG = (
        "Спасибо!\nВаш вопрос отправлен и будет рассмотрен в рабочее время.\n"
        "Скоро вы получите ответ, а пока посмотрите котиков."
    )
    SEND_QUESTION_EMAIL = (
        "Спасибо!\n"
        "Ваш вопрос отправлен и будет рассмотрен в ближайшее время.\n"
        "Ответ вы получите на указанный вами ящик электронной почты,\n"
        "а пока ждёте  - посмотрите котиков."
    )
    CANCEL = "Жаль, что передумали.\nВы сможете %s в любой момент."
    ANSWER_FROM_ADMIN = (
        "<b>На ваш вопрос поступил ответ от администратора:</b>\n\n"
        "%s\n\n\n"
        "<i>Пожалуйста, не отвечайте на это сообщение. Если вы хотите задать "
        "новый вопрос, выберите в меню пункт Частые вопросы.</i>"
    )
    ANSWER_BY_FAQ = "<b>Вопрос:\n</b>%s\n\n<b>Ответ:\n</b>%s"
    SERVER_ERROR = "Произошла ошибка в работе бота. Сообщите в поддержку"
    ERROR_THANKS = "Спасибо! Благодаря вам скоро мы всё исправим!"
    INVALID_FULLNAME = (
        "Неверный ввод. \n"
        "Убедитесь, что вы вписываете Имя и Фамилию кириллицей"
    )
    INVALID_EMAIL = (
        "Неверный ввод. \n"
        "Убедитесь, что вы вписываете свой Email в правильном формате\n"
        "например: user@example.com"
    )
    INVALID_PHONE = (
        "Неверный ввод. \n"
        "Убедитесь, что вы вписываете номер телефона\n"
        "состоящий из 11 цифр\nв формате 7XXXXXXXXXX или 8XXXXXXXXXX"
    )
    USER_ADD_TO_BAN = "Пользователь id:%s добавлен в чёрный список"
    USER_EXIST_AT_BAN = (
        "К сожалению, вы не можете задать вопрос.\n"
        "Зато можете посмотреть котиков"
    )


class BotLogMessage:
    SHOW_MENU_BTN = "Показана кнопка вызова главного меню"
    SHOW_MAIN_MENU = "Показано главное меню"
    UNKNOWN_MESSAGE = "Получено необрабатываемое сообщение: %s"
    PROCESSING_BTN = "Обработка кнопки `%s`"
    STUB_BTN = "Здесь должна быть обработка кнопки %s, но её пока нет"
    CREATE_MAIN_KB = "Создана основная клавиатура"
    REMOVE_KB = "Клавиатура удалена"
    CREATE_FAQ_KB = "Создана страница №%s клавиатуры частых вопросов"
    UNKNOWN_ERROR = "Что-то пошло не так! Ошибка: %s"
    SERVER_ERROR = "Ошибка получения данных с сервера: %s"
    UPDATE_FAQ_DICT = "Список частых вопросов обновлён"
    CREATE_CUSTOM_QUESTION_KB = "Создана клавиатура нового вопроса"
    CREATE_BACK_TO_FAQ_KB = "Создана кнопка возврата к частым вопросам"
    CREATE_SUBSCRIBE_KB = "Создана клавиатура подписки на рассылку"
    CREATE_TO_BAN_KB = "Создана клавиатура добавления в черный список"
    TOKEN_RECEIVED = "Токен успешно получен"
    USER_ADD_TO_BAN = "Пользователь id:%s добавлен в чёрный список"
    USER_EXIST_AT_BAN = (
        "Неудачная попытка общения. Пользователь id:%s в чёрном списке"
    )


class ConversationLogMessage:
    START = "Начато общение с пользователем id:%s"
    RECEIVED_FULLNAME = "Полное имя пользователя id:%s получено"
    RECEIVED_EMAIL = "Email пользователя id:%s получен"
    RECEIVED_PHONE = "Номер телефона пользователя id:%s получен"
    RECEIVED_SUBJECT = "Тема сообщения пользователя id:%s получена"
    RECEIVED_QUESTION = "Вопрос пользователя id:%s получен"
    INVALID_DATA = "Полученные данные %s не прошли проверку"
    SEND_QUESTION = "Вопрос пользователя id:%s отправлен администратору"
    END = "Общение с пользователем id:%s завершено"
    CANCEL = "Общение прервано пользователем id:%s"
    ANSWER_FROM_ADMIN = "Пользователю %s отправлен ответ администратора"
    ERROR_TO_ADMIN = "Сообщение об ошибке отправлено администратору"
    SUBSCRIBE_SUCCESS = "Пользователь id:%s успешно подписался на рассылку"
    SUBSCRIBE_ERROR = "Ошибка (%s) при попытке пользователя id:%s подписаться"
    UNSUSCRIBE_SUCCESS = "Пользователь id:%s успешно отписался от рассылки"
    UNSUBSCRIBE_ERROR = "Ошибка (%s) при попытке пользователя id:%s отписаться"


class PlaceholderMessage:
    MENU_BTN = "Нажмите кнопку для входа в меню"
    MAIN_MENU = "Выберите пункт меню"


class InlineButtonText:
    CUSTOM_QUESTION = "Задать другой вопрос"
    FIRST_PAGE = "<<  Перв."
    LAST_PAGE = "Посл.  >>"
    PREV_PAGE = "<  Пред."
    NEXT_PAGE = "След.  >"
    TELEGRAM_QUESTION = "Telegram"
    EMAIL_QUESTION = "Email"
    BACK_TO_FAQ = "Назад к вопросам"
    USER_TO_BAN = "Заблокировать пользователя"


class SubscribeTextMessage:
    USER_DATE = "Ваши данные:"
    DONE = (
        "<b>Мяу, вы успешно подписаны на рассылку сообщений.</b>\n"
        "Вот ваши данные:"
    )
    ERROR = "Мррр, что-то пошло не так:\n"
    UNSUBSCRIBE = "Вы успешно отписались от рассылки"


class DelayedQstnsTextMessage:
    SEND_START = "У вас есть непрочитанные сообщения."
    SEND_END = "На сегодня это все сообщения!"


class DelayedQstnsLogMessage:
    QUESTION_DELAYED = "Вопрос пользователя id:%s сохранён в отложенные"
    SEND_START = "Начата отправка отложенных сообщений."
    SEND_END = "Отправка сообщений окончена. Отложенные сообщения удалены."
