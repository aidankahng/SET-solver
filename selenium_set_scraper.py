from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from set_solver import get_matches, dec_to_ternary_card

########################################################################################
# This program automatically opens the setgame and solves it.
# PLEASE REPLACE USERNAME WITH YOUR USERNAME
USERNAME = "YOUR_USERNAME_HERE"

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, timeout=10)
js_scroll = "arguments[0].scrollIntoView();"
driver.get("https://www.setgame.com/set/puzzle")

# Waits until it can find cards on the webpage or times out
wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, "set-card-td"))
)

# Scrolls page to approximately where it can click on all cards
game_board = driver.find_element(By.CLASS_NAME, "set-game-wrapper")
driver.execute_script(js_scroll, game_board)

# Gets all card elements
full_cards = driver.find_elements(By.CLASS_NAME, "set-card-td")
# Converts cards into manipulatable values
ternary_cards = []
for i in range(12):
    ternary_cards.append(dec_to_ternary_card(
        ''.join(j for j 
                in full_cards[i].find_element(By.TAG_NAME, "img").get_attribute("src") 
                if j.isdigit())
        ))

# Finds and clicks on matches
matches_list = get_matches(ternary_cards)
for set_answer in matches_list:
    for item in set_answer:
        # sleep(0.1) # UNCOMMENT IF CLICKS ARE TOO FAST TO REGISTER
        full_cards[item].click()

sleep(20) # Lets next page load with enough time to screenshot your time

########################################################################################
# OPTIONAL CODE! WILL AUTOMATICALLY INPUT YOUR USERNAME TO ADD TO WEEKLY RAFFLE

# user_input = driver.find_element(By.ID, "edit-submitted-user-id")
# user_input.clear()
# user_input.send_keys(USERNAME + Keys.ENTER)

# sleep(20) # keeps window open after finishing the set game