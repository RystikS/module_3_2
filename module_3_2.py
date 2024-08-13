def send_email(message, recepient, sender="university.help@gmail.com"):
    if ("@" not in (recepient or sender)) or (recepient.endswith(".com" or ".ru" or ".net") or sender.endswith(".com" or ".ru" or ".net")):
        print (f"Невозможно отправить письмо с адреса {sender} на адрес {recepient}")
        return
    if sender == recepient:
        print("Нельзя отправить письмо самому себе!")
        return
    if sender=="university.help@gmail.com":     print (f"Письмо успешно отправлено с адреса {sender} на адрес {recepient}")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recepient}.")
        

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')