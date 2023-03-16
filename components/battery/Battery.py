from abc import ABC, abstractmethod

from components.Component import Component


class Battery(Component):

    @abstractmethod
    def needs_service(self) -> bool:
        pass