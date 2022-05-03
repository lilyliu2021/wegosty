from faker import Faker

fake = Faker(locale='en_CA')

app = 'WeGoStudy'
wegosty_url = 'http://34.233.225.85/students/admissions'
wegosty_homepage_url = 'http://34.233.225.85/'
wegosty_homepage_title = 'WeGoStudy'
admin_username = 'chris.velasco78@gmail.com'
admin_password = '123cctb'
first_name = fake.first_name()
last_name = fake.last_name()
passport_number = f'PA{fake.random_int(100000, 999999)}'
college_ID = fake.random_int(10000, 99999)
student_permit_number = f'SP{fake.random_int(10000, 99999)}'
first_language = 'English'
phone_number = fake.phone_number()
# apartment_number =
mailing_address = fake.street_address()
user_email = fake.email()
# province_state =
# city =
postal_code = fake.postalcode()
# user_email =
# school_name =
# program =
# gpa =
