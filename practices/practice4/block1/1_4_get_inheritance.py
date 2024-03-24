# Напишите функцию-однострочник get_inheritance для вывода строки,
# отражающей иерархию наследования для входного класса.


def get_inheritance(cls: object):
    return ' -> '.join([parent.__name__ for parent in cls.mro()])


print(get_inheritance(OSError))
