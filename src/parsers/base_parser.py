from abc import ABC, abstractmethod
from typing import Optional
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class BaseParser(ABC):
    def __init__(self, driver: WebDriver, url: str):
        self.driver = driver
        self.url = url
        self.wait = None

    def load_page(self):
        self.driver.get(self.url)
        self.wait = WebDriverWait(self.driver, 10)

    def extract_link(self, element: WebElement) -> Optional[str]:
        try:
            return element.find_element(By.TAG_NAME, 'a').get_attribute("href")
        except NoSuchElementException:
            return None

    @abstractmethod
    def parse(self, data):
        pass
