#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      gena1
#
# Created:     24.12.2021
# Copyright:   (c) gena1 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
from playsound import *
from datetime import *


def validate_time(alarm_time):
    if len(alarm_time) != 8:
        return 'Неверный формат, попробуйте заново'
    else:
        if int(alarm_time[0:2]) > 23:
            return 'Неверный фомат часов, попробуйте заново'
        elif int(alarm_time[3:5]) > 59:
            return 'Неверный фомат минут, попробуйте заново'
        elif int(alarm_time[6:8]) > 59:
            return 'Неверный фомат секунд, попробуйте заново'
        else:
            return 'Хорошо!'

while True:
    alarm_time = input('Введите имя вследующем формате \'НН:ММ:SS\'\nВремя будильника: ')
    validate = validate_time(alarm_time)
    if validate != 'Хорошо!':
        print(validate)
    else:
        print(f"Будильник установлен на время {alarm_time}...")
        break

alarm_hour = int(alarm_time[0:2])
alarm_min = int(alarm_time[3:5])
alarm_sec = int(alarm_time[6:8])

while True:
    now = datetime.now()

    current_hour = now.hour
    current_min = now.minute
    current_sec = now.second

    if alarm_hour == current_hour:
        if alarm_min == current_min:
            if alarm_sec == current_sec:
                print('Подъем')
                playsound('C:/Пользователи/gena1/Загрузки/1.mp3')
                break


