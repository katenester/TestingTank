// test_smartfit.py
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_smartfit(driver):
    # Step #1
    driver.get("https://smartfit.com")
    assert "SmartFit" in driver.title
    form = driver.find_element_by_id("preselection-form")
    assert form.is_displayed()

    # Step #2
    gender = driver.find_element_by_id("gender")
    gender.send_keys("Ж")
    assert gender.get_attribute("value") == "Ж"

    # Step #3
    weight = driver.find_element_by_id("weight")
    weight.send_keys("60")

    # Step #4
    height = driver.find_element_by_id("height")
    height.send_keys("170")

    # Step #5
    activity = driver.find_element_by_id("activity-level")
    activity.send_keys(Keys.ARROW_DOWN)
    assert activity.get_attribute("value") == "1"

    # Step #6
    age = driver.find_element_by_id("age")
    age.send_keys("20")

    # Step #7
    goal = driver.find_element_by_id("goal")
    goal.send_keys(Keys.ARROW_DOWN)
    goal.send_keys(Keys.RETURN)
    assert goal.get_attribute("value") == "похудеть"

    # Step #8
    location = driver.find_element_by_id("location")
    location.send_keys("Москва")
    location.send_keys(Keys.RETURN)
    assert location.get_attribute("value") == "Москва"

    # Step #9
    sessions = driver.find_element_by_id("sessions")
    sessions.send_keys("3")

    # Step #10
    days = driver.find_element_by_id("days")
    days.send_keys("пн, ср, чт")

    # Step #11
    # Step #11.1
    nutrition_link = driver.find_element_by_link_text("суточного потребления калорий")
    nutrition_link.click()
    driver.switch_to.window(driver.window_handles[-1])
    assert "Калькулятор калорий" in driver.title

    # Step #11.2
    # TODO: add code to enter nutrition data

    # Step #11.3
    counter = driver.find_element_by_id("counter").text

    # Step #11.4
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    # Step #11.5
    calories = driver.find_element_by_id("calories")
    calories.send_keys(counter)

    # Step #12
    next_button = driver.find_element_by_id("next-button")
    next_button.click()
    assert "Календарь тренировок" in driver.title