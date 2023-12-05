from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.action_chains import ActionChains

import time
import requests
import os


# 设置 Chrome 用户数据目录
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--user-data-dir=/Users/guoyusheng/Downloads/test-chrome-stroge")
chrome_options.add_argument("--disk-cache-dir=/Users/guoyusheng/Downloads/test-chrome-stroge")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-extensions")
#chrome_options.add_argument("--profile-directory=/Users/guoyusheng/Library/Application\ Support/Google/Chrome/Profile\ 2")
#chrome_options.add_experimental_option("debuggerAddress","127.0.0.1:9222") # 此处端口要和cmd启动的端口号一致
# 创建 Chrome 实例
driver = webdriver.Chrome(options=chrome_options)
time.sleep(10)
# 打开网页或执行其他操作
driver.get("https://web.telegram.org/a/#-1001374839099")
time.sleep(20)
# 打开第二个页面（在新的标签页中）
driver.execute_script("window.open('', '_blank');")  # 打开一个新的标签页
driver.switch_to.window(driver.window_handles[1])  # 切换到新标签页
driver.get("https://web.telegram.org/a/#-1002014178588")
time.sleep(20)
# 在第一个页面操作
# ...
# 初始时，设置最后一条消息的 ID 为 14017（根据你的实际情况修改）
last_message_id = 260325
# 切换回第一个页面
driver.switch_to.window(driver.window_handles[0])
time.sleep(15)
def clear_browser_cache():
    # 执行 JavaScript 清除浏览器缓存
    driver.execute_script("window.location.reload(true);")

def insert_message_to_input(message_content):
    try:
        if message_content is not None:
        # 等待消息输入框可见
            input_box = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, 'editable-message-text'))
            )

            # 在消息输入框中输入新的消息内容
            input_box.clear()  # 清空原有内容
            #input_box.send_keys(message_content)
            # 使用 ActionChains 执行输入操作
            actions = ActionChains(driver)
            actions.move_to_element(input_box)
            actions.click()  # 模拟点击输入框
            actions.send_keys(message_content.split('\n')[0])  # 输入第一行内容
            actions.key_down(Keys.SHIFT)  # 按下 Shift 键
            actions.send_keys(Keys.ENTER)  # 按下 Enter 键
            actions.key_up(Keys.SHIFT)  # 释放 Shift 键
            actions.key_up(Keys.ENTER)  # 释放 Enter 键
            actions.send_keys(message_content.split('\n')[1])  # 输入第二行内容
            actions.send_keys(Keys.ENTER)  # 按下 Enter 键
            actions.key_up(Keys.ENTER)  # 释放 Enter 键
            actions.perform()  # 执行操作
            print(f"1-Inserted message: {message_content}")        
            # 这里可以模拟按下回车键，如果需要发送消息的话
            # 获取发送按钮元素
            # send_button = WebDriverWait(driver, 10).until(
            #     EC.element_to_be_clickable((By.XPATH, '//button[@class="Button send"]'))
            # )

            # # 使用 ActionChains 进行点击操作
            # ActionChains(driver).click(send_button).perform()


            print(f"2-Inserted message: {message_content}")
    except TimeoutException as e:
        print(f"TimeoutException: {e}")
# 定义等待条件，等待消息出现
def wait_for_new_message(last_message_id):
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(5)
    last_message_id = int(last_message_id )+ 1
    new_message_locator = (By.CSS_SELECTOR, f'div#message{last_message_id}')
    try:
        # 等待新消息出现
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(new_message_locator))
        # 获取新消息的文本内容
        new_message = driver.find_element(*new_message_locator).text
        first_newline_index = new_message.find('\n')
        second_newline_index = new_message.find('\n', first_newline_index + 1)

        # 如果找到了第二次换行，截取第二次换行之前的内容
        if second_newline_index != -1:
            new_message = new_message[:second_newline_index]
        else:
            new_message = new_message

        print(f"New message ({last_message_id}): {new_message}")
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(5)
        insert_message_to_input(new_message)
        return last_message_id
        

    except (TimeoutException, WebDriverException) as e:
        print(f"抛出了错误Error: {e}")
        last_message_id = int(last_message_id )- 1
        return last_message_id 
    


# 循环监听新消息
while True:
    last_message_id = wait_for_new_message(last_message_id)







