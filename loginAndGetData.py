from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

website = 'https://tracxn.com/a/s/query/t/people/t/allpeople/table?h=6745d0d696d68befc9a4a12642ca3092f08fb08b4b943035939990df51ddd75f&s=sort%3DpeopleScore%7Corder%3DDEFAULT'
driver = webdriver.Chrome()
driver.get(website)
driver.maximize_window()

# //input[@id="email_"]
input_username = driver.find_element(By.XPATH,'//input[@id="email_"]')
input_username.send_keys("EMAILID")
next_button = driver.find_element(By.XPATH,'//button[@type="submit"]')
next_button.click()
time.sleep(5)
input_password = driver.find_element(By.XPATH,'//input[@name="password"]')
input_password.send_keys("PASSWORD")
submit_button = driver.find_element(By.XPATH,'//button[@type="submit"]')
submit_button.click()
# //button[@type="submit"]
time.sleep(15)

scrolling = True
person_info_list = []
names = []
summary = []
location = []
work_experience = []
angel_investments = []
board_member = []
people_score = []
linkedIn_ids = []
prev = 0
while scrolling:
    time.sleep(10)
    rows = driver.find_elements(By.XPATH,'//*[@id="container_tracxn"]/div[2]/div[3]/div[4]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div/div')
    for row in rows:
        # person_info_list.append(row.text)
        row_data = row.find_elements(By.XPATH,'./div')
        if len(row_data) >= 7:  # Check if there are enough elements in the row_data
            print(row_data[1].text)
            names.append(row_data[1].text)
            summary.append(row_data[2].text)
            location.append(row_data[3].text)
            work_experience.append(row_data[4].text)
            angel_investments.append(row_data[5].text)
            board_member.append(row_data[6].text)
        else:
            print("Insufficient elements in row_data. Skipping.")
    prev = prev + 5000
    driver.execute_script("window.scrollTo(0, " + str(prev) + ")")
    new_height = driver.execute_script("document.body.scrollHeight")
    if prev >= 26000:
        scrolling = False
        break
        # button = row.find_element(By.XPATH,'//div[contains(@class,"people-card--icons-on-hover")]')
        # button.click()
        # time.sleep(1)
        # linkedIn_button = driver.find_element(By.XPATH,'//div[@style="position: fixed; z-index: 1070;"]/div/div/div/div/ul/li/span')
        # linkedIn_id = linkedIn_button.get_attribute("id")
        # linkedIn_ids.append(linkedIn_id)

# print(person_info_list,len(person_info_list))
df = pd.DataFrame({"Name":names,"Summary":summary,"Location":location,"Work Experience":work_experience,"Angel Investmenst":angel_investments,"Board Member":board_member})
df.to_excel('ScrolledOutput.xlsx', index=False)
time.sleep(10)
driver.close()
# div box of 10 infos
# //*[@id="container_tracxn"]/div[2]/div[3]/div[4]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div