from abc import ABC, abstractmethod
from datetime import date

from Serviceable import Serviceable
from components.battery.Battery import Battery
from components.battery.nubbin_battery import SpindlerBattery, NubbinBattery
from components.engine.Engine import Engine
from components.engine.capulet_engine import CapuletEngine
from components.engine.sternman_engine import SternmanEngine
from components.engine.willoughby_engine import WilloughbyEngine


class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        if self.engine.needs_service():
            return True
        if self.battery.needs_service():
            return True
        return False

class CarFactory:

    def create_calliope(self, last_service_date: date, current_mileage: int, last_service_mileage: int):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date)
        return Car(engine, battery)

    def create_glissade(self, last_service_date: date, current_mileage: int, last_service_mileage: int):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date)
        return Car(engine, battery)

    def create_palindrome(self, last_service_date: date, warning_light_on: bool):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date)
        return Car(engine, battery)

    def create_rorschach(self, last_service_date: date, current_mileage: int, last_service_mileage: int):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date)
        return Car(engine, battery)

    def create_thovex(self, last_service_date: date, current_mileage: int, last_service_mileage: int):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date)
        return Car(engine, battery)
