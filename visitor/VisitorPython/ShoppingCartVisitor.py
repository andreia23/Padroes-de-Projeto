import abc

class ShoppingCartVisitor(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def visit(self, item):
        pass
