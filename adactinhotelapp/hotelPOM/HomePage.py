from seleniumbase import BaseCase
import openpyxl
import os

class Homepage(BaseCase):

    expected_url = "https://adactinhotelapp.com/index.php"
    reg_url = "https://adactinhotelapp.com/Register.php"
    username = "#username"
    password = "#password"
    newuser = "a[href='Register.php']"
    login = "#login"
    logo = "img[alt='AdactIn Group']"

    password2 = "#re_password"
    fullname = "#full_name"
    email = "#email_add"
    captcha = "#captcha-form"
    expected_error_message1 = "#username_span"
    expected_error_message2 = "#password_span"
    expected_error_message3 = "#re_password_span"
    expected_error_message4 = "#email_add_span"
    expected_error_message5 = "#captcha_span"
    expected_error_message6 = "a[href='index.php']"

    reset = "#Reset"


    TnC = "#tnc_box"

    def open_home_page(self):
        # Launch home page
        self.open(self.expected_url)
        # verify title
        self.assert_title("Adactin.com - Hotel Reservation System")
        self.save_screenshot("Launching HomePage", "custom_screenshots")
        self.assert_element("table.header > tbody > tr:nth-child(1) > td:nth-child(1) > img")
        # scroll and verify copyright
        self.scroll_to_bottom()
        self.assert_text("2020", ".footer")

        # click on new user registration
        self.click(self.newuser)

        # assert the registration page
        register_url = self.get_current_url()
        self.assert_true("Register.php" in register_url)
        self.save_screenshot("New User", "custom_screenshots")

    def register_profile(self):
        # launch register user url
        self.open(self.reg_url)

        flags = [False] * 6
        flag1, flag2, flag3, flag4, flag5, flag6 = flags

        # load the excel workbook
        file_path = "C:/Cyber Physical/comp3217-lab2-main/pythonProject/pythonProject/pythonAutomation/venv/adactinhotelapp/RegisterNew.xlsx"
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active

        # need to go thru all the rows and feed into the register form
        for row in sheet.iter_rows(min_row=2):

            self.input(self.username, row[0].value)
            self.type(self.password, row[1].value)
            self.type(self.password2, row[2].value)

            self.type(self.fullname, row[3].value)
            self.type(self.email, row[4].value)

            if (row[5].value is not None):
                self.type(self.captcha, row[5].value)
            else:
                self.wait(10)

            error_message1 = row[6].value
            error_message2 = row[7].value
            error_message3 = row[8].value
            error_message4 = row[9].value
            error_message5 = row[10].value
            error_message6 = row[11].value


            self.click("#tnc_box")

            if (self.assert_element_present("#Submit")):
                self.click("#Submit")
                if (error_message1 is not None):
                    self.assert_text(error_message1, self.expected_error_message1)
                    flag1 = True
                if (error_message2 is not None):
                    self.assert_text(error_message2, self.expected_error_message2)
                    flag2 = True
                if (error_message3 is not None):
                    self.assert_text(error_message3, self.expected_error_message3)
                    flag3 = True
                if (error_message4 is not None):
                    self.assert_text(error_message4, self.expected_error_message4)
                    flag4 = True
                if (error_message5 is not None):
                    self.assert_text(error_message5, self.expected_error_message5)
                    flag5 = True
                if (error_message6 is not None):
                    self.assert_text(error_message6, self.expected_error_message6)
                    flag6 = True

            if (flag1 & flag2) or (flag1 & flag3) or (flag4) or (flag5) or (flag6):
                status = "PASS"
                flags = [False] * 6
                flag1, flag2, flag3, flag4, flag5, flag6 = flags

            # Save the workbook
            #workbook.save("RegisterNew.xlsx")

