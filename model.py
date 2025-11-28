"""
1. Setting up sqlite db which will store the contact details
2. Defining Contact object which let's us abstract some functionality
"""


class Contact:
    first: str
    last: str
    phone: str
    email: str

    def __init__(
        self, first: str = "", last: str = "", phone: str = "", email: str = ""
    ):
        self.first = first
        self.last = last
        self.phone = phone
        self.email = email
