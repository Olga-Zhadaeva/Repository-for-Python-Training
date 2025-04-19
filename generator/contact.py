from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

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
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))