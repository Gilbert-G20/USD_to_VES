from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_usd_ves_ratePL():
    """Retorna el valor del dólar desde Monitor Dólar (VES)."""
    url = "https://monitordolarvenezuela.com/precio-dolar-paralelo"
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Ejecución sin interfaz gráfica
    chrome_options.add_argument("--no-sandbox")  # Necesario para Docker
    chrome_options.add_argument("--disable-dev-shm-usage")  # Mejor rendimiento

    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        # -------------------------------
        # Opcional: Debug (descomentar si hay problemas)
        # print("Navegador iniciado. Cargando página...")
        # -------------------------------
        
        driver.get(url)
        
        # Espera a que el elemento esté visible (ajusta el ID)
        usd_span = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "precio-paralelo"))
        )
        rate = usd_span.text.strip()
        
        # -------------------------------
        # Opcional: Debug
        # print(f"Valor extraído: {rate}")
        # -------------------------------
        
        return {"rate": rate}
    
    except Exception as e:
        # -------------------------------
        # Opcional: Debug (error handling)
        # print(f"Error: {str(e)}")
        # -------------------------------
        return {"error": str(e)}
    
    finally:
        driver.quit()

# -------------------------------
# Opcional: Testing local (descomentar para probar)
# if __name__ == "__main__":
#    print("Testing scraper...")
#    dolar_rate = get_usd_ves_ratePL()
#    print(f"USD/VES: {dolar_rate}")
# -------------------------------