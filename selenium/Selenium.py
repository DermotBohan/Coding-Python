##from selenium import webdriver
##from selenium.webdriver.edge.service import Service
##import selenium
### driver = webdriver.Chrome()
##driver = webdriver.Edge(service = ser)
##driver.get('https://sma.pfizer.com/sm/index.do')


# ConfigurationManagement = driver.find_element_by_xpath('//*[@id="ext-gen-top293"]')



# //*[@id="ext-gen-top293"]
# /html/body/div[2]/div/div[2]/div[1]/div/div/div[7]/div[1]/span

# ConfigurationManagement.send_keys('~')
# ConfigurationManagement.click()

# driver.get("http://username:password@www.domain.com")


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()

driver.get('https://sma.pfizer.com/sm/index.do')

element = driver.find_element(By.ID, 'sb_form_q')
element.send_keys('WebDriver')
element.submit()

time.sleep(5)
driver.quit()

