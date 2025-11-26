"""
1. Setting up sqlite db which will store the contact details
2. Defining Contact object which let's us abstract some functionality
"""


class Contact:
    def __init__(self, id=None, first=None, last=None, phone=None, email=None):
        self.id = id
        self.first = first
        self.last = last
        self.phone = phone
        self.email = email
