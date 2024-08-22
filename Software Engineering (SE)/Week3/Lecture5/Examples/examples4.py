class Contact:

    def __init__(self, name, number, email=""):
        self.name = name
        self.number = number
        self.email = email

    @property
    def contact_card(self):
        return "Name: {}\nNumber: {}\nEmail: {}".format(self.name, self.number, self.email)


class SpecialContacts(Contact):

    def __init__(self, name, number, email="", address=""):
        super().__init__(name, number, email)
        self.address = address

    def contact_card(self):
        return "Name: {}\nNumber: {}\nEmail: {}\nAddress: {}".format(self.name,
                                                                     self.number,
                                                                     self.email,
                                                                     self.address)