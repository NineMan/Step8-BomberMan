"""
Перемещение объекта из списка movements

Представлю следующую игровую структуру данных. Список movements хранит пары объект-новые координаты.
Если мы хотим переместить какой-то объект, мы добавляем соотвествующую пару в этот список.
Напишите функцию move_objects, которая будет провереять все пары в списке movements и перемещать объекты.
Переместить объект в заданные координаты можно только если там нет ни одного объекта,
у которого в описании аттрибут passable равен False.
Если объект перемещается в занятую клетку, то он взаимодействует с теми объектами, которые там уже находятся.
Добавьте соотвествующую пару в список interactions.

Не забудьте очистить список movements, после того как обработатете все пары оттуда.

Вы можете использовать функцию get_objects_by_coords, которую вы уже написали.

NOTE!!!
Данное решение не учитывает такую возможность:
    В точке куда двигается объект есть несколько объектов.
    Некоторые из них passable == True, другие passable == False
В этом решении - если есть хоть одно с True - игрок переместится и добавиться пара в interactions

"""


game_objects = {
    ('wall', 0): {'position': (0, 0), 'passable': False, 'interactable': False, 'char': '#'},
    ('wall', 1): {'position': (0, 1), 'passable': False, 'interactable': False, 'char': '#'},
    ('player',): {'position': (1, 1), 'passable': True, 'interactable': True, 'char': '@', 'coins': 0},
    ('soft_wall', 11): {'position': (1, 4), 'passable': False, 'interactable': True, 'char': '%'},
    ('coin', 2): {'position': (1, 2), 'passable': True, 'interactable': True, 'char': '$'},
    ('wall', 2): {'position': (1, 2), 'passable': False, 'interactable': False, 'char': '#'},
}


def get_objects_by_coords(position):
    answer = []
    for cell in game_objects:
        if game_objects[cell]['position'] == position:
            answer.append(cell)
    return answer


def move_objects():
    for obj1, point in movements:
        # print(obj1, point)
        for obj2 in get_objects_by_coords(point):
            # print(obj2)
            if game_objects[obj2]['passable']:
                interactions.append((obj1, obj2))
            else:
                point = game_objects[obj1]['position']
        game_objects[obj1]['position'] = point
    movements.clear()


interactions = []


# movements = [(('player', ), (0, 1))]
# move_objects()
# print(game_objects[('player', )]['position'])   # новые координаты player'a == (1, 1)
# print(game_objects)                             # весь список игровых объектов
# print(interactions)                             # список пар на взаимодействие
# print(game_objects[('player', )])               # свойства player'a


movements = [(('player', ), (1, 2))]
move_objects()
print(game_objects[('player', )]['position'])   # новые координаты player'a == (1, 2)
# print(game_objects)                             # весь список игровых объектов
print(interactions)                             # список пар на взаимодействие
# print(game_objects[('player', )])               # свойства player'a


# movements = [(('player', ), (1, 3))]
# move_objects()
# print(game_objects[('player', )]['position'])   # новые координаты player'a == (1, 3)
# print(game_objects)                             # весь список игровых объектов
# print(interactions)                             # список пар на взаимодействие
# print(game_objects[('player', )])               # свойства player'a
