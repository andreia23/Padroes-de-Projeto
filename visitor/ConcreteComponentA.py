import Component
from Visitor import Visitor
class ConcreteComponentA(Component):
   
    def accept(self, visitor: Visitor) -> None:
        
        visitor.visit_concrete_component_a(self)

    def exclusive_method_of_concrete_component_a(self) -> str:
        return "A"