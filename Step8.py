"""
Игровое состояние

Напишите функцию check_game_state, которая будет возвращать:

- "lose", если в игровых объектах нет игрока,
- "win", если нет ни одной монетки на поле
- "in_progress", в остальных случаях.

    game_objects = {}
    assert check_game_state() == 'lose'
"""


def get_next_counter_value():
    global objects_ids_counter
    result = objects_ids_counter
    objects_ids_counter += 1
    return result

def get_objects_by_coords(position):
    answer = []
    for cell in game_objects:
        if game_objects[cell]['position'] == position:
            answer.append(cell)
    return answer

def add_new_objects():
    for name, props, position in new_objects:                       # получаю тройку нового объекта
        obj = get_objects_by_coords(position)
        if obj:
            for obj in get_objects_by_coords(position):             # для объектов с координатами как у нового объекта
                if game_objects[obj]['interactable']:               # если есть объекты с interactible == True
                    props['position'] = position                    # то добавляем в свойства позицию
                    game_objects[(name, get_next_counter_value())] = props  # и добавляем новый объект в game_objects
        else:
            props['position'] = position                            # то добавляем в свойства позицию
            game_objects[(name, get_next_counter_value())] = props  # и добавляем новый объект в game_objects

        # print('props =', props)

def create_object(type, position, **kwargs):
    desc = {'position': position,
            'passable': type not in ['wall', 'soft_wall'],
            'interactable': type not in ['wall'],
            'char': obj_types_to_char[type]
            }
    if type == 'player':
        desc['coins'] = 0
    if type == 'bomb':
        desc['power'] = 3
        desc['life_time'] = 3
    desc.update(kwargs)
    return type, desc, position

def char_to_obj_types(new_char):
    for key, value in obj_types_to_char.items():
        if value == new_char:
            return key

def load_level(level):
    game_objects.clear()
    level = level.strip().splitlines()
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] != ' ':
                type = char_to_obj_types(level[y][x])
                position = (y, x)
                new_object = create_object(type, position)
                new_objects.append(new_object)
    add_new_objects()

def remove_objects():
    for obj in old_objects:
        game_objects.pop(obj, None)
    old_objects.clear()

def idle_logic(_):
    pass

def process_objects_logic():
    for game_object in game_objects:
        object_logics.get(game_object[0], idle_logic)(game_object)

def bomb_logic(bomb_object):
    game_objects[bomb_object]['life_time'] -= 1
    if game_objects[bomb_object]['life_time'] <= 0:
        # Вношу бомбу в список на удаление
        old_objects.append(bomb_object)
        # Создаю пять волн на месте бомбы и по соседству
        (x, y) = game_objects[bomb_object]['position']
        new_objects.append(create_object('heatwave', (x, y)))
        new_objects.append(create_object('heatwave', (x + 1, y)))
        new_objects.append(create_object('heatwave', (x - 1, y)))
        new_objects.append(create_object('heatwave', (x, y + 1)))
        new_objects.append(create_object('heatwave', (x, y - 1)))

def heatwave_logic(heatwave):
    old_objects.append(heatwave)

def check_game_state():
    player, coin = False, False
    for obj in game_objects:
        if obj[0] == 'player':
            player = True
        if obj[0] == 'coin':
            coin = True
    if not player:
        return 'lose'
    if not coin:
        return 'win'
    return 'in_progress'

'''    
    if ('player', ) not in game_objects:
        return 'lose'
    # else:
    coin_in_game = False
    for i in game_objects:
        if i[0] == 'coin':
            coin_in_game = True
    if coin_in_game:
        return 'in_progress'
    # else:
    return 'win'
'''

# game_objects = {}
game_objects = {
    ('wall', 0):       {'position': (0, 0), 'passable': False, 'interactable': False, 'char': '#'},
    ('wall', 1):       {'position': (0, 1), 'passable': False, 'interactable': False, 'char': '#'},
    # ('player',):       {'position': (1, 1), 'passable': True,  'interactable': True,  'char': '@', 'coins': 0},
    ('soft_wall', 11): {'position': (1, 4), 'passable': False, 'interactable': True,  'char': '%'},
    ('bomb', 0):       {'position': (1, 5), 'passable': True,  'interactable': True,  'life_time': 0},
    ('coin', 0): {'position': (1, 5), 'passable': True, 'interactable': True, 'life_time': 0},
}

level_example = """
##########
#@  %    #
#   %    #
#  %%%   #
# %%$%%  #
#  %%%   #
#   %    #
#   %    #
#   %    #
##########
"""

obj_types_to_char = {
    "player": "@", "wall": '#', 'soft_wall': '%', 'heatwave': '+', "bomb": '*', "coin": '$'
}

object_logics = {
    'bomb': bomb_logic,
    'heatwave': heatwave_logic
}

old_objects = []
new_objects = []
objects_ids_counter = 0


# ------------------------------------

# print('---')
print(check_game_state())
# process_objects_logic()

# process_objects_logic()
# add_new_objects()
# remove_objects()

# check_game_state()

# for i in game_objects:
#     print(i, ': ', game_objects[i])

