import google.generativeai as genai
from selenium import webdriver
from selenium.webdriver.common.by import By
from healenium import Healenium
import subprocess
import json
import time
from config import Config

genai.configure(api_key=Config.GEMINI_API_KEY)

def generate_selenium_code(url):
    response = genai.generate_text(
        model="models/text-bison-001",
        prompt=f"""Generate Python Selenium test code for {url} including:
        - Basic navigation
        - Form interactions
        - Element assertions
        Use Healenium for locators""",
        temperature=0.7
    )
    return response.result

def run_selenium_test(url):
    driver = webdriver.Chrome(Config.SELENIUM_DRIVER)
    healenium = Healenium(driver)
    
    try:
        # Execute AI-generated test
        test_code = generate_selenium_code(url)
        exec(test_code, {'driver': driver, 'healenium': healenium})
        return {"status": "passed", "output": test_code}
    except Exception as e:
        return {"status": "failed", "error": str(e)}
    finally:
        driver.quit()

def run_performance_test(url):
    try:
        result = subprocess.check_output(
            f"lighthouse {url} --output=json --quiet",
            shell=True
        )
        return json.loads(result)
    except Exception as e:
        return {"error": str(e)}

def run_security_test(url):
    try:
        result = subprocess.check_output(
            f"zap-baseline.py -t {url} -J report.json",
            shell=True
        )
        return json.loads(result)
    except Exception as e:
        return {"error": str(e)}

def run_full_audit(url):
    return {
        "functional": run_selenium_test(url),
        "performance": run_performance_test(url),
        "security": run_security_test(url)
    }