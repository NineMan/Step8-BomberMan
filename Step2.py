"""
Удаление объекта по списку old_objects

Чтобы удалить игровой объект, поместите его в список old_objects.
Напишите функцию remove_objects, которая будет удалять из game_objects те элементы,
которые есть в списке old_objects.
Не надо падать, если объект уже был удален.
Не забудьте очистить список old_objects, после того как обработаете его.
"""


game_objects = {
    ('wall', 0): {'position': (0, 0), 'passable': False, 'interactable': False, 'char': '#'},
    ('wall', 1): {'position': (0, 1), 'passable': False, 'interactable': False, 'char': '#'},
    ('player',): {'position': (1, 1), 'passable': True, 'interactable': True, 'char': '@', 'coins': 0},
    ('soft_wall', 11): {'position': (1, 4), 'passable': False, 'interactable': True, 'char': '%'}
}


def remove_objects():
    for obj in old_objects:
        game_objects.pop(obj, None)
    old_objects.clear()


old_objects = [('player', )]
remove_objects()

for _ in game_objects:
    print(_, ': ', game_objects[_])
print('old_objects: ', old_objects)

# assert not ('player', ) in game_objects
# assert not old_objects

print('----')
for i in game_objects:
    print(i[0])
print('----')
print(game_objects.keys())
