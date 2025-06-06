from sys import maxsize

class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None, address=None, home=None, mobile=None, work=None,
                       fax=None, email=None, email2=None, email3=None, homepage=None, bday=None, bmonth=None, byear=None, aday=None, amonth=None, ayear=None, id=None, all_phones_from_home_page=None, all_email_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax  = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_email_from_home_page = all_email_from_home_page

    def __repr__(self):
        return "%s:%s %s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s" % (self.id, self.firstname,
                                        self.lastname, self.nickname, self.title, self.company, self.address, self.home,
                                        self.mobile, self.work, self.fax, self.email, self.email2, self.email3, self.homepage,
                                        self.bday, self.bmonth, self.byear, self.aday, self.amonth, self.ayear,
                                        self.id, self.all_phones_from_home_page, self.all_email_from_home_page)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize