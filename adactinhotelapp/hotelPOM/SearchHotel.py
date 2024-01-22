from seleniumbase import BaseCase
from faker import Faker


class SearchHotelPage(BaseCase):
    expected_url = "https://adactinhotelapp.com/SearchHotel.php"
    location = "#location"
    hotels = "#hotels"
    roomtype = "#room_type"
    numofrooms = "#room_nos"
    checkin = "#datepick_in"
    checkout = "#datepick_out"
    adults = "#adult_room"
    children = "#child_room"
    searchbtn = "#Submit"
    resetbtn = "#Reset"
    selectSearch = "#radiobutton_0"
    continuebtn = "#continue"
    booknow = "#book_now"
    fname = "#first_name"
    lname = "#last_name"
    biladd = "#address"
    ccnum = "#cc_num"
    cctypedrpdwm = "#cc_type"
    cvvnum = "#cc_cvv"
    expmon = "#cc_exp_month"
    expyr = "#cc_exp_year"


    def open_searchotel_page(self):
        self.open(self.expected_url)

    def input_location_value(self):
        self.select_option_by_value(self.location, "London")
        self.select_option_by_value(self.hotels, "Hotel Sunshine")
        self.select_option_by_value(self.roomtype, "Deluxe")
        # self.select_option_by_value(self.numofrooms, "2 - Two")
        self.select_option_by_index(self.numofrooms, 1)
        self.add_text(self.checkin, "20/01/2024")
        self.add_text(self.checkout, "22/01/2024")
        # self.select_option_by_value(self.adults, "2 - Two")
        self.select_option_by_index(self.adults, 1)
        # self.select_option_by_value(self.children, "2 - Two")
        self.select_option_by_index(self.children, 1)
        self.save_screenshot("search_hotel_page", "custom_screenshots")
        self.wait_for_element_clickable(self.searchbtn)
        self.click(self.searchbtn)

        self.wait_for_element_present("#continue")
        self.save_screenshot("Search_Continue_page", "custom_screenshots")

    def continue_book(self):
        self.click(self.selectSearch)
        self.click(self.continuebtn)
        self.wait_for_element_visible(self.booknow)
        fake = Faker()

        self.add_text(self.fname, fake.first_name())
        self.add_text(self.lname, fake.last_name())
        self.add_text(self.biladd, fake.street_address())
        self.add_text(self.ccnum, fake.credit_card_number(card_type='visa'))
        self.select_option_by_text(self.cctypedrpdwm, "VISA")
        self.select_option_by_index(self.expmon, 1)
        self.select_option_by_index(self.expyr, 5)
        self.add_text(self.cvvnum, fake.credit_card_security_code(card_type='visa'))
        self.save_screenshot("Search_Customer_data", "custom_screenshots")
        ''''# try:
        filepath = ".customer_data.xlsx"
        workbook = openpyxl.load_workbook(filepath)
        sheet = workbook.active

        for row in sheet.iter_rows(min_row=2):
            txtfname = row[0].value
            txtlname = row[1].value
            txtbiladd = row[2].value
            txtccnum = row[3].value
            # txtcctypedrpdwm = row[4].value
            txtcvvnum = row[5].value
            txtexpmon = row[6].value
            txtexpyr = row[7].value

            self.add_text(self.fname, txtfname)
            self.add_text(self.lname, txtlname)
            self.add_text(self.biladd, txtbiladd)
            self.add_text(self.ccnum, txtccnum)
            self.select_option_by_text(self.cctypedrpdwm, "VISA")
            self.select_option_by_index(self.expmon, txtexpmon)
            self.select_option_by_index(self.expyr, "20" + txtexpyr)
            self.add_text(self.cvvnum, txtcvvnum)'''

        self.wait_for_element_clickable(self.booknow)
        self.click(self.booknow)
        self.wait_for_element_visible("#my_itinerary")
        self.save_screenshot("Search_Booking_Confimed_page", "custom_screenshots")
        confirmed_url = self.get_current_url()
        self.assert_true("BookingConfirm.php" in confirmed_url)

