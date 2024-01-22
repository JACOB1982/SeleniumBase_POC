from .hotelPOM.SearchHotel import SearchHotelPage


class HomePageTest(SearchHotelPage):

    def successful_login(self, username, password):
        self.open("https://adactinhotelapp.com/")
        self.input("#username", username)
        self.input("#password", password)
        self.click("#login")
        self.wait_for_element_visible("#username_show")
        print("***User Login Sucessful*** \n")

    def test_searchhotel_page(self):
        self.successful_login("Cyber123", "0519CY")
        self.open_searchotel_page()
        self.input_location_value()
        self.continue_book()
