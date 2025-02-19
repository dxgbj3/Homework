import time

def countdown(n):
    while n > 0:
        print('Осталось:', n, 'секунд...')
        time.sleep(1)
        n -= 1
    print('Время вышло!')


a = int(input('Введите количество секунд: '))
countdown(a)