import os, random, sys

from engine import entity, items, events
import majeCommands, data

def updateScreen():
    data.x, data.y = os.get_terminal_size()
    data.title = f"""{' '*(data.x//2-25//2)} _____ _____    __ _____ 
{' '*(data.x//2-25//2)}|     |  _  |__|  |   __|
{' '*(data.x//2-25//2)}| | | |     |  |  |   __|
{' '*(data.x//2-25//2)}|_|_|_|__|__|_____|_____|"""

print(data.title)
print(f"{'-'*data.x}Приветствую путник, перед тем как начать играть в maje придумайте себе ник")

data.player = entity.Entity(name = input("Ваш ник: "), health = 100, maxHealth = 100, damage = 1, xp = 0, lvl = 1, coins = 0, reqxp = 250, type = "Player", items = [], weapon = data.items["BaseSword"], armor = data.items["BaseArmor"], events = data.dispatcher)
data.player.points = 0

print(f"{'-'*data.x}Хорошо {data.player.name}, да начнется игра!")

input(f"{chr(10)*(data.y//2-9)}{' '*(data.x//2-30//2)}Нажмите Enter чтобы продолжить")

data.clearScreen()

while True:
    updateScreen()
    print(data.title, end='\n' + '-'*data.x)
    print(f"{f'{chr(10)}'.join(map(lambda x: str(majeCommands.commands.showCommands[x]), majeCommands.commands.showCommands))}")
    
    option = input(f'[{data.player.name}:Выбор] ')
    data.clearScreen()
    try:
        majeCommands.commands.commands[option].function()
    except:
        pass