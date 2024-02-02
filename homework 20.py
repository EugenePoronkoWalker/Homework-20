from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from helpers.xpath import mensa as x

driver = webdriver.Chrome()
driver.set_window_position(2000, 600)
driver.maximize_window()
url = "https://test.mensa.no"
driver.get(url)

# enter_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x.enter_button)))
# enter_button.click()

age1850_xpath_button = driver.find_element(By.XPATH, x.age1850_xpath)
age1850_xpath_button.click()
time.sleep(3)

start_id_button = driver.find_element(By.ID, x.start_id)
start_id_button.click()
time.sleep(3)

ex1_a_button = driver.find_element(By.XPATH, x.ex1_a_xpath)
ex1_a_button.click()
time.sleep(3)

ex2_b_button = driver.find_element(By.XPATH, x.ex2_b_xpath)
ex2_b_button.click()
time.sleep(3)

ex3_c_button = driver.find_element(By.XPATH, x.ex3_c_xpath)
ex3_c_button.click()
time.sleep(3)

ex4_d_button = driver.find_element(By.XPATH, x.ex4_d_xpath)
ex4_d_button.click()
time.sleep(3)

ex5_e_button = driver.find_element(By.XPATH, x.ex5_e_xpath)
ex5_e_button.click()
time.sleep(3)

ex6_f_button = driver.find_element(By.XPATH, x.ex6_f_xpath)
ex6_f_button.click()
time.sleep(3)

ex7_a_button = driver.find_element(By.XPATH, x.ex7_a_xpath)
ex7_a_button.click()
time.sleep(3)

ex8_b_button = driver.find_element(By.XPATH, x.ex8_b_xpath)
ex8_b_button.click()
time.sleep(3)

ex9_c_button = driver.find_element(By.XPATH, x.ex9_c_xpath)
ex9_c_button.click()
time.sleep(3)

ex10_d_button = driver.find_element(By.XPATH, x.ex10_d_xpath)
ex10_d_button.click()
time.sleep(3)

ex11_e_button = driver.find_element(By.XPATH, x.ex11_e_xpath)
ex11_e_button.click()
time.sleep(3)

ex12_f_button = driver.find_element(By.XPATH, x.ex12_f_xpath)
ex12_f_button.click()
time.sleep(3)

ex13_a_button = driver.find_element(By.XPATH, x.ex13_a_xpath)
ex13_a_button.click()
time.sleep(3)

ex14_b_button = driver.find_element(By.XPATH, x.ex14_b_xpath)
ex14_b_button.click()
time.sleep(3)

ex15_c_button = driver.find_element(By.XPATH, x.ex15_c_xpath)
ex15_c_button.click()
time.sleep(3)

ex16_d_button = driver.find_element(By.XPATH, x.ex16_d_xpath)
ex16_d_button.click()
time.sleep(3)

ex17_e_button = driver.find_element(By.XPATH, x.ex17_e_xpath)
ex17_e_button.click()
time.sleep(3)

ex18_f_button = driver.find_element(By.XPATH, x.ex18_f_xpath)
ex18_f_button.click()
time.sleep(3)

ex19_a_button = driver.find_element(By.XPATH, x.ex19_a_xpath)
ex19_a_button.click()
time.sleep(3)

ex20_b_button = driver.find_element(By.XPATH, x.ex20_b_xpath)
ex20_b_button.click()
time.sleep(3)

ex21_c_button = driver.find_element(By.XPATH, x.ex21_c_xpath)
ex21_c_button.click()
time.sleep(3)

ex22_d_button = driver.find_element(By.XPATH, x.ex22_d_xpath)
ex22_d_button.click()
time.sleep(3)

ex23_e_button = driver.find_element(By.XPATH, x.ex23_e_xpath)
ex23_e_button.click()
time.sleep(3)

ex24_f_button = driver.find_element(By.XPATH, x.ex24_f_xpath)
ex24_f_button.click()
time.sleep(3)

ex25_a_button = driver.find_element(By.XPATH, x.ex25_a_xpath)
ex25_a_button.click()
time.sleep(3)

ex26_b_button = driver.find_element(By.XPATH, x.ex26_b_xpath)
ex26_b_button.click()
time.sleep(3)

ex27_c_button = driver.find_element(By.XPATH, x.ex27_c_xpath)
ex27_c_button.click()
time.sleep(3)

ex28_d_button = driver.find_element(By.XPATH, x.ex28_d_xpath)
ex28_d_button.click()
time.sleep(3)

ex29_e_button = driver.find_element(By.XPATH, x.ex29_e_xpath)
ex29_e_button.click()
time.sleep(3)

ex30_f_button = driver.find_element(By.XPATH, x.ex30_f_xpath)
ex30_f_button.click()
time.sleep(3)

ex31_a_button = driver.find_element(By.XPATH, x.ex31_a_xpath)
ex31_a_button.click()
time.sleep(3)

ex32_b_button = driver.find_element(By.XPATH, x.ex32_b_xpath)
ex32_b_button.click()
time.sleep(3)

ex33_c_button = driver.find_element(By.XPATH, x.ex33_c_xpath)
ex33_c_button.click()
time.sleep(3)

ex34_d_button = driver.find_element(By.XPATH, x.ex34_d_xpath)
ex34_d_button.click()
time.sleep(3)

ex35_e_button = driver.find_element(By.XPATH, x.ex35_e_xpath)
ex35_e_button.click()
time.sleep(3)

finish_button = driver.find_element(By.XPATH, x.finish_xpath)
finish_button.click()
time.sleep(3)

done_already_button = driver.find_element(By.XPATH, x.done_already_xpath)
done_already_button.click()
time.sleep(3)

time.sleep(3000)
