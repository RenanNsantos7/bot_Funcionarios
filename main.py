from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
from login import login2
import pandas as pd

def selecionar_empresa(driver, codigo_empresa):
    try:
        print(f"🔎 Buscando empresa: {codigo_empresa}")
        driver.switch_to.frame('socframe')
        campo_codigo = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "cproemp"))
        )
        driver.execute_script("arguments[0].value = arguments[1];", campo_codigo, codigo_empresa)
        botao_procurar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "procuraModalBtn"))
        )
        driver.execute_script("arguments[0].click();", botao_procurar)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "listaemop"))
        )
        elemento = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="listaemop"]/table/tbody/tr/td[2]/a'))
        )

        elemento.click()
        print("✅ Empresa selecionada com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao selecionar empresa {codigo_empresa}: {e}")

def programa_funcionario(driver, codigo_programa):
    try:
        # Espera o campo estar presente e visível
        campo_programa = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'cod_programa'))
        )
        
        # Insere o valor com JavaScript
        driver.execute_script("arguments[0].value = arguments[1];", campo_programa, codigo_programa)

        # Espera o botão estar clicável
        botao = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'btn_programa'))
        )

        # Clica com JavaScript pra evitar tretas de sobreposição
        driver.execute_script("arguments[0].click();", botao)

        time.sleep(2)  # Se quiser, pode até tirar depois
        print("🔍 buscar dados...")
        driver.switch_to.default_content()
        
    except Exception as e:
        print(f"❌ Erro ao selecionar programa {codigo_programa}: {e}")


        
def main():
    driver = login2()

    selecionar_empresa(driver, '1430925')
    programa_funcionario(driver, '232')
    time.sleep(2)



if __name__ == "__main__":
    main()