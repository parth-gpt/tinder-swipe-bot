from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from time import sleep

chrome_driver_path = "/Users/parth_gpt/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://tinder.com/")

sleep(2)
log_in = driver.find_element_by_xpath(
    '//*[@id="u1186853273"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
log_in.click()

sleep(2)
try:
    log_in_with_fb = driver.find_element_by_xpath('//*[@id="u1408193709"]/div/div/div[1]/div/div[3]/span/div[2]/button')
    log_in_with_fb.click()
except:
    more_options = driver.find_element_by_xpath('//*[@id="u1408193709"]/div/div/div[1]/div/div[3]/span/button')
    more_options.click()
    sleep(1)
    log_in_with_fb = driver.find_element_by_xpath('//*[@id="u1408193709"]/div/div/div[1]/div/div[3]/span/div[2]/button')
    log_in_with_fb.click()

driver.window_handles
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

sleep(2)
email = driver.find_element_by_id("email")
email.send_keys(EMAIL)

password = driver.find_element_by_id("pass")
password.send_keys(PASS)

password.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)

sleep(5)
allow_location_button = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

notifications_button = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

try:
    cookies = driver.find_element_by_xpath('//*[@id="u1186853273"]/div/div[2]/div/div/div[1]/button')
    cookies.click()
except:
    pass

sleep(6)

# Tinder free tier only allows 100 "Likes" per day. If you have a premium account, feel free to change to a while loop.
for n in range(100):

    # Add a 1 second delay between likes.
    sleep(1)

    try:
        print("called")
        sleep(2)
        like_button = driver.find_element_by_xpath(
            '//*[@id="u1186853273"]/div/div[1]/div/div/main/div/div[1]/div[1]/div/div[5]/div/div[4]/button')
        like_button.click()

    # Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()

        # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            sleep(2)
    except NoSuchElementException:
        pass
driver.quit()
