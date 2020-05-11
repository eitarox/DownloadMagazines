from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# Chrome Driverのパス
driver_path = './chromedriver'
# ドライバーを開く
driver = webdriver.Chrome(driver_path)

# ウィンドウサイズを固定
# +123としているのは
# 「Chromeは自動テストソフトウェアによって制御されています。」
# という部分を考慮している
window = (500, 420+123)
driver.set_window_size(*window)

# nxtbookのarchaeologyページを開く
target_url = 'https://www.nxtbook.com/projects/archaeology/'
driver.get(target_url)

# archaeology画面をずらすために書く
target_xpath = '//*[@id="game"]/div'
webgl_element = driver.find_element_by_xpath(target_xpath)
actions = ActionChains(driver)
actions.move_to_element(webgl_element).perform()

# クリックする前にロード時間待機
sleep(10)

# スタートボタンの座標
center_x = 250
center_y = 256

# スタートボタンをクリックする
actions = ActionChains(driver)
actions.move_to_element_with_offset(webgl_element, center_x, center_y).click().perform()

print("スタートボタンをクリックしました。")
input("何か入力してください")

# ドライバーを閉じる
driver.close()
driver.quit()