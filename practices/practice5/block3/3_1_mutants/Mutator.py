import random
from binary_search import binary_search, test_binary_search
import inspect
import ast


class Mutator(ast.NodeTransformer):
    def visit_Constant(self, node):
        if isinstance(node.value, (int, float)):
            node.value = random.choice(
                [random.randint(-100, 100), random.uniform(-100, 100)])
        return node


def mutate_code(src):
    tree = ast.parse(src)
    tree = Mutator().visit(tree)
    return ast.unparse(tree)


def make_mutants(func, size):
    mutant = src = ast.unparse(ast.parse(inspect.getsource(func)))
    mutants = [src]
    while len(mutants) < size + 1:
        while mutant in mutants:
            mutant = mutate_code(src)
        mutants.append(mutant)
    return mutants[1:]


def mut_test(func, test, size=20):
    survived = []
    mutants = make_mutants(func, size)
    for mutant in mutants:
        try:
            exec(mutant, globals())
            test()
            survived.append(mutant)
        except:
            pass
    return survived


if __name__ == '__main__':
    survived_mutants = mut_test(binary_search, test_binary_search(), size=10)
    print("Survived mutants:", survived_mutants)