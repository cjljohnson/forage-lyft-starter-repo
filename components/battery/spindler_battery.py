import datetime

from components.battery.Battery import Battery

SERVICE_YEARS = 2

class SpindlerBattery(Battery):


    def __init__(self, last_service_date: datetime):
        super().__init__()
        self.last_service_date = last_service_date
        #self.current_date = current_date

    def needs_service(self) -> bool:
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + SERVICE_YEARS)
        return service_threshold_date >= datetime.today().date()