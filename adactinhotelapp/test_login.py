# test_login.py

from seleniumbase import BaseCase


class loginfunction(BaseCase):

    def login(self, username, password):
        self.open("https://adactinhotelapp.com/")
        self.input("#username", username)
        self.input("#password", password)
        self.click("#login")
        return None

    def test_successful_login(self):
        self.login("Cyber123", "0519CY")
        self.wait_for_element_visible("#username_show")
        print("***User Login Sucessful***")
