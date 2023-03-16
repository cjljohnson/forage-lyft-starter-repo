from abc import ABC

from components.engine.Engine import Engine

MILEAGE_THRESHOLD = 60000


class WilloughbyEngine(Engine, ABC):
    def __init__(self, last_service_mileage: int, current_mileage: int):
        super().__init__()
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > MILEAGE_THRESHOLD
