from model.contact import Contact

def test_edit_first_contact(app):
    app.session.login("admin", "secret")
    app.contact.edit_first_contact(Contact(firstname="1Ivan", middlename="1Ivanovich", lastname="1Ivanov", nickname="1Vanya", title="1Man", company="1unreal", address="1Moscow", home="1St. Petersburg",
                            mobile="188888888888", work="189888888888", fax="189988888888", email="1Ivan@gmail.com", email2="1Ivan@mail.ru",
                            email3="1Iban@yandex.ru", homepage="1something", bday="2", bmonth="February", byear="2002", aday="3", amonth="March", ayear="2003"))
    app.session.logout()