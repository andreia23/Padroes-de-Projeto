from abc import ABC, abstractmethod
from ConcreteComponentA import ConcreteComponentA
from ConcreteComponentB import ConcreteComponentB

class Visitor(ABC):

    @abstractmethod
    def visit_concrete_component_a(self, element: ConcreteComponentA) -> None:
        pass

    @abstractmethod
    def visit_concrete_component_b(self, element: ConcreteComponentB) -> None:
        pass