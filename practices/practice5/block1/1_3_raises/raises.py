class MealyError(Exception):
    pass


class raises:
    def __init__(self, exception_type):
        self.exception_type = exception_type

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            raise AssertionError(f"{self.exception_type.__name__} not raised")
        if issubclass(exc_type, self.exception_type):
            return True
        else:
            raise exc_value


try:
    with raises(MealyError) as e:
        pass
except AssertionError as e:
    print(e)