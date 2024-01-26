from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from langdetect import detect

# query = input('what do you wanna research?')
# new_query = query.replace(' ', '+')
new_query = 'cafes+in+new+york'


def azazaz1():
    driver = webdriver.Chrome()
    try:
        driver.get(f'https://www.google.com/maps/search/{new_query}/')
        results = []
        links = []

        # LOCATE AND GET RID OF THE COOKIES BUTTON
        # fuck_cookies_button = driver.find_element(by=By.XPATH, value='//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[1]/div/div/button')
        # fuck_cookies_button.click()

        # LOCATE AND GET ALL THE RESTAURANTS
        time.sleep(2)
        all_restaurants = driver.find_elements(by=By.CLASS_NAME, value="hfpxzc")

        # LOCATE THE SIDE BAR AND SCROLL AS LOW AS POSSIBLE
        divSideBar = driver.find_element(By.XPATH,
                                         '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]')

        keepScrolling = True
        while (keepScrolling):
            divSideBar.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.5)
            divSideBar.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.5)
            html = driver.find_element(By.TAG_NAME, "html").get_attribute('outerHTML')
            # end_text = driver.find_element(By.XPATH,
            #                               '/html/body/div[2]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[247]/div/p/span/span')
            # detect(end_text)

            # HERE YOU NEED TO TRANSLATE THE END TEXT TO ALL THE VARIATIONS

            if (html.find("You've reached the end of the list.") != -1 or html.find("THE SENTENCE GOOGLE USES FOR THEIR SPANISH GOOGLE MAPS") != -1):
                keepScrolling = False

        # GATHER ALL THE LINKS TO GET INTO THE RESTAURANT DATA (STILL IN GOOGLE MAPS)
        for restaurant in all_restaurants:
            link = restaurant.get_attribute('href')
            links.append(link)
            # name = restaurant.find_element(By.CLASS_NAME, value="DUwDvf lfPIob")
            # results.append(name.text)

        return links

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        driver.quit()
