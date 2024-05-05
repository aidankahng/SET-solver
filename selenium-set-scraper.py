from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# This program automatically opens the setgame and solves it.
# Set card numbers are changed into lists of ternary digits:
# [FILL, SHAPE, COLOR, COUNT]
# Color: Red, Purple, Green
# SHAPE: Wavy, Diamond, Pill
# FILL: Solid, Striped, Empty
# COUNT: 1, 2, 3

#####################
# PLEASE REPLACE USERNAME WITH YOUR USERNAME
USERNAME = "test_user_123"


service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, timeout=10)

driver.get("https://www.setgame.com/set/puzzle")

#sleep to make sure page loads
sleep(2)

full_cards = driver.find_elements(By.CLASS_NAME, "set-card-td")
card_urls = []
for i in range(12):
    card_urls.append(full_cards[i].find_element(By.TAG_NAME, "img").get_attribute("src"))
card_ids = []
for card_url in card_urls:
    card_ids.append(''.join(i for i in card_url if i.isdigit()))

# Helps to ensure card_ids' are indeed valid
print(card_ids)

card_ternary = []
for id in card_ids:
    value = int(id) - 1
    card_ternary.append([value//27, (value%27)//9, (value%9)//3, value%3])

# Console print allows checking if ternary values make sense
print(card_ternary)

# Now we have a list of values that can be compared to each other.
# We now need to use this list to calculate exactly which combinations of 3 will create sets
# For a set of 3 cards, write a helper function that calculates if they are a SET

# Helper function returns true if cards are a match.
def is_set(card1, card2, card3):
    for i in range(4):
        # check if all different OR all same
        if not (((card1[i] == card2[i]) and (card2[i] == card3[i])) or ((card1[i] != card2[i]) and (card2[i] != card3[i]) and (card1[i] != card3[i]))):
            
            return False
    print(f"Cards {card1}, {card2}, {card3} ARE A MATCH!")
    return True

# Goes through every combination of cards and if they match clicks them for you
for i in range(len(card_ternary)-2):
    for j in range(i+1, len(card_ternary)-1):
        for k in range(j+1, len(card_ternary)):
            if is_set(card_ternary[i], card_ternary[j], card_ternary[k]):
                full_cards[i].click()
                sleep(0.1)
                full_cards[j].click()
                sleep(0.1)
                full_cards[k].click()
                sleep(0.1)

sleep(10) # Lets next page load


# OPTIONAL CODE! WILL AUTOMATICALLY INPUT YOUR USERNAME TO ADD TO WEEKLY RAFFLE 

# user_input = driver.find_element(By.ID, "edit-submitted-user-id")
# user_input.clear()
# user_input.send_keys(USERNAME + Keys.ENTER)

# sleep(20) # keeps window open after finishing the set game