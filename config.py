import os

class Config:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "your-api-key")
    SELENIUM_DRIVER = os.getenv("SELENIUM_DRIVER", "chromedriver")
    HEALENIUM_SERVER = "http://localhost:7878"
    ALLURE_DIR = "reports"