from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# TAREFAS:
   # Acessar página; - OK
   # Pesquisar um produto; - OK
      # Clicar na barra pesquisa; - OK
      # Digitar produto; - OK
      # Clicar no botão busca. - OK

sites = {'Amazon': {'url': 'https://www.amazon.com.br/', 'elemento_pesquisa': '//*[@id="twotabsearchtextbox"]'},
         'Magazine Luiza': {'url': 'https://magazineluiza.com.br/', 'elemento_pesquisa': '//*[@id="input-search"]'},
         'Mercado Livre': {'url': 'https://www.mercadolivre.com.br/', 'elemento_pesquisa': '//*[@id="cb1-edit"]'}
         }

def acesso_pagina(sites, indx):
   driver.get(sites['url'][indx])

def pesquisa_produto(sites, indx, produto):
   # Clica na barra 'pesquisa' e digita o produto.
   driver.find_element(By.XPATH, sites['elemento_pesquisa'][indx]).send_keys(produto)

   # Aperta botão 'ENTER'.
   ActionChains(driver).send_keys(Keys.ENTER).perform()

# Definindo parâmetros.
produto = input('Produto: ').lower()

## Firefox
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)

for indx in range(0, len(sites['site'])): # NOTE: Talvez um 'WHILE'?

   # Acessando página.
   acesso_pagina(sites, indx)

   # Pesquisando produto.
   pesquisa_produto(sites, indx, produto)

   # Acessa próxima página (IF TRUE).
   # proxima_pagina()

   # NOTE: Extrair dados com BeautifulSoup.
   # Extração dos dados.
   # extrat_dados()

sleep(5)

driver.quit()