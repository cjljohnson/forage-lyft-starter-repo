from abc import ABC, abstractmethod

from Serviceable import Serviceable

class Component(Serviceable):

    @abstractmethod
    def needs_service(self) -> bool:
        pass