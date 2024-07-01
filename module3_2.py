words = ['.ru', '.com', '.net']


def send_email(message, sender='university.help@gmail.com', *, recipient):
    if not ('@' in recipient and any(word.lower() in str(recipient).lower() for word in words)):
        if not ('@' in sender and any(word.lower() in str(sender).lower() for word in words)):
            return f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.'
    elif recipient == sender:
        return f'Невозможно отправить письмо самому себе.'
    elif sender == 'university.help@gmail.com':
        return f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.'
    else:
        return f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.'


print(send_email('FFFFF', recipient='yashindmitry5@gmail.com'))
