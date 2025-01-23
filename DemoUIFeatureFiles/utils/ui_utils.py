from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def get_driver():
    """Initialize and return a WebDriver instance."""
    # Setup Chrome options (optional, you can customize if needed)
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Start browser maximized
    chrome_options.add_argument("--headless")  # Open in headless mode

    # Initialize the WebDriver
    driver = webdriver.Chrome()
    return driver
