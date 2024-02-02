from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
import json

chrome_options = Options()
chrome_options.add_argument('--headless')  # Optional: Run in headless mode if you don't need a browser window
chrome_options.add_argument('--ignore-ssl-errors=yes')
chrome_options.add_argument('--ignore-certificate-errors')
# Provide the path to your ChromeDriver executable
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# URL and authentication credentials
url = "http://166.152.83.37:8081/wmf/index.html#/setup/basic_videoProfile"
username = "admin"
password = "Orbital227"

wait=WebDriverWait(driver,20)
driver.get(url)
time.sleep(20)
get_url = driver.current_url
wait.until(EC.url_to_be(url))

if get_url == url:
    page_source = driver.page_source

soup = BeautifulSoup(page_source, features="html.parser")
xpath='//*[@id="profilepage"]/div/div[6]/div[2]/div[3]/div[2]/input'
name= driver.find_element(By.XPATH,xpath)
name_value= name.get_attribute('value')


xpath2='//*[@id="profilepage"]/div/div[6]/div[2]/div[4]/div[2]/select'
codec= driver.find_element(By.XPATH,xpath2)
codec_value= codec.get_attribute('value')


xpath3='//*[@id="profilepage"]/div/div[6]/div[4]/div[2]/div[1]/div[2]/select'
resolution= driver.find_element(By.XPATH,xpath3)
resolution_value= resolution.get_attribute('value')



xpath4='//*[@id="profilepage"]/div/div[6]/div[4]/div[2]/div[2]/div[2]/select'
frame_rate= driver.find_element(By.XPATH,xpath4)
frame_rate_value= frame_rate.get_attribute('value')

xpath5='//*[@id="profilepage"]/div/div[6]/div[4]/div[2]/div[3]/div[3]/input'
maximum_bitrate= driver.find_element(By.XPATH,xpath5)
maximum_bitrate_value= maximum_bitrate.get_attribute('value')

xpath6='//*[@id="profilepage"]/div/div[6]/fieldset/div[1]/div[2]/div[1]/div[2]/select'
bitrate_control= driver.find_element(By.XPATH,xpath6)
bitrate_control_value= bitrate_control.get_attribute('value')


xpath7='//*[@id="profilepage"]/div/div[6]/fieldset/div[1]/div[2]/div[2]/div[2]/input'
video_compression= driver.find_element(By.XPATH,xpath7)
video_compression_value= video_compression.get_attribute('value')

xpath8='//*[@id="profilepage"]/div/div[6]/fieldset/div[1]/div[2]/div[4]/div[2]/input'
gov_length= driver.find_element(By.XPATH,xpath8)
gov_length_value= gov_length.get_attribute('value')

xpath9='//*[@id="profilepage"]/div/div[6]/fieldset/div[1]/div[2]/div[5]/div[2]/select'
profile=driver.find_element(By.XPATH,xpath9)
profile_value= profile.get_attribute('value')

xpath10='//*[@id="profilepage"]/div/div[6]/fieldset/div[1]/div[2]/div[6]/div[2]/select'
entropy_coding=driver.find_element(By.XPATH,xpath10)
entropy_coding_value= entropy_coding.get_attribute('value')



data = {"Name": name_value,
        "Codec": codec_value,
        "resolution": resolution_value,
        "frame_rate": frame_rate_value,
        "Maximum bit rate": maximum_bitrate_value,
        "Bitrate Control": bitrate_control_value,
        "Video Compression": video_compression_value,
        "Gov Length": gov_length_value,
        "Profile": profile_value,
        "Entropy Coding": entropy_coding_value}

json_data = json.dumps(data, indent=2)
with open('Final_output.json', 'w') as json_file:
    json_file.write(json_data)

#file_path = 'output.txt'
#with open(file_path, 'w') as file:
#    for key, value in data.items():
#        file.write(f"{key}: {value}\n")
driver.quit
