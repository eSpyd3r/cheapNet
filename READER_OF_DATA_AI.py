import bs4
from selenium.webdriver.support.wait import WebDriverWait
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


#links = azazaz1()


def item_gathering_bulk():
    driver = webdriver.Chrome()
    for link in links:
        try:
            driver.get(link)


        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            driver.quit()


def locate_and_click_all_menu_buttons(url):
    options = webdriver.ChromeOptions()
    options.headless = True  #true if you don't want it to open a visible website everytime it runs the code
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    # Detect if the link brings us directly to a pdf with the items or a home website
    response = requests.head(url)
    content_type = response.headers.get('content-type', '')
    if 'pdf' in content_type.lower():
        with open('pdf_menus.txt', mode='w') as file:
            file.write(f'{url}\n')
    elif 'html' in content_type.lower():
        try:
            # look up all the "menu" items. Sometimes there are multiple
            soup = bs4.BeautifulSoup('html.parser')

            #NOT SURE WHICH ONE OF THESE WILL WORK BEST
            #menu_buttons = soup.find_all('button', {'name': 'Menu'})
            menu_buttons = driver.find_elements(By.XPATH, '//button[@name="Menu"]')

            if len(menu_buttons) < 0:
                pass
            else:
                # Assuming the "Menu" button is inside the navbar
                navbar_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'nav'))
                )

                # Use BeautifulSoup to parse the HTML within the navbar
                navbar_soup = bs4.BeautifulSoup(navbar_element.get_attribute("outerHTML"), 'html.parser')

                # Find the button with the label "Menu"
                menu_button = navbar_soup.find('button', {
                    'name': 'Menu'})  # Replace 'button' and 'name' with the actual button tag and attribute

                #SECOND PHASE --> SECOND WEBSITE
                menu_button.click()
                WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "menu-open")]'))
                    )

                # We have to check if there are more menu buttons. If there are not, we are in the desired location where the menu items are.
                soup = bs4.BeautifulSoup('html.parser')
                menu_buttons_second_search = soup.find_all('button', {'name': 'Menu'})
                if 1 <= len(menu_buttons_second_search) > 0:
                    for menu_button in menu_buttons_second_search:
                        menu_button[1].click()
                        WebDriverWait(driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "menu-open")]'))
                        )
                else:
                    # We do this to hasten the process for future runnings of the scrypt
                    # VERY IMPORTANT: when enough data is gathered in these .txt, create scrypt to pass the running of the scrypt whenever one of the links is about to be processed/clicked.
                    with open('No_more_menus_list.txt', mode='w') as file:
                        file.write(f'{url}\n')

        except Exception as e:
            print(f"Error: {e}")

        finally:
            driver.quit()


