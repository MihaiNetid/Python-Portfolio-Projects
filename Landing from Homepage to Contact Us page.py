import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait


class ContactType:
    """ Listing attributes from 'Contact Type' dropdown list """
    STATE_ELECTIONS_DEPARTMENT = 'state_elections_department'
    COUNTY_ELECTIONS_DEPARTMENT = 'county_elections_department'
    NEED_NEW_SOFTWARE = 'need_new_software'
    PRIVATE_CITIZEN = 'private_citizen'
    PRESS_CONTACT = 'press_contact'


class HowCanWeHelp:
    """ Listing attributes from 'How Can We Help?' dropdown list """
    DEMO_ELECTIONS_OFFICIALS = 'demo_for_elections_officials'
    NEW_SOFTWARE_DEVELOPMENT = 'new_software_development'
    GENERAL_INQUIRY = 'general_inquiry'


class NavigateFromWebsiteHomepageToContactUs(unittest.TestCase):
    """ Locators on HOME PAGE """
    contact_us_btn = (By.XPATH, "//span[contains(text(),'Contact Us')]")
    """ Locators on CONTACT US page """
    contact_name = (By.NAME, 'contact-name')
    contact_type = (By.XPATH, "//option[@value='State Elections Department']/../..//select")
    state_elections_department = (By.CSS_SELECTOR, "option[value='State Elections Department']")
    county_elections_department = (By.CSS_SELECTOR, "option[value='County Elections Department']")
    need_new_software = (By.CSS_SELECTOR, "option[value='We need a new software!']")
    private_citizen = (By.CSS_SELECTOR, "option[value='Private Citizen']")
    press_contact = (By.CSS_SELECTOR, "option[value='Press Contact']")
    representing = (By.CSS_SELECTOR, "input[name^='i-am representing']")
    email = (By.NAME, 'email')
    how_can_we_help = (By.XPATH, "//option[@value='Demo for Elections Officials']/../..//select")
    demo_for_elections_officials = (By.CSS_SELECTOR, "option[value='Demo for Elections Officials']")
    new_software_development = (By.CSS_SELECTOR, "option[value='New Software Development']")
    general_inquiry = (By.CSS_SELECTOR, "option[value='General Inquiry']")
    contacting_reason_txt_area = (By.CSS_SELECTOR, "textarea[id^='textarea']")

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\Mihai\PycharmProjects\ProvistaCorp/browser_drivers/chromedriver.exe')
        """ Landing on HOME PAGE """
        self.driver.get("https://www.provistacorp.com/")

    def test_navigation_between_pages(self):
        """ Setup Faker for generating fake data """
        fake = Faker()
        driver = self.driver

        """ Assert if HOME PAGE has opened"""
        self.assertEqual(driver.current_url, "https://www.provistacorp.com/")

        """ Find CONTACT US menu button from upper right and click on it """
        self.click_on_elm(self.contact_us_btn)

        """ Implement wait time for letting page to load """
        self._wait_for_elm_to_load(self.contact_name)

        """ Assert if CONTACT US page has opened """
        self.assertEqual(driver.current_url, "https://www.provistacorp.com/contact-us")

        """ Find 'Contact Name' text input field and enter fake name """
        self.click_on_elm_and_enter_text(self.contact_name, fake.name())

        """ Find 'Contact Type' dropdown list and select the 'Private Citizen' option """
        self.select_contact_type(ContactType.NEED_NEW_SOFTWARE)

        """ Find 'i-am representing... (e.g. county of nevada, california)' text input field 
        and enter 'Union County, North Carolina' """
        self.click_on_elm_and_enter_text(self.representing, fake.city())

        """ Find 'Email' text input field and enter fake email """
        self.click_on_elm_and_enter_text(self.email, fake.email())

        """ Find 'How can we help?' dropdown list and select the 'General Inquiry' option """
        self.select_how_can_we_help(HowCanWeHelp.DEMO_ELECTIONS_OFFICIALS)

        """ Find 'Please let us know more about why you're contacting!' text input field and enter fake text """
        self.click_on_elm_and_enter_text(self.contacting_reason_txt_area, fake.paragraph(nb_sentences=5))

        """ Find 'Submit' button and click on it.  """
    # NOTES: It is commented - not to generate a request on website
        # driver.find_element_by_css_selector("//span[contains(text(),'Submit')]")

    def select_contact_type(self, contact_type):
        """ Getting attributes for selecting the Contact Type """
        locator_contact = getattr(self, contact_type)
        self.click_on_elm(self.contact_type)
        self.click_on_elm(locator_contact)

    def select_how_can_we_help(self, how_can_we_help):
        """ Getting attributes for selecting How Can We Help """
        locator_contact = getattr(self, how_can_we_help)
        self.click_on_elm(self.how_can_we_help)
        self.click_on_elm(locator_contact)

    def click_on_elm(self, locator):
        """ Performs click on web element """
        self._wait_for_elm_to_load(locator).click()

    def click_on_elm_and_enter_text(self, locator, text):
        """ Performs click on web element and then enters text """
        self.click_on_elm(locator)
        self._wait_for_elm_to_load(locator).send_keys(text)

    def _wait_for_elm_to_load(self, locator, time_sec=3):
        """ Wait for element to load """
        return WebDriverWait(self.driver, timeout=time_sec).until(EC.presence_of_element_located(locator))

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

