from modules.selenium import SELENIUM
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

channel = os.environ.get('CANAL')
profile = os.environ.get('PERFIL')

class OPA:

    def __init__(self):
        self.selenium = SELENIUM()
        self.selenium.enterSite("https://opa.ateky.net.br/auth/login")

    def login(self, email, password):
        self.selenium.awaitElement(By.XPATH, '//*[@id="username"]')
        emailInput = self.selenium.findElement(By.XPATH,'//*[@id="username"]')
        self.selenium.sendKeys(emailInput['message'], email)

        passwordInput = self.selenium.findElement(By.XPATH,'//*[@id="password"]')
        self.selenium.sendKeys(passwordInput['message'], password)

        buttonForm = self.selenium.findElement(By.XPATH,"/html/body/div/div[2]/div[1]/div/form/button")
        self.selenium.clickElement(buttonForm['message'])

        verifyLogin = self.selenium.awaitElement(By.XPATH,"/html/body/section/ol/li/div[2]/div", time=2)
        if verifyLogin['status'] == 400:
            return {"status": 200, "message": "Logado com sucesso"}
        else:
            return {"status": 400, "message": verifyLogin['message'].text}

    def openAtt(self, number, name):
        self.selenium.awaitElement(By.XPATH, '/html/body/div/div[5]/div[1]')
        menu = self.selenium.findElement(By.XPATH,'/html/body/div/div[5]/div[1]')
        if menu['status'] != 200:
            return menu
        
        self.selenium.clickElement(menu['message'])

        self.selenium.awaitElement(By.XPATH, '/html/body/div/div[1]/div[7]/div[1]/div')
        menuOpenAtt = self.selenium.findElement(By.XPATH,'/html/body/div/div[1]/div[7]/div[1]/div')
        if menuOpenAtt['status'] != 200:
            return menu
        self.selenium.clickElement(menuOpenAtt['message'])

        self.selenium.awaitElement(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/button')
        openAttClient = self.selenium.findElement(By.XPATH,'/html/body/div[2]/div/div[2]/div/div[2]/button')
        if openAttClient['status'] != 200:
            return menu
        self.selenium.clickElement(openAttClient['message'])

        self.selenium.awaitElement(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div/span/span[1]/span/span[1]')
        departament = self.selenium.findElement(By.XPATH,'/html/body/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div/span/span[1]/span/span[1]')
        if departament['status'] != 200:
            return menu
        self.selenium.clickElement(departament['message'])
        
        listDepartament = self.selenium.findElement(By.XPATH,'//*[@id="select2-selectDepartamentoAbrirAtendimento-results"]')
        if listDepartament['status'] != 200:
            return menu
        itemListDepartament = self.selenium.findElementInElement(listDepartament['message'], By.TAG_NAME,'li')
        if itemListDepartament['status'] != 200:
            return menu
        self.selenium.clickElement(itemListDepartament['message'][0])

        nameClient = self.selenium.findElement(By.XPATH,'/html/body/div[2]/div/div[2]/div/div[1]/div[1]/div[3]/input')
        if nameClient['status'] != 200:
            return menu
        self.selenium.sendKeys(nameClient['message'], name)

        numberClient = self.selenium.findElement(By.XPATH,'/html/body/div[2]/div/div[2]/div/div[1]/div[1]/div[4]/div/input')
        if numberClient['status'] != 200:
            return menu
        self.selenium.sendKeys(numberClient['message'], number)
        self.selenium.sendKeys(numberClient['message'], Keys.ENTER)


        time.sleep(1)

        listChannel = self.selenium.findElement(By.XPATH, f'/html/body/div[2]/div/div[2]/div/div[1]/div[2]/div/div/div[2]/div[{channel}]/div[1]/div[1]/button')
        if listChannel['status'] != 200:
            return menu
        self.selenium.clickElement(listChannel['message'])

        time.sleep(1)

        listProfile = self.selenium.findElement(By.XPATH, f'/html/body/div[2]/div/div[2]/div/div[1]/div[2]/div/div/div[2]/div[{channel}]/div[2]/div/div[2]/div[{profile}]/div/div[1]/button')
        if listProfile['status'] != 200:
            return menu
        self.selenium.clickElement(listProfile['message'])
        

        self.selenium.awaitElement(By.XPATH, '/html/body/div[3]/div[2]/div/div/div/div/div/div/div')
        confirmOpenAtt = self.selenium.findElement(By.XPATH,'/html/body/div[3]/div[2]/div/div/div/div/div/div/div/div[4]/button[2]')
        if confirmOpenAtt['status'] != 200:
            return menu
        self.selenium.clickElement(confirmOpenAtt['message'])

        return {"status": 200, "message": 'Aberto atendimento com sucesso'} 
        

        

        
        
        


        