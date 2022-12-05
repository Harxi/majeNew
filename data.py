import os, sys

from engine import commands, entity, events, items

# GAME DATA

platform = {
    "win32": "cls",
    "linux": "clear"
}

dispatcher = events.Events()
day = 1
names = ['Орвутер', 'Анаель', 'Цраxьеикс', 'Бенгрун', 'Аомине', 'Мирилис', 'Гербальт', 'Могтаф', 'Исье', 'Мисса', 'Авоик', 'Круспас', 'Майнард', 'Тругомол', 'Гото', 'Могерун', 'Бисеаандер', 'Сенни', 'Хумфридус', 'Изабель', 'Дагдронун', 'Возал', 'Мацумото', 'Сеанайн', 'Илмаф', 'Радульф', 'Малик', 'Релгомод', 'Кетеаансиан', 'Лиеагмон', 'Захнатх', 'Шудулайс', 'Ройс', 'Сцекуин', 'Тазава', 'Цоуин', 'Брогтауч', 'Шимомура', 'Мункофан', 'Ходж', 'Загдрудач', 'Киасдиан', 'Гоин', 'Дерзукаф', 'Чолзол', 'Алис', 'Стеллид', 'Црааикс', 'Аделин', 'Араель', 'Иасутаке', 'Фонгрон', 'Друсеазал', 'Аедс', 'Гевеx', 'Аигфинс', 'Сагакет', 'Лоцрон', 'Отугоу', 'Рилгуерик', 'Канно', 'Ацур', 'Кигфеч', 'Илкоиx', 'Врернолея', 'Оргин', 'Иваиама', 'Велле', 'Хардуинус', 'Ингарет', 'Бригитта', 'Асмодей']

x, y = os.get_terminal_size()
title = f"""{' '*(x//2-25//2)} _____ _____    __ _____ 
{' '*(x//2-25//2)}|     |  _  |__|  |   __|
{' '*(x//2-25//2)}| | | |     |  |  |   __|
{' '*(x//2-25//2)}|_|_|_|__|__|_____|_____|"""

# ITEMS
items = {
    "BaseSword": items.Sword("Деревянный меч", "Меч оточеный в тренеровках", "base", 1, 0.08),
    "BaseArmor": items.Armor("Тряпки", "Тряпки, которые даже от мороза не спасут", "base", 0)
}

# FUNCTIONS

def clearScreen():
    os.system(platform[sys.platform])
    
def statics(user: entity.Entity):
    print(f"""Здоровье: {user.health}/{user.maxHealth}
Атака: {user.damage+user.weapon.damage}/{(user.damage+user.weapon.damage)*2}
Опыт: {user.xp:.2f}/{user.reqxp}
Предметы: {'Отсутствуют' if user.items == [] else ', '.join(map(lambda item: str(item), user.items))}
Оружие: {user.weapon}
Броня: {user.armor}
Уровень: {user.lvl}
Защита: {user.armor.armor}
Тип: {entity.entityTypes[user.type]}
""")
 
def death():
    clearScreen()
    print(f"{chr(10)*(y//2-1)}{' '*(x//2-9//2)}Вы умерли")
    input(f"{' '*(x//2-30//2)}Нажмите Enter чтобы продолжить")
    player.health = player.maxHealth
    player.coins = 0
    player.items = []
    clearScreen()