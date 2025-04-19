from model.contact import Contact
import random
import string

constant = [
    Contact(firstname="firstname1", lastname="lastname1", nickname="nickname1", title="title1", company="company1",
            address="address1", home="home1", mobile="mobile1", work="work1", fax="fax1", email="email11", email2="email21",
            email3="email31", homepage="homepage1", bday="1", bmonth="January", byear="2001", aday="1", amonth="January", ayear="2001"),
    Contact(firstname="firstname2", lastname="lastname2", nickname="nickname2", title="title2", company="company2",
            address="address2", home="home2", mobile="mobile2", work="work2", fax="fax2", email="email12", email2="email22",
            email3="email32", homepage="homepage2", bday="2", bmonth="January", byear="2002", aday="2", amonth="February", ayear="2002")
]

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_phone_string(prefix, maxlen):
    symbols = string.digits + "+()- "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_year_string(prefix, maxlen):
    symbols = string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                    home="", mobile="", work="", fax="", email="", email2="", email3="", homepage="", byear="", ayear="")] + [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
            lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
            title=random_string("title", 20), company=random_string("company", 20),
            address=random_string("address", 20), home=random_phone_string("home", 11),
            mobile=random_phone_string("mobile", 11), work=random_phone_string("work", 11),
            fax=random_phone_string("fax", 11), email=random_string("email", 10),
            email2=random_string("email2", 10), email3=random_string("email3", 10),
            homepage=random_string("homepage", 10), bday="1", bmonth="January",
            byear=random_year_string("byear", 11), aday="2", amonth="February", ayear=random_year_string("ayear", 4))
    for i in range(5)
]