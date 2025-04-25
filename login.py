import selenium
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from dotenv import load_dotenv


load_dotenv()

login = os.getenv("SOC_LOGIN")
senha = os.getenv("SOC_SENHA")
ID = os.getenv("SOC_ID")

def login2():
        options = Options()
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--ignore-ssl-errors")
        options.add_argument("--disable-notifications")
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()

        driver.get('https://sistema.soc.com.br/WebSoc/')

        login_script = f"""
            document.getElementById("usu").value = "{login}";
            document.getElementById("senha").value = "{senha}";
            document.getElementById("empsoc").value = "{ID}";

            setTimeout(function() {{
                document.getElementById("bt_entrar").click();
            }}, 1000);
            """
        driver.execute_script(login_script)
        print("⏳ Fazendo Login no SOC...")
        time.sleep(3)
        
        return driver