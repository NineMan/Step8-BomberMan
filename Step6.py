"""
Загрузка уровня

Функция create_object довольна простая, поэтому я даю её вам просто так.

obj_types_to_char = {
    "player": "@", "wall": '#', 'soft_wall': '%', 'heatwave': '+', "bomb": '*', "coin": '$'
}


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
Что вам нужно сделать, так это написать функцию load_level,  которая будет принимать на вход строку с описанием уровня и инициализировать словарь game_objects вызывая нужное число раз create_object и add_new_objects. Игнорируйте пустые строки. Не забудьте очистить game_objects перед загрузкой.

level_example = '''
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
'''

load_level(level_example)
assert get_objects_by_coords((0,0)) == [('wall', 0)]
"""


game_objects = {
    ('wall', 0):       {'position': (0, 0), 'passable': False, 'interactable': False, 'char': '#'},
    ('wall', 1):       {'position': (0, 1), 'passable': False, 'interactable': False, 'char': '#'},
    ('player',):       {'position': (1, 1), 'passable': True,  'interactable': True,  'char': '@', 'coins': 0},
    ('soft_wall', 11): {'position': (1, 4), 'passable': False, 'interactable': True,  'char': '%'},
    # ('bomb', 0):       {'position': (1, 5), 'passable': True,  'interactable': True,  'lifetime': 5},
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

new_objects = []
objects_ids_counter = 0


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


load_level(level_example)
print('-----')
for i in game_objects:
    print(i, game_objects[i])

# assert get_objects_by_coords((0,0)) == [('wall', 0)]
