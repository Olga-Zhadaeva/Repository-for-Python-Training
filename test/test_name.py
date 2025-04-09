import re
from random import randrange

def test_phones_on_home_page(app):
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert clear(contact_from_home_page.firstname) == clear(contact_from_edit_page.firstname)
    assert clear(contact_from_home_page.lastname) == clear(contact_from_edit_page.lastname)

def test_phones_on_contact_view_page(app):
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_view_page = app.contact.get_contact_from_view_page(index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert clear(contact_from_view_page.firstname) == clear(contact_from_edit_page.firstname)
    assert clear(contact_from_view_page.lastname) == clear(contact_from_edit_page.lastname)

def clear(s):
    return re.sub(r"\s+", "", s)
