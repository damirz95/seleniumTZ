import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function",autouse=True)
def driver():
    options = Options()
    #options.add_argument("--headless")
    prefs = {
        "download.default_directory": f"{os.getcwd()}/downloads"
    }
    options.add_experimental_option("prefs",prefs)
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service,options=options)
    driver.maximize_window()
    yield driver
    driver.quit()