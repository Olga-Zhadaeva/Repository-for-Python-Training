import re
from random import randrange

def test_full_contact_data_integrity(app):
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    contact_from_view_page = app.contact.get_contact_from_view_page(index)

    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_view_page.home == contact_from_edit_page.home
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.work == contact_from_edit_page.work
    assert contact_from_view_page.fax == contact_from_edit_page.fax

    assert contact_from_home_page.all_email_from_home_page == merge_email_like_on_home_page(contact_from_edit_page)
    assert contact_from_view_page.email == contact_from_edit_page.email
    assert contact_from_view_page.email2 == contact_from_edit_page.email2
    assert contact_from_view_page.email3 == contact_from_edit_page.email3

    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_view_page.address == contact_from_edit_page.address

    assert clear_text(contact_from_home_page.firstname) == clear_text(contact_from_edit_page.firstname)
    assert clear_text(contact_from_home_page.lastname) == clear_text(contact_from_edit_page.lastname)
    assert clear_text(contact_from_view_page.firstname) == clear_text(contact_from_edit_page.firstname)
    assert clear_text(contact_from_view_page.lastname) == clear_text(contact_from_edit_page.lastname)

def clear_text(s):
    return re.sub(r"\s+", "", s)

def clear_phone(s):
    return re.sub(r"[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear_phone(x), filter(lambda x: x is not None, [contact.home, contact.mobile, contact.work, contact.fax]))))

def merge_email_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear_text(x), filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3]))))