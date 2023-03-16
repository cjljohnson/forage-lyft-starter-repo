from abc import ABC, abstractmethod

from components.Component import Component


class Engine(ABC, Component):

    @abstractmethod
    def needs_service(self) -> bool:
        pass