import abc

class ItemElement(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def accept(self):
        pass