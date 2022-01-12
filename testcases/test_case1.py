import time
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestExample:
    def test_fixture(self):
        print("Actual test scenario1")
        # self.driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']").click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='BE_flight_origin_city']"))).send_keys("Mumbai")
        self.driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']").send_keys(Keys.ENTER)
        # self.driver.find_element_by_id("BE_flight_arrival_city").click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, "BE_flight_arrival_city"))).send_keys("New Delhi")
        # self.driver.find_element_by_id("BE_flight_arrival_city").send_keys(Keys.ENTER)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_date']"))).click()
        self.driver.find_element_by_id("11/01/2022").click()
        self.driver.find_element(By.XPATH, "//div[@class='ripple-parent search-height demo-icon icon-go']//input["
                                           "@id='BE_flight_flsearch_btn']").click()
        time.sleep(5)
