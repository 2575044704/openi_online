from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from urllib.parse import urlparse, urlunparse
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
 
#选项
chrome_options=Options()
 
 
#设置chrome浏览器为无界面模式
chrome_options.add_argument('--headless')
 
 
 
#下面的两行代码一般是不需要的，至少经过我的测试在windows上是不需要的。但经过我的测试在Ubuntu上如果不加的话等下就会报错WebDriverException: unknown error: DevToolsActivePort file doesn't exist while trying to initiate Chrome Browser，所以要加上
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
 

is_login = True
def main():
    driver = webdriver.Chrome(options=chrome_options)
    def login():
        try:
            driver.get("https://openi.pcl.ac.cn/user/login")
        
            #driver.implicitly_wait(0.5)
        
            text_box = driver.find_element(by=By.NAME, value="user_name")
            password = driver.find_element(by=By.ID, value="input_password")
            submit_button = driver.find_element(by=By.ID, value="submitId")
        
            text_box.send_keys("18420278726")
            password.send_keys("Qq2575044704")
            submit_button.click()
            
            driver.add_cookie({"name": "foo", "value": "bar"})
            
            print(driver.get_cookie("foo"))
        except Exception as e:
            print(f"An error occurred: {e}")
        # Function to perform the login and task creation
    
    if is_login == True:
        print("Logging in...")
        login()
    else:
        print("跳过登录")


    def perform_operations(driver):
        
        
        if is_login == False:
            driver.get("https://openi.pcl.ac.cn/index.html")
            # 首先清除由于浏览器打开已有的cookies
            driver.delete_all_cookies()
            with open('cookies.txt','r') as f:
            # 使用json读取cookies 注意读取的是文件 所以用load而不是loads
                cookies_list = json.load(f)
                for cookie in cookies_list:
                    driver.add_cookie(cookie)
        else:
            pass

           
                
        def close_2():
            # 使用显式等待等待复选框出现，这里等待10秒，可以根据实际情况调整
            
            try:
                time.sleep(10)
                #checkbox = WebDriverWait(driver, 10).until(
                #EC.element_to_be_clickable((By.NAME, 'notRemindAgain'))
                #)
                # 使用 ActionChains 模拟鼠标移动到按钮上并点击
                #if not checkbox.is_selected():
                #    actions = ActionChains(driver)
                #    actions.move_to_element(checkbox).click().perform()
                
                print("find the second close button")
                buttonclose = WebDriverWait(driver, 11).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, 'ui.positive.button'))
                )
            
                # 点击按钮
                actions = ActionChains(driver)
                actions.move_to_element(buttonclose).click().perform()
                print("关闭第二个按钮成功")
                # 执行其他操作...
            except Exception as e:
                print(f"点击按钮过程中发生错误: {str(e)}")
        def stop():

            driver.get("https://openi.pcl.ac.cn/asdfqwerty/sd2/grampus/onlineinfer")
            close_2()
            time.sleep(2)
            # 等待可按按钮元素可见
            button_element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'停止') and not(@class='disabled')]"))
            )

            # 检查按钮是否可点击
            if button_element.is_enabled():
                # 点击按钮
                ActionChains(driver).move_to_element(button_element).click().perform()
                #button_element.click()
                print("停止按钮已点击")
                time.sleep(2)
            else:
                print("停止不可点击")
        def fill_form(image_address, startup_file):
                          
            try:
                # 使用显式等待等待输入框出现，这里等待10秒，可以根据实际情况调整
                image_input = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="选择镜像或输入镜像地址"]'))
                )
                startup_input = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[placeholder="请输入启动文件"].el-input__inner'))
                )
        
                # 填写表单
                
                image_input.send_keys(image_address)
                startup_input.send_keys(startup_file)
        
                # 执行其他操作...
        
            except Exception as e:
                print(f"填写表单过程中发生错误: {str(e)}")
        
         #填写表单
        # Wait for the new task button to appear
        def click_close_button():
            
            driver.get("https://openi.pcl.ac.cn/asdfqwerty/sd2/grampus/onlineinfer/create")
            try:
                # 使用显式等待等待按钮出现，这里等待10秒，可以根据实际情况调整
                close_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'button.el-button.el-button--primary.el-button--small'))
                )
                
                # 使用 ActionChains 模拟鼠标移动到按钮上并点击
                actions = ActionChains(driver)
                actions.move_to_element(close_button).click().perform()
        
                # 执行其他操作...
                print("点击关闭按钮成功")
                time.sleep(2)
            except Exception as e:
                print(f"点击关闭按钮过程中发生错误: {str(e)}")
        def click_create_task_button():
            try:
                # 使用显式等待等待按钮出现，这里等待10秒，可以根据实际情况调整
                create_task_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'button.el-button.submit-btn'))
                )
        
                # 点击按钮
                        # 使用 ActionChains 模拟鼠标移动到按钮上并点击
                actions = ActionChains(driver)
                actions.move_to_element(create_task_button).click().perform()
        
                # 执行其他操作...
                print("创建任务按钮已按下")
            except Exception as e:
                print(f"点击按钮过程中发生错误: {str(e)}")
        def click_online_inference_link():
            global current_url
            try:
                driver.get("https://openi.pcl.ac.cn/asdfqwerty/sd2/grampus/onlineinfer")
                # 使用显式等待等待链接出现，这里等待10秒，可以根据实际情况调整
                online_inference_link = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//div[@class='op-wrap']//a[contains(text(), '在线推理')]"))
                )


                actions = ActionChains(driver)
                actions.move_to_element(online_inference_link).click().perform()
                                # 获取当前窗口句柄
                current_window_handle = driver.current_window_handle
        
                # 点击链接，在新标签页中打开
                online_inference_link.send_keys(Keys.CONTROL + Keys.RETURN)
        
                # 等待新标签页打开
                WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        
                # 获取所有窗口句柄
                all_window_handles = driver.window_handles
        
                # 切换到新标签页
                for window_handle in all_window_handles:
                    if window_handle != current_window_handle:
                        driver.switch_to.window(window_handle)
                        break

                current_url = driver.current_url
                print(f"当前浏览的网页URL: {current_url}")

            except Exception as e:
                print(f"点击链接过程中发生错误: {str(e)}")

        def run():
            if "is-disabled" in new_task_button.get_attribute("class"):
                print("不可用，restart")
                driver.quit()
                main()
                perform_operations(driver)
            else:
            # Click the new task button
                new_task_button.click()
        #run()
        
    # Create a webdriver session
        stop()
        click_close_button()
        close_2()
        fill_form("192.168.204.22:5000/default-workspace/99280a9940ae44ca8f5892134386fddb/image:sd_v10", "exc.py")
        click_create_task_button()
        click_create_task_button()
        click_create_task_button()
        #time.sleep(60)
        #click_online_inference_link()
    # Main loop with a 30-minute interval
    try:
        perform_operations(driver)
        # 去掉端口号
        parsed_url = urlparse(current_url)
        netloc_without_port = parsed_url.netloc.split(":")[0]

        # 去掉token部分
        new_path = parsed_url.path
        if "?" in new_path:
            new_path = new_path.split("?")[0]

        # 构建新的URL，省略端口号和token部分
        new_url = urlunparse((parsed_url.scheme, netloc_without_port, new_path,
                              parsed_url.params, parsed_url.query, parsed_url.fragment))
        print(f"当前浏览的网页URL（去掉端口号）: {new_url}")
        print("完成")
        time.sleep(200)  # Sleep for 30 minutes (1800 seconds)

    finally:
        # Close the browser outside the loop
        driver.quit()
        
    
        
    
import requests
def detect():
    url = 'https://mouse-glowing-husky.ngrok-free.app/internal/ping'
    headers = {'accept': 'application/json'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        #main() #测试用
        print("成功")
        #print(response.json())
        time.sleep(5)
        detect()
    else:
        print("failed")
        main()
        detect()


main()
