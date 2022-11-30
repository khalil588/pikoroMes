path = r'C:/frais/package_to_install'
link = 'http://www.parcours-lmd.salima.tn/'
link2= 'http://www.parcours-lmd.salima.tn/listeueetab.php?parc=Vk5VGAgnWThRYAF7DjIBM1J0Wm4HMg==&etab=UzZXZFtt'
sheet1Columns = ['CodeParcours','Type','Domaine','Mention','Parcours']
sheet2Columns = ['Code_UE','Libelle','crt','Coef','Nat','Rg','CodeParcours']
sheet3Columns = ['Code_EE','Libelle','Coef','Cr','Rg','Cours','TD','Tp','C_Int','Total','Code_UE']

#land_page

"""        select = Select(self.find_element(by=By.XPATH,value='//*[@id="univ"]'))
        select.select_by_value('02')
        time.sleep(5)
        select = Select(self.find_element(by=By.XPATH, value='//select[@id="etablisement"]'))
        l = select.options
        for i in l[1:] :
            print(i.text)
            select.select_by_visible_text(i.text)
            break
        return True"""






















"""
# Python program to scrape table from website

# import libraries selenium and time
from selenium import webdriver
from time import sleep

# Create webdriver object
driver = webdriver.Chrome(
       executable_path="C:\selenium\chromedriver_win32\chromedriver.exe")

# Get the website
driver.get(
       "https://www.geeksforgeeks.org/find_element_by_link_text-driver-method-selenium-python/")

# Make Python sleep for some time
sleep(2)

# Obtain the number of rows in body
rows = 1 + len(driver.find_elements_by_xpath(
       "/html/body/div[3]/div[2]/div/div[1]/div/div/div/article/div[3]/div/table/tbody/tr"))

# Obtain the number of columns in table
cols = len(driver.find_elements_by_xpath(
       "/html/body/div[3]/div[2]/div/div[1]/div/div/div/article/div[3]/div/table/tbody/tr[1]/td"))

# Print rows and columns
print(rows)
print(cols)

# Printing the table headers
print("Locators		 " + "			 Description")

# Printing the data of the table
for r in range(2, rows + 1):
       for p in range(1, cols + 1):
              # obtaining the text from each column of the table
              value = driver.find_element_by_xpath(
                     "/html/body/div[3]/div[2]/div/div[1]/div/div/div/article/div[3]/div/table/tbody/tr[" + str(
                            r) + "]/td[" + str(p) + "]").text
              print(value, end='	 ')
       print()
"""

"""            value_list.append({
            'Date': row.find_elements(By.TAG_NAME, "td")[0].text,
            'Value': row.find_elements(By.TAG_NAME, "td")[1].text
        })



                self.execute_script("window.open('');")

                # Switch to the new window and open new URL
                self.switch_to.window(self.window_handles[1])



"""