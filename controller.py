from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.interaction import KEY
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common import keys
from queue import Queue
from threading import Thread
from time import sleep


NICKNAME = "[K]enny_bot"
room_link = "https://www.haxball.com/play?c=fcomsCn9tS4"
action_possibility = ["x", keys.Keys.DOWN, keys.Keys.UP, keys.Keys.RIGHT, keys.Keys.LEFT]
options = Options()
options.headless = True


def main():
    driver_1 = webdriver.Firefox(options=options)
    driver_2 = webdriver.Firefox(options=options)
    drivers = [driver_1, driver_2]

    threads = []

    for i in range(len(drivers)):
        process = Thread(target=run, args=[drivers[i]])
        process.start()
        threads.append(process)

    for process in threads:
        process.join()



def run(driver):
    # Go to url
    driver.get(room_link)

    # Delay to start
    sleep(4)

    # Change driver focus
    frame = driver.find_element_by_xpath('/html/body/div/div[2]/iframe')
    driver.switch_to.frame(frame)

    # Enter nickname
    input_element = driver.find_element_by_xpath("/html/body/div/div/div/div/input")
    action = ActionChains(driver)
    action.move_to_element(input_element).click(input_element).send_keys(NICKNAME).send_keys(keys.Keys.ENTER).perform()

    sleep(10)

    # Select the field
    element = driver.find_element_by_xpath("//div[@class='top-section']")
    element.click()

    # Fix camera
    actions = ActionChains(driver)
    actions.send_keys("1").perform()

    # Take screenshot
    sleep(0.2)
    element.screenshot("./screenshots/first_test.png")

    do_something(driver)

    # Stop the driver
    sleep(10)
    driver.quit()



def do_something(driver):
    actions = ActionChains(driver)
    counter = 0
    while True:
        # do_something(driver)
        actions = ActionChains(driver)
        actions.send_keys(action_possibility[counter]).perform()
        counter += 1
        if counter == 5:
            counter = 0
    # elem.send_keys("pycon")
    # elem.send_keys(Keys.RETURN)
    # assert "No results found." not in driver.page_source
    # driver.close()



if __name__ == "__main__":
    main()
