from fastapi import FastAPI
from selenium import webdriver
from selenium.webdriver import ChromeOptions
import uuid 
import time

app = FastAPI()

@app.post("/screenshot")
def get_screenshot(url: str, company:str):
    uuid_obj = uuid.uuid4()
    uuid_str = str(uuid_obj)
    opts = ChromeOptions()
    opts.add_argument("--window-size=1280,720")
    opts.headless = True
    # Create a new Selenium webdriver
    driver = webdriver.Chrome(options=opts)
    driver.get(url)
    time.sleep(3)

    screenshot = driver.get_screenshot_as_png()

    driver.close()

    # Save the screenshot to a file
    with open(f"./screenshot/{company}_{uuid_str}.png", "wb") as f:
        f.write(screenshot)

    return {"screenshot": screenshot}

