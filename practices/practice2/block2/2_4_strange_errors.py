# Объясните поведение приведенного ниже кода.


lst = ['a', 'b', 'c']
lst += 'd'
print(lst)

lst = lst + 'd'  # Ошибка?!
print(lst)

lst += 42
print(lst)  # Ошибка?!
