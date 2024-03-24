# Реализовать язык HTML-тегов с помощью менеджера контекста.


from contextlib import contextmanager


class HTML:
    def __init__(self):
        self.markup = ''
        self.indent = 0

    def __add_line(self, line):
        self.markup += '\t' * self.indent + line

    @contextmanager
    def body(self):
        try:
            self.__add_line('<body>\n')
            self.indent += 1
            yield self.markup
        finally:
            self.indent -= 1
            self.__add_line('</body>\n')

    @contextmanager
    def div(self):
        try:
            self.__add_line('<div>\n')
            self.indent += 1
            yield self.markup
        finally:
            self.indent -= 1
            self.__add_line('</div>\n')

    def p(self, inner: str):
        self.__add_line(f'<p>{inner}</p>\n')

    def get_code(self):
        return self.markup


def main():
    html = HTML()
    with html.body():
        with html.div():
            with html.div():
                html.p('Первая строка.')
                html.p('Вторая строка.')
            with html.div():
                html.p('Третья строка.')

    print(html.get_code())


if __name__ == '__main__':
    main()
