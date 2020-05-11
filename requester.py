from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

driver_path = "./chromedriver"
URL = "https://www.nxtbook.com/projects/archaeology/"

driver = webdriver.Chrome(driver_path)
driver.get(URL)

my_email = ""
my_password = ""

id = driver.find_element_by_id("email")
id.send_keys(my_email)
password = driver.find_element_by_id("password")
password.send_keys(my_password)

time.sleep(1)

login_button = driver.find_element_by_xpath("//*[@id='signin-form']/form/button")
login_button.click()

time.sleep(2)

number_of_magazine = 64
# number_of_magazine = 5


for i in range(9, number_of_magazine):
    watch_button = driver.find_element_by_xpath("/html/body/main/div/div[2]/div[{}]/div/div[2]/div/div/a".format(i+1))
    watch_button.click()
    time.sleep(12)
    print(driver.current_url)
    window_array = driver.window_handles
    driver.switch_to.window(window_array[-1])
    print(driver.current_url)

    # move_to_pdf = driver.find_element_by_xpath("//*[@id='container-1052-innerCt']")
    # move_to_pdf = driver.find_element_by_xpath("//*[@id='nxticonbutton-1040']")
    window_size = driver.get_window_size()
    button_size = {"width": 35, "height": 35}
    pdf_position_x = window_size['width'] - 4.5 * button_size["width"]
    pdf_position_y = button_size["height"]/2
    ActionChains(driver).move_by_offset(pdf_position_x, pdf_position_y).click().perform()
    ActionChains(driver).move_by_offset(-pdf_position_x, -pdf_position_y).perform()
    time.sleep(8)

    # # select_all = driver.find_element_by_xpath("//*[@id='button-1143-btnInnerEl']")
    # select_all = driver.find_element_by_xpath("//*[@id='button-1128-btnInnerEl']")
    # select_all.click()
    # time.sleep(6)
    #
    # # generate_pdf = driver.find_element_by_xpath("//*[@id='button-1145-btnInnerEl']")
    # generate_pdf = driver.find_element_by_xpath("//*[@id='button-1130-btnInnerEl']")
    # generate_pdf.click()
    # time.sleep(2)
    driver.switch_to.window(window_array[0])
    print(driver.current_url)
    print("{} magazine(s) have downloaded".format(i+1))
    driver.get("https://www.nxtbook.com/projects/archaeology/backissues.php")
    time.sleep(2)

driver.close()
driver.quit()
