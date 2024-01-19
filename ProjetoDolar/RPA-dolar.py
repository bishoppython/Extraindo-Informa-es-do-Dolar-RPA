#RPA que busca cotação do Dolar Comercial e Turismo
# e envia para o Telegram em tempo real


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime
import requests
from credentials import *

# Configurações do driver do navegador
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)

# URL do site para verificar a cotação do dólar
url = 'https://valor.globo.com/valor-data/'

# Abra o site e espere o elemento de tabela carregar
driver.get(url)
wait = WebDriverWait(driver, 10)
# Clique no botão para selecionar o tipo de câmbio
# cambio_button = driver.find_element_by_xpath("//button[contains(text(),'Dólar Comercial')]")
# cambio_button.click()

# Obter o valor atual do dólar na tabela
dolar_value = driver.find_element('xpath','//*[@id="valor-data__convertion-container"]/div[2]/div[1]/div/div[2]/div[1]').text

dolar_turismo = driver.find_element('xpath', '//*[@id="valor-data__convertion-container"]/div[2]/div[3]/div/div[2]/div[1]').text

# Obter a data e hora atual
now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# Configurar a mensagem para ser enviada via Telegram
message = f"Valor do Dólar Comercial: R$ {dolar_value} e\n" \
          f"Valor do Dolar Turismo: R$ {dolar_turismo}\n" \
          f"Dado coletado em: {now}"

print(message) #Apenas para validação de como está a mensagem
# Enviar mensagem para o Telegram
#bot_token = bot_token
#chat_id = chat_id
url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}'
requests.get(url)

# Fechar o driver do navegador
driver.quit()
