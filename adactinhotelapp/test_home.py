from .hotelPOM.HomePage import Homepage

class HomePageTest(Homepage):
    def test_home_page(self):
        # open home page
        self.open_home_page()


    def test_register_profile(self):
        # open registeration url and validate fields
        self.register_profile()
