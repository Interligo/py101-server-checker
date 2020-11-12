'''
Напиши скрипт для мониторинга доступности произвольного сервиса. В случае, если сервис становится недоступен,
скрипт отправляет SMS-сообщение на твой номер. Сервисом может быть любой сайт или сервер (даже наш учебный).
Опрашивай сервис каждые 60 секунд.
'''


def course_server_checker():
    # setting up logs
    logging.basicConfig(filename='python101_course_server_checker.log',
                        level=logging.INFO,
                        format='%(levelname)s %(asctime)s %(message)s')

    response = requests.get('https://python101.online')

    if not response.ok:
        global app_working
        app_working = False
        return send_sms('Python 101 server is down.')


if __name__ == '__main__':
    import logging
    import requests
    from time import sleep

    from send_sms import send_sms

    app_working = True

    while app_working:
        course_server_checker()
        sleep(60)
