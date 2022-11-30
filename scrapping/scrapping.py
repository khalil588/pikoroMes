
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import constant as cnst

class Scrapper2 (webdriver.Chrome):

    def __init__(self,driver_path=cnst.path, teardown = False):
        self.driver_path=driver_path
        self.teardown=teardown
        os.environ['PATH'] +=self.driver_path
        super(Scrapper2,self).__init__()
        self.implicitly_wait(60)


    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown :
            self.quit()

    def land_first_page(self):
        link = cnst.link
        self.get(link)
        select = Select(self.find_element(by=By.XPATH, value='//*[@id="univ"]'))
        select.select_by_value('02')
        time.sleep(5)
        select = Select(self.find_element(by=By.XPATH, value='//select[@id="etablisement"]'))
        l = select.options
        for i in l[1:]:
            print(i.text)
            select.select_by_visible_text(i.text)
            break
        return True
#Collecting matieres from table
    def CollectMatiereData(self,v = None,x = None):
        rows = v.find_elements(by = By.TAG_NAME, value='tr')
        l = []
        for row in rows[1:]:
            ls = []
            ls.append(x)
            value_list = row.find_elements(by =  By.TAG_NAME, value='td')
            for v in value_list :
                ls.append(v.text)
            l.append(ls)
            #//*[@id="main"]/table[3]/tbody/tr[4]/td[7]/table
            #//*[@id="main"]/table[3]/tbody/tr[6]/td[7]/table
            #//*[@id="main"]/table[3]/tbody/tr[8]/td[7]/table
            #//*[@id="main"]/table[3]/tbody/tr[4]
            #//*[@id="main"]/table[3]/tbody/tr[6]
            #//*[@id="main"]/table[3]/tbody/tr[3]
            #//*[@id="main"]/table[3]/tbody/tr[16]/td
            #//*[@id="main"]/table[3]/tbody/tr[18]/td[7]
            #//*[@id="main"]/table[3]/tbody/tr[26]/td[7]/table


#Collecting data from maquette
    def CollectMaquetteData(self):
        time.sleep(5)
        table = self.find_element(by = By.CSS_SELECTOR , value='#main > table:nth-child(8)')
        rows = table.find_elements(by = By.TAG_NAME, value='tr')
        print(type(rows))
        l = []
        #//*[@id="main"]/table[3]/tbody/tr[4]/td[1]
        #//*[@id="main"]/table[3]/tbody/tr[4]/td[7]
        for row in rows :
            i=0
            ls = []
            value_list = row.find_element(by = By.TAG_NAME,value='td')
            vl = value_list.text.upper()
            if vl[:8] == 'SEMESTRE' :
                continue

            for v in value_list :
                i+=1
                if i < 7 :
                  ls.append(v.text)
                else:
                    self.CollectMatiereData(v, ls[0])

            l.append(ls)

#collecting the terms of data such as
    def collectTabledata(self):
        time.sleep(5)
        table = self.find_element(by=By.CSS_SELECTOR, value='#parc > table')
        rows = table.find_elements(by = By.TAG_NAME ,value = "tr")
        i = 1
        for row in rows :
            i+=1
            value_list = row.find_elements(By.TAG_NAME,"td")
            l = []
            for v in value_list:
                l.append(v.text)

            my_element = self.find_element(by=By.XPATH, value='//*[@id="parc"]/table/tbody/tr['+str(i)+']/td[6]/a')
            print(my_element.get_attribute('href'))
            self.execute_script("window.open('');")

            # Switch to the new window and open new URL
            self.switch_to.window(self.window_handles[1])
            self.get(my_element.get_attribute('href'))

            # Closing new_url tab
            self.close()

            # Switching to old tab
            self.switch_to.window(self.window_handles[0])
            #self.execute_script("arguments[0].click();", my_element)
            i = 1
            break


#collecting_data_for example pays : france
    def collect_data_def(self):
        data = []
        data_recap = self.find_element(by=By.XPATH,value='//*[@id="parc"]/table/tbody/tr[2]/td[1]/div')
        data.append(data_recap.text)
        return data


