from abc import ABC, abstractmethod


class BaseParser(ABC):
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def load_page(self):
        self.driver.get(self.url)

    @abstractmethod
    def parse(self, data):
        pass
