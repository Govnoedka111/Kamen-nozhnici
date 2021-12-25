#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      gena1
#
# Created:     25.12.2021
# Copyright:   (c) gena1 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
if user_action == computer_action:
    print(f"Оба пользователя выбрали {user_action}. Ничья!!")
elif user_action == "камень":
    if computer_action == "ножницы":
        print("Камень бьет ножницы! Вы победили!")
    else:
        print("Бумага оборачивает камень! Вы проиграли.")
elif user_action == "бумага":
    if computer_action == "камень":
        print("Бумага оборачивает камень! Вы победили!")
    else:
        print("Ножницы режут бумагу! Вы проиграли.")
elif user_action == "ножницы":
    if computer_action == "бумага":
        print("Ножницы режут бумагу! Вы победили!")
    else:
        print("Камень бьет ножницы! Вы проиграли.")