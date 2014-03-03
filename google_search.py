from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import unittest
import sys
import time


class GoogleTestCase(unittest.TestCase):
    desired_capabilities = {
                        "browserName": "firefox",
                        "appID" : "appID",
                        "version": "23",
                        "platform":"LINUX",
                        "hubUrl" : "http://ommm:NZq6R6BLgVf93iGt7SPe@hub.browserstack.com:80/wd/hub",
                        # "hubUrl" : "http://ec2-54-213-199-4.us-west-2.compute.amazonaws.com:4444/wd/hub",

                        }
    def setUp(self):
        self.driver = webdriver.Remote(desired_capabilities=GoogleTestCase.desired_capabilities)

    # def test_example1(self):
    #     self.driver.get("http://www.google.com")
    #     self.assertEqual(self.driver.title, "Google")
    #     elem = self.driver.find_element_by_name("q")

    #     elem.send_keys("selenium")
    #     elem.send_keys(Keys.RETURN)
    #     self.assertIn("Google", self.driver.title)

    def test_example2(self):
        self.driver.get("http://www.google.com")
        # self.assertEqual(self.driver.title, "Google")
        elem = self.driver.find_element_by_name("q")

        elem.send_keys("robustest")
        time.sleep(2)
        elem = self.driver.find_element_by_name("btnG")
        elem.click()
        time.sleep(2)
        self.assertIn("Google", self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
