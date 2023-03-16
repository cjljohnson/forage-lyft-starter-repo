from abc import ABC

from components.engine.Engine import Engine

MILEAGE_THRESHOLD = 30000


class SternmanEngine(Engine, ABC):
    def __init__(self, warning_light_on: bool):
        super().__init__()
        self.warning_light_on = warning_light_on

    def engine_should_be_serviced(self):
        return self.warning_light_on