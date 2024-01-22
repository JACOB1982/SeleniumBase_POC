from faker import Faker
from openpyxl import Workbook


def gen_customer_data():
    fake = Faker()

    FirstName = fake.first_name()
    LastName = fake.last_name()
    BillingAddress = fake.street_address()
    CCnum = fake.credit_card_number(card_type='mastercard')
    # CCType = fake.credit_card_type()
    Expmonth = fake.credit_card_expire().split('/')[0]
    Expyear = fake.credit_card_expire().split('/')[1]
    CVV = fake.credit_card_security_code(card_type='mastercard')

    return FirstName, LastName, BillingAddress, CCnum, Expmonth, Expyear, CVV


def gen_xls_workbook(num_records=10, output_file='Test_Data/customer_data.xlsx'):
    workbook = Workbook()
    sheet = workbook.active
    header = ['FirstName', 'LastName', 'BillingAddress', 'CCnum', 'Expmonth', 'ExpYear', 'CVV']
    sheet.append(header)

    for _ in range(num_records):
        customer_data = gen_customer_data()
        sheet.append(customer_data)

    workbook.save(output_file)
    print(f"Fake customer data saved to {output_file}")


# Example usage

gen_xls_workbook(1, 'customer_data.xlsx')
