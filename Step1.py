"""
Возвращение списка объектов по заданным координатам.

Начнем с простого.
Напишите функцию get_objects_by_coords, которая будет возвращать список объектов,
которые находятся в заданных координатах.
"""


game_objects = {
    ('wall', 0): {'position': (0, 0), 'passable': False, 'interactable': False, 'char': '#'},
    ('wall', 1): {'position': (0, 1), 'passable': False, 'interactable': False, 'char': '#'},
    ('player',): {'position': (1, 1), 'passable': True, 'interactable': True, 'char': '@', 'coins': 0},
    ('soft_wall', 11): {'position': (1, 4), 'passable': False, 'interactable': True, 'char': '%'}
}


def get_objects_by_coords(position):
    answer = []
    for cell in game_objects:
        if game_objects[cell]['position'] == position:
            answer.append(cell)
    return answer


print(get_objects_by_coords((0, 1)))    # == [('wall', 1)]
print(get_objects_by_coords((1, 1)))    # == [('player',)]
print(get_objects_by_coords((2, 1)))    # == []
