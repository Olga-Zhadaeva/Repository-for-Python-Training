from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "add new").click()

    def open_home_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[20]").click()
        self.return_to_contact_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        #submit deletion
        wd.find_element(By.XPATH, '//*[@value="Delete"]').click()
        self.contact_cache = None

    def edit_first_contact(self, new_contact_data):
        self.edit_contact_by_index(0)

    def edit_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        self.fill_contact_form(new_contact_data)
        # submit contact update
        wd.find_element(By.NAME, "update").click()
        self.return_to_contact_page()
        self.contact_cache = None

    def return_to_contact_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home page").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.input_type("firstname", contact.firstname)
        self.input_type("middlename", contact.middlename)
        self.input_type("lastname", contact.lastname)
        self.input_type("nickname", contact.nickname)
        self.input_type("title", contact.title)
        self.input_type("company", contact.company)
        self.input_type("address", contact.address)
        self.input_type("home", contact.home)
        self.input_type("mobile", contact.mobile)
        self.input_type("work", contact.work)
        self.input_type("fax", contact.fax)
        self.input_type("email", contact.email)
        self.input_type("email2", contact.email2)
        self.input_type("email3", contact.email3)
        self.input_type("homepage", contact.homepage)
        self.select_type("bday", contact.bday)
        self.select_type("bmonth", contact.bmonth)
        self.input_type("byear", contact.byear)
        self.select_type("aday", contact.aday)
        self.select_type("amonth", contact.amonth)
        self.input_type("ayear", contact.ayear)

    def select_type(self, select_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, select_name).click()
            Select(wd.find_element(By.NAME, select_name)).select_by_visible_text(text)

    def input_type(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, '//*[@title="Edit"]').click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements(By.XPATH, '//*[@title="Edit"]')[index].click()

    def count(self):
        wd = self.app.wd
        if not (wd.current_url.endswith('/index.php')):
            self.open_home_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements(By.CSS_SELECTOR, 'tr[name="entry"]'):
                text = element.text
                id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                self.contact_cache.append(Contact(firstname=text.split()[1], lastname=text.split()[0], id=id))
        return list(self.contact_cache)
