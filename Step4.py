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
"""


game_objects = {
    ('wall', 0): {'position': (0, 0), 'passable': False, 'interactable': False, 'char': '#'},
    ('wall', 1): {'position': (0, 1), 'passable': False, 'interactable': False, 'char': '#'},
    ('player',): {'position': (1, 1), 'passable': True, 'interactable': True, 'char': '@', 'coins': 0},
    ('soft_wall', 11): {'position': (1, 4), 'passable': False, 'interactable': True, 'char': '%'},
    ('coin', 2): {'position': (1, 2), 'passable': True, 'interactable': True, 'char': '$'},
    ('wall', 2): {'position': (1, 2), 'passable': True, 'interactable': False, 'char': '#'},
}


def get_objects_by_coords(position):
    answer = []
    for cell in game_objects:
        if game_objects[cell]['position'] == position:
            answer.append(cell)
    return answer


def move_objects():
    move = True
    for i in movements:
        objs = get_objects_by_coords(i[1])
        if not objs:
            game_objects[i[0]]['position'] = i[1]
        else:
            for obj in objs:
                if not game_objects[obj]['passable']:
                    move = False
            if move:
                game_objects[i[0]]['position'] = i[1]
                for k in objs:
                    interactions.append((i[0], k))

    print('interactions =', interactions)
    movements.clear()


# movements = [(('player', ), (0, 1))]
# move_objects()
# print(game_objects[('player', )]['position'])   # == (1, 1)
# print(game_objects[('player', )])   # == (1, 1)


interactions = []
movements = [(('player', ), (1, 2))]
move_objects()
# print(game_objects[('player', )]['position'])   # == (1, 2)
# print(game_objects)   # == (1, 2)
# print(interactions)
# print(game_objects[('player', )])   # == (1, 2)

# movements = [(('player', ), (1, 3))]
# move_objects()
# print(game_objects[('player', )]['position'])   # == (1, 3)
# print(game_objects[('player', )])   # == (1, 3)


