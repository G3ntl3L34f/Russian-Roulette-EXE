import time
from random import randint
import webbrowser
import os
def game():
    global win
    num = randint(1, 6)
    print("выбери число от 1 до 6!")
    usernum = int(input())
    if num == usernum:
        win += 1
        if win == 3:
            print("Поздравляю! Ты выиграл 6 раз подряд!")
            print("Вот твой приз!")
            webbrowser.open("https://rutube.ru/video/b910a27415afe356775ffe868badb8df/?t=0")
            time.sleep(20)
            exit()
        print("Молодец! Ты угадал")
        print(f'Раунд {win} пройден, осталось {3-win}')
        game()
    if num != usernum:
        print("Ты не угадал (")
        print("Теперь я удалю system32 XD")
        time.sleep(1)
        for i in range(1, 100):
            print(f'Удаление завершено на {i} %')
            time.sleep(0.1)
        print("Ладно, я пошутил XD")
        time.sleep(3)
        os.system('shutdown -s')
win = 0

print("Привет! Это русская рулетка, если выиграешь 3 раза подряд - получишь приз! Готовы сыграть?")
print("Y/n")
s = input().lower()
if s == "n":
    exit()
if s =="y":
    game()
