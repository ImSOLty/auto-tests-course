import math

from selenium.common import NoAlertPresentException


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.browser.implicitly_wait(10)
        self.url = url
        self.browser.get(url)

    def element_present(self, locator):
        element = self.browser.find_elements(*locator)
        if len(element) == 0:
            return False, None
        return True, element[0]

    def get_by_locator(self, locator):
        return self.element_present(locator)[1]

    def get_multiple_by_locator(self, locator):
        return self.browser.find_elements(*locator)

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
