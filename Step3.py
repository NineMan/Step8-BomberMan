"""
Взаимодействие двух объектов.

Здесь задание - описать функцию взаимодействия:
- игрока и монеты
- ударной волны c игроком или мягкой стеной

Чтобы два объекта провзаимодействовали друг с другом добавьте их пару в список interactions.
Я дарю вам немного кода. Посмотрите на него внимательно и постарайтесь понять, что он делает.

Напишите функции player_interaction и wave_interaction.
Когда игрок взаимодействует с монеткой, то монетка исчезает.
Когда ударная волна взаимодействует с мягкой стеной 'soft_wall' или игроком,
то стена или игрок исчезают.
Смотрите предыдущую задачу, там написано куда нужно добавить игровые объекты, чтобы их удалить.
"""


game_objects = {
    ('wall', 0): {'position': (0, 0), 'passable': False, 'interactable': False, 'char': '#'},
    ('wall', 1): {'position': (0, 1), 'passable': False, 'interactable': False, 'char': '#'},
    ('player',): {'position': (1, 1), 'passable': True, 'interactable': True, 'char': '@', 'coins': 0},
    ('soft_wall', 11): {'position': (1, 4), 'passable': False, 'interactable': True, 'char': '%'}
}


def player_interaction(player, obj):
    # if obj[0] in ['coin',]:
    if 'coin' in obj:
        old_objects.append(obj)


def wave_interaction(wave, obj):
    # if obj[0] in ['player', 'soft_wall']:
    if 'player' in obj and 'soft_wall' in obj:
        old_objects.append(obj)


def idle_interaction(o1, o2):
    pass


def process_interactions():
    for obj1, obj2 in interactions:
        print(obj1)
        print(obj2)
        interaction_funs.get(obj1[0], idle_interaction)(obj1, obj2)
        interaction_funs.get(obj2[0], idle_interaction)(obj2, obj1)
    interactions.clear()


interaction_funs = {
    'player': player_interaction,
    'heatwave': wave_interaction,
}
interactions = [(('player',), ('coin', 2)), (('player',), ('coin', 3))]
old_objects = []


print(interactions)
process_interactions()
print(interactions)



