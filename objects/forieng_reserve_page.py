from selenium.webdriver.common.by import By


class Foreign_Reserve():
    rl_XPATH = (By.XPATH,'//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr/td[2]')
    cl_XPATH = (By.XPATH,'//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[1]/td')







    def __init__(self,driver):
        self.driver = driver


    def scroll(self):
        m = self.driver.find_element(By.XPATH,'//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[4]/td[2]')
        self.driver.execute_script('arguments[0].scrollIntoView();',m)

    def Row_length(self):
        m= len(self.driver.find_elements(*Foreign_Reserve.rl_XPATH))
        return m


    def Col_length(self):
        n = len(self.driver.find_elements(*Foreign_Reserve.cl_XPATH))
        return n

    def iteration(self,a,b):
        m = self.driver.find_element(By.XPATH,'//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr['+str(a)+']/td['+str(b)+']').text
        return m

    def Header(self,b):
        n = self.driver.find_element(By.XPATH,'//*[@id="mw-content-text"]/div[1]/table[1]/thead/tr/th['+str(b)+']').text
        return n
