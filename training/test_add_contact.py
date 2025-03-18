# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from training.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_contact(app):
    app.login("admin", "secret")
    app.create_contact(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="Vanya", title="Man", company="unreal", address="Moscow", home="St. Petersburg",
                            mobile="88888888888", work="89888888888", fax="89988888888", email="Ivan@gmail.com", email2="Ivan@mail.ru",
                            email3="Iban@yandex.ru", homepage="something", bday="1", bmonth="January", byear="2000", aday="2", amonth="February", ayear="2000"))
    app.logout()