from abc import ABC, abstractmethod

from Serviceable import Serviceable

class Component(ABC, Serviceable):

    @abstractmethod
    def needs_service(self) -> bool:
        pass