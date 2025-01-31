from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def create_headless_chromedriver(width: int = 1280, height: int = 720, driver_path: str = None) -> webdriver.Chrome:
    # The following options are required to make headless Chrome
    # Work in a Docker container
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument(f"window-size={width},{height}")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--remote-debugging-port=9222")
    chrome_options.add_argument(
        "--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36")
    # Initialize a new browser
    return webdriver.Chrome(ChromeDriverManager(path=driver_path).install(), chrome_options=chrome_options)
