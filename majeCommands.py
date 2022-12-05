import os, random, sys

from engine import commands, events, items, entity
import data

def updateScreen():
    data.x, data.y = os.get_terminal_size()
    data.title = f"""{' '*(data.x//2-25//2)} _____ _____    __ _____ 
{' '*(data.x//2-25//2)}|     |  _  |__|  |   __|
{' '*(data.x//2-25//2)}| | | |     |  |  |   __|
{' '*(data.x//2-25//2)}|_|_|_|__|__|_____|_____|"""

meCommand = commands.Command("Профиль|profile|me", "Показывает вашу статистику")
@meCommand.command
def me():
    data.clearScreen()
    data.statics(data.player)
    input(f"{' '*(data.x//2-29//2)}Нажмите Enter чтобы вернуться")
    data.clearScreen()

attackCommand = commands.Command("attack", "Отправиться в приключения")
@attackCommand.command
def attack():
    print(f"{' '*(data.x//2-(5+len(str(data.day)))//2)}ДЕНЬ {data.day}")
        
    health = random.randint(7,11)
    mob = entity.Entity(name = random.choice(data.names), health = health, maxHealth = health, damage = 1, xp = 20, lvl = 1, coins = 0, reqxp = 250, type = "Zombie", items = [], weapon = data.items["BaseSword"], armor = data.items["BaseArmor"], events = data.dispatcher)
        
    print(f"Путешествуя по миру вы наткнулись на моба {mob.name}, его статистика:", end = "\n\n")
    data.statics(mob)
    text = ''
    while mob.health > 0:
        updateScreen()
        if data.player.health <= 0:
            updateScreen()
            data.death()
            break
        print(f"""{' '*(data.x//2-(16+len(str(data.player.health))+len(str(data.player.maxHealth)))//2)}Ваше здоровье: {data.player.health}/{data.player.maxHealth}
{' '*(data.x//2-(12+len(mob.name)+len(str(mob.health))+len(str(mob.maxHealth)))//2)}Здоровье {mob.name}: {mob.health}/{mob.maxHealth}
""")
        print("""A - Атака
S - Защита""")
        print(f"Последние сделаное действие: {text}")
            
        action = input(f'[{data.player.name}:Действие] ').upper()
        if action == "A":
            youhit = data.player.hit(mob)
            hit = mob.hit(data.player)
            text = f"Нанесено {'нисколько' if youhit == -1 else youhit}, по вам ударили {'нисколько' if hit == -1 else hit}"
        if action == "S":
            if random.randint(0, 0) == 0:
                text = "Успешная защита!"
            else:
                hit = mob.hit(data.player)
                text = f"По вам ударили {'нисколько' if hit == -1 else hit}"
        data.clearScreen()
    else:
        kill = mob.deathEvent(data.player)
        kill = f"Вы убили {mob.name} и получили {kill['xp']:.2f} XP, {mob.coins} Coins и следующие предметы: {', '.join(map(lambda item: str(item), kill['items']))}"
        print(f"{chr(10)*(data.y//2-1)}{' '*(data.x//2-len(kill)//2)}{kill}")
        input(f"{' '*(data.x//2-30//2)}Нажмите Enter чтобы продолжить")
        data.clearScreen()
    data.day += 1

commands = commands.Commands(attackCommand, meCommand)