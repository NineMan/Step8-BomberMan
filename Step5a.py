"""
Создание новых объектов.

Давайте теперь научимся создавать объекты.

В списке new_objects хранятся тройки: тип объекта, словарь со всеми его аттрибутами и координаты.
Напишите функцию add_new_objects, которая будет добавлять эти объекты в список game_objects, если это возможно.
Вы не можете поставить объект, если место занято объектом c аттрибутом interactable == False.

Помните, что у всех ключей в game_objects, кроме игрока, есть второй элемент - число.
С изменением значений чисел, которые объявлены глобально есть небольшая хитрость, которую вам пока не рассказывали.
Но вы можете все изучить самостоятельно.
А пока просто вызывайте функцию get_next_counter_value:

    objects_ids_counter = 0

    def get_next_counter_value():
        global objects_ids_counter
        result = objects_ids_counter
        objects_ids_counter += 1
        return result
"""


game_objects = {
    ('wall', 0):       {'position': (0, 0), 'passable': False, 'interactable': False, 'char': '#'},
    ('wall', 1):       {'position': (0, 1), 'passable': False, 'interactable': False, 'char': '#'},
    ('player',):       {'position': (1, 1), 'passable': True,  'interactable': True,  'char': '@', 'coins': 0},
    ('soft_wall', 11): {'position': (1, 4), 'passable': False, 'interactable': True,  'char': '%'},
    # ('bomb', 0):       {'position': (1, 5), 'passable': True,  'interactable': True,  'lifetime': 5},
}


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
    for name, props, position in new_objects:           # получаю тройку нового объекта
        obj = get_objects_by_coords(position)
        if obj:
            for obj in get_objects_by_coords(position):    # для объектов с координатами как у нового объекта
                if game_objects[obj]['interactable']:      # если есть объекты с interactible == True
                    props['position'] = position            # то добавляем в свойства позицию
                    game_objects[(name, get_next_counter_value())] = props  # и добавляем новый объект в game_objects
        else:
            props['position'] = position            # то добавляем в свойства позицию
            game_objects[(name, get_next_counter_value())] = props  # и добавляем новый объект в game_objects

        print('props =', props)


objects_ids_counter = 0
new_objects = [
    ('bomb', {'passable': True, 'interactable': True, 'lifetime': 5}, (1, 1)),
    ('bomb', {'passable': True, 'interactable': True, 'lifetime': 5}, (1, 5)),
]
add_new_objects()
print('----------')
for _ in game_objects:
    print(_, game_objects[_])
# print('----------')
# print(get_objects_by_coords((1, 1)))

# assert get_objects_by_coords((1, 1)) == [('player', ), ('bomb', 0)]