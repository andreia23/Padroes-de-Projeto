from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Component(ABC):

    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass
