from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Configurar Chrome en modo headless
options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")

# Ruta al ejecutable del driver (solo si no está en PATH)
service = Service(r"C:\Users\facab\AppData\Local\webdriver\chromedriver.ex")
driver = webdriver.Chrome(service=service, options=options)

# URL de Steam (puedes cambiar por otro juego)
url = "https://store.steampowered.com/app/1476970/IdleOn__The_Idle_RPG/"
driver.get(url)

# Esperar a que cargue el contenido dinámico
time.sleep(5)

# Simular scroll para que cargue más reseñas
for _ in range(3):  # puedes aumentar este valor para más comentarios
    driver.execute_script("window.scrollBy(0, 1500);")
    time.sleep(2)

# Extraer los comentarios
comentarios = []
elements = driver.find_elements(By.CLASS_NAME, "apphub_CardTextContent")

for el in elements:
    texto = el.text.strip()
    if texto:
        comentarios.append({"comentario": texto})

# Guardar en CSV
df = pd.DataFrame(comentarios)
df.to_csv("steam_idleon_comentarios.csv", index=False, encoding="utf-8")

print(f"Guardados {len(comentarios)} comentarios en steam_comentarios.csv")

driver.quit()