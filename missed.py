import random
import termcolor
from termcolor import colored, cprint
import time #обычные модули

x=" " #пробел сделал

mylist = ["spread", "desync", "death", "occlusion", "prediction error", "resolver"] #сам список со словами

print(colored("one", 'red') + "tap" + x + "lore:") #красным пишет ван и обычный тап лор
time.sleep(0.5) #засыпает на половину сек
print("missed shot due to" + x + random.choice(mylist)) #пишет миссед шут дуе ту и добавляет что то из списка
print("") #типо как отступ
print("ezzz dog owned by" + x + colored("trash#3228", 'magenta')) #ну тут понятно