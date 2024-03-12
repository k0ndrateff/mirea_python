# Напишите код, состоящий из двух модулей, для получения
# следующего сообщения об ошибке:
#
# AttributeError: partially initialized module '...' has no attribute '...'
# (most likely due to a circular import)


from second_module import another_var

some_var = 42
