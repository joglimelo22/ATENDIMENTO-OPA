# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from modules.defaultResponses import DEFAULT
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class SELENIUM():

  def __init__(self):
    # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    self.driver = webdriver.Firefox()

  
  def enterSite(self, url):
    try:
      self.driver.get(url)

      return DEFAULT.defaultResponse(200, 'Conectado ao link')
    
    except Exception as err:
      return DEFAULT.defaultResponse(400, f'Erro ao tentar entrar no site, Erro: {err}')
  
  def quitSite(self):
    try:
      self.driver.quit()

      return DEFAULT.defaultResponse(200, 'Descontado do navegador')
    
    except Exception as err:
      return DEFAULT.defaultResponse(400, f'Erro ao tentar sair do site, Erro: {err}')
  
  def findElement(self, type, element):
    try:
      return DEFAULT.defaultResponse(200, self.driver.find_element(type, element))
    
    except Exception as err:
      return DEFAULT.defaultResponse(400, f'Erro ao tentar coletar o elemento, Erro: {err}')
    
  def findElementInElement(self, elementFather, type, elementChildren):
    try:
      return DEFAULT.defaultResponse(200, elementFather.find_elements(type, elementChildren))
    
    except Exception as err:
      return DEFAULT.defaultResponse(400, f'Erro ao tentar coletar o elemento, Erro: {err}')

  def getAttributeHTML(self, element):
    try:
      return DEFAULT.defaultResponse(200, element.get_attribute('outerHTML'))
    
    except Exception as err:
      return DEFAULT.defaultResponse(400, f'Erro ao tentar coletar o elemento, Erro: {err}')
  
  def awaitElement(self, type, element, time=10):
    try:
      element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located((type, element)))

      return DEFAULT.defaultResponse(200, element)
    
    except Exception as err:
      return DEFAULT.defaultResponse(400, f'Erro ao tentar aguardar o item, Erro: {err}')
  
  def sendKeys(self, element, command):
    try:
      element.send_keys(command)

      return DEFAULT.defaultResponse(200, 'Comando efetuado com sucesso')
    
    except Exception as err:
      return DEFAULT.defaultResponse(400, f'Erro ao tentar enviar o comando, Erro: {err}')
  
  def clickElement(self, element):
    try:
      element.click()

      return DEFAULT.defaultResponse(200, 'Comando efetuado com sucesso')
    
    except Exception as err:
      return DEFAULT.defaultResponse(400, f'Erro ao tentar enviar o comando, Erro: {err}')

  def printHTML(self):
    with open('teste.html', 'w', encoding="utf-8") as arquivo:
      arquivo.write(self.driver.page_source)



  def switchFrame(self, frame):    
    try:
      self.driver.switch_to.frame(frame)

      return DEFAULT.defaultResponse(200, 'Sucesso ao tentar mudar de tela')
    
    except Exception as err:
      return DEFAULT.defaultResponse(400, f'Erro ao tentar mudar de tela, Erro: {err}')
    
  def switchFrameDefault(self):    
    try:
      self.driver.switch_to.default_content()

      return DEFAULT.defaultResponse(200, 'Sucesso ao tentar mudar de tela')
    
    except Exception as err:
      return DEFAULT.defaultResponse(400, f'Erro ao tentar mudar de tela, Erro: {err}')