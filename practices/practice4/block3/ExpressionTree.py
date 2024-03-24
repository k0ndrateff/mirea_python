# Требуется реализовать операции для печати, вычисления арифметических
# выражений и компиляции выражений в код стековой машины.


class Expression:
    def __init__(self, left_operand, right_operand):
        self.left = left_operand
        self.right = right_operand


class Num:
    def __init__(self, value: float):
        self.value = value


class Add(Expression):
    def __init__(self, left: Num or Expression, right: Num or Expression):
        super().__init__(left, right)


class Mul(Expression):
    def __init__(self, left: Num or Expression, right: Num or Expression):
        super().__init__(left, right)


class PrintVisitor:
    def visit(self, ast: Num or Expression) -> str:
        if isinstance(ast, Num):
            return str(ast.value)
        else:
            if isinstance(ast, Add):
                return f'({self.visit(ast.left)} + {self.visit(ast.right)})'
            elif isinstance(ast, Mul):
                return f'({self.visit(ast.left)} * {self.visit(ast.right)})'


class CalcVisitor:
    def visit(self, ast: Num or Expression) -> float:
        if isinstance(ast, Num):
            return ast.value
        elif isinstance(ast, Add):
            return self.visit(ast.left) + self.visit(ast.right)
        elif isinstance(ast, Mul):
            return self.visit(ast.left) * self.visit(ast.right)


def main():
    ast = Add(Num(7), Mul(Num(3), Num(2)))

    pv = PrintVisitor()
    cv = CalcVisitor()

    print(pv.visit(ast))
    print(cv.visit(ast))


if __name__ == '__main__':
    main()

    