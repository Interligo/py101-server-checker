'''
Напиши скрипт для мониторинга доступности произвольного сервиса. В случае, если сервис становится недоступен,
скрипт отправляет SMS-сообщение на твой номер. Сервисом может быть любой сайт или сервер (даже наш учебный).
Опрашивай сервис каждые 60 секунд.
'''

from time import sleep

from send_sms import send_sms
from python101_course_server_checker import course_server_checker
from logger_settings import logging


if __name__ == '__main__':
    while True:
        if not course_server_checker():
            send_sms('Python 101 server is down.')
            logging.info('Python 101 server is down.')
            break
        else:
            sleep(60)
