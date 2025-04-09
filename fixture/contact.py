from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re

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
            for row in wd.find_elements(By.NAME, "entry"):
                cells = row.find_elements(By.TAG_NAME, "td")
                firstname = cells[2].text
                lastname = cells[1].text
                id = cells[0].find_element(By.TAG_NAME, "input").get_attribute("value")
                all_phones = cells[5].text
                address = cells[3].text
                all_email = cells[4].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id, all_phones_from_home_page=all_phones, address=address, all_email_from_home_page=all_email))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements(By.NAME, "entry")[index]
        cell = row.find_elements(By.TAG_NAME, "td")[7]
        cell.find_element(By.TAG_NAME, "a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements(By.NAME, "entry")[index]
        cell = row.find_elements(By.TAG_NAME, "td")[6]
        cell.find_element(By.TAG_NAME, "a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element(By.NAME, "firstname").get_attribute("value")
        lastname = wd.find_element(By.NAME, "lastname").get_attribute("value")
        id = wd.find_element(By.NAME, "id").get_attribute("value")
        home = wd.find_element(By.NAME, "home").get_attribute("value")
        mobile = wd.find_element(By.NAME, "mobile").get_attribute("value")
        work = wd.find_element(By.NAME, "work").get_attribute("value")
        fax = wd.find_element(By.NAME, "fax").get_attribute("value")
        address = wd.find_element(By.NAME, "address").get_attribute("value")
        email = wd.find_element(By.NAME, "email").get_attribute("value")
        email2 = wd.find_element(By.NAME, "email2").get_attribute("value")
        email3 = wd.find_element(By.NAME, "email3").get_attribute("value")
        return Contact(firstname= firstname, lastname=lastname, id=id, home=home, mobile=mobile, work=work, fax=fax, address=address, email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element(By.ID, "content").text
        home = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        fax = re.search("F: (.*)", text).group(1)

        full_name = wd.find_element(By.CSS_SELECTOR, "#content > b").text
        name_parts = full_name.split()
        firstname = name_parts[0]
        lastname = name_parts[-1]

        all_lines = [line.strip() for line in text.split('\n') if line.strip()]
        address = None
        for i, line in enumerate(all_lines):
            if 'H:' in line:
                address = all_lines[i - 1]
                break

        email_elements = wd.find_elements(By.XPATH, "//a[starts-with(@href, 'mailto:')]")
        emails = [email_element.get_attribute("href").replace("mailto:", "") for email_element in email_elements]
        email = emails[0] if len(emails) > 0 else None
        email2 = emails[1] if len(emails) > 1 else None
        email3 = emails[2] if len(emails) > 2 else None

        return Contact(home=home, mobile=mobile, work=work, fax=fax, firstname=firstname, lastname=lastname, address=address, email=email, email2=email2, email3=email3)
