from utils.driver_factory import DriverFactory



class BasePage:
    def __init__(self):
        self.page = DriverFactory.get_driver()
