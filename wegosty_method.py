import sys
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import wegosty_locators as locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

s = Service(executable_path='venv/chromedriver.exe')
driver = webdriver.Chrome(service=s)
l = 0.25


def setUp():
    print(f'launch {locators.app} App')
    print('---------------~*~---------------------')

    # Make browser full screen
    driver.maximize_window()

    # Give the browser up to 30 seconds to respond
    driver.implicitly_wait(30)

    # Navigate the Wegostudy app website
    driver.get(locators.wegosty_homepage_url)

    if driver.current_url == locators.wegosty_homepage_url and driver.title == locators.wegosty_homepage_title:
        print('browser launched!')
        print(f'{locators.app} Url is {driver.current_url}\n{locators.app} website title is: {driver.title}')
        sleep(0.25)
    else:
        print('please check!')
        tearDown()


def login():
    driver.find_element(By.LINK_TEXT, 'LOGIN').click()
    sleep(l)
    driver.find_element(By.ID, 'user_email').send_keys(locators.admin_username)
    sleep(1)
    driver.find_element(By.ID, 'user_password').send_keys(locators.admin_password)
    sleep(1)
    driver.find_element(By.XPATH, "//input[@value='SIGN IN']").click()


def log_out():
    driver.find_element(By.XPATH, '//span[contains(text(),"Ch Velasco")]').click()
    sleep(l)
    driver.find_element(By.LINK_TEXT, 'Log out').click()
    sleep(l)


def create_new_student():
    driver.find_element(By.LINK_TEXT, 'My WeGoStudy').click()
    sleep(1)
    driver.find_element(By.LINK_TEXT, 'Students').click()
    sleep(1)
    driver.find_element(By.LINK_TEXT, 'Create New Student').click()
    sleep(1)
    # __________________Personal_Information______________________________
    driver.find_element(By.ID, 'user_student_detail_attributes_first_name').send_keys(locators.first_name)
    sleep(0.3)
    driver.find_element(By.ID, 'user_student_detail_attributes_last_name').send_keys(locators.last_name)
    sleep(0.3)
    driver.find_element(By.ID, 'user_student_detail_attributes_preferred_name').send_keys(locators.first_name)
    sleep(0.3)
    # driver.find_element(By.ID, 'user_student_detail_attributes_passport_number').send_keys(locators.passport_number)
    # sleep(1)
    driver.find_element(By.ID, 'phone_number').send_keys(locators.phone_number)
    sleep(0.3)
    driver.find_element(By.ID, 'select2-user_student_detail_attributes_country_of_citizenship-container').click()
    sleep(0.3)
    driver.find_element(By.XPATH, '//input[@type="search"]').send_keys('Canada')
    sleep(0.3)
    driver.find_element(By.XPATH, '//*[@id="user_student_detail_attributes_country_of_citizenship"]/option[40]').click()
    sleep(0.3)
    driver.find_element(By.ID, 'user_student_detail_attributes_passport_number').send_keys(locators.passport_number)
    sleep(0.3)
    driver.find_element(By.ID, 'user_student_detail_attributes_birth_date').send_keys('2000-03-15')
    sleep(0.3)
    driver.find_element(By.ID, 'user_student_detail_attributes_birth_date').clear()
    sleep(0.3)
    driver.find_element(By.ID, 'user_student_detail_attributes_birth_date').send_keys('2000 03 1')
    sleep(0.3)
    # __________________Contact Information______________________________
    driver.find_element(By.ID, 'user_student_detail_attributes_address_attributes_mailing_address').send_keys(
        locators.mailing_address)
    sleep(0.3)
    driver.find_element(By.LINK_TEXT, 'Country').click()
    sleep(0.3)
    driver.find_element(By.XPATH,
                        '//*[@id="user_student_detail_attributes_address_attributes_country_chosen"]/div/ul/li[40]').click()
    sleep(0.6)
    driver.find_element(By.LINK_TEXT, 'Province/State').click()
    sleep(0.6)
    driver.find_element(By.XPATH,
                        '//*[@id="user_student_detail_attributes_address_attributes_state_chosen"]/div/ul/li[3]').click()
    sleep(0.6)
    driver.find_element(By.LINK_TEXT, 'City').click()
    sleep(0.6)
    driver.find_element(By.XPATH,
                        '//*[@id="user_student_detail_attributes_address_attributes_city_chosen"]/div/ul/li[30]').click()
    sleep(0.6)
    driver.find_element(By.ID, 'user_student_detail_attributes_address_attributes_zip_code').send_keys(
        locators.postal_code)
    sleep(0.6)
    driver.find_element(By.ID, 'user_email').send_keys(locators.user_email)
    sleep(0.6)
    # __________________Education Information______________________________
    driver.find_element(By.LINK_TEXT, 'Credentials').click()
    sleep(0.6)
    driver.find_element(By.XPATH,
                        '//*[@id="user_student_detail_attributes_user_educations_attributes_0_credentials_chosen"]/div/ul/li[3]').click()
    sleep(0.3)
    driver.find_element(By.ID, 'user_student_detail_attributes_user_educations_attributes_0_school_name').send_keys(
        'CCTB')
    sleep(0.3)
    driver.find_element(By.ID, 'user_student_detail_attributes_user_educations_attributes_0_program').send_keys('SQTA')
    sleep(0.3)
    # _______________________________________
    driver.find_element(By.LINK_TEXT, 'GPA Scale').click()
    sleep(0.3)
    driver.find_element(By.XPATH,
                        '//*[@id="user_student_detail_attributes_user_educations_attributes_0_gpa_scale_chosen"]/div/div/input').send_keys(
        '100')
    sleep(0.3)
    driver.find_element(By.XPATH,
                        '//*[@id="user_student_detail_attributes_user_educations_attributes_0_gpa_scale_chosen"]/a/span').select_by_visible_text(
        '100')
    sleep(0.3)
    # __________________________________________
    driver.find_element(By.ID, 'user_student_detail_attributes_user_educations_attributes_0_gpa').send_keys('4.0')
    sleep(0.3)
    # driver.find_element(By.XPATH, '//input[@value="Save"]').click()


def create_application():
    driver.find_element(By.XPATH, '//span[contains(text(),"My WeGoStudy")]').click()
    sleep(l)
    driver.find_element(By.LINK_TEXT, 'Students').click()
    sleep(l)
    driver.find_element(By.LINK_TEXT, 'Create Application').click()
    sleep(l)
    # ----------------Course Information----------------#
    driver.find_element(By.LINK_TEXT, "Select School").click()
    driver.find_element(By.XPATH, '//input[@class="chosen-search-input"]').send_keys('British Columbia')
    sleep(l)
    driver.find_element(By.XPATH, '//div[@id="admission_institute_detail_id_chosen"]/div/ul/li[1]').click()
    sleep(l)
    driver.find_element(By.LINK_TEXT, "Select Course").click()
    driver.find_element(By.XPATH, '//div[@id="admission_institute_program_id_chosen"]/div/ul/li[2]').click()
    sleep(l)
    driver.find_element(By.LINK_TEXT, "Select Starting Semester").click()
    driver.find_element(By.XPATH, '//div[@id="admission_starting_semester_chosen"]/div/ul/li[2]').click()
    sleep(l)
    driver.find_element(By.LINK_TEXT, "Select Start Day").click()
    driver.find_element(By.XPATH, '//div[@id="admission_start_day_chosen"]/div/ul/li[2]').click()
    sleep(l)
    driver.find_element(By.LINK_TEXT, "Select Year").click()
    driver.find_element(By.XPATH, '//div[@id="admission_start_year_chosen"]/div/ul/li[2]').click()
    sleep(l)
    # ----------------Personal Information----------------#
    driver.find_element(By.XPATH, '//input[@id="admission_date_of_birth"]').clear()
    driver.find_element(By.XPATH, '//input[@id="admission_date_of_birth"]').click()
    i = 1
    while i <= 50:
        driver.find_element(By.XPATH, '//th[@class="next"]').click()
        i += 1
    sleep(l)
    driver.find_element(By.XPATH, '//div[@class="datepicker-days"]').click()
    sleep(l)
    driver.find_element(By.ID, "admission_passport_number").clear()
    driver.find_element(By.ID, "admission_passport_number").send_keys(locators.passport_number)
    driver.find_element(By.ID, "admission_cambrian_id").send_keys(locators.college_ID)
    driver.find_element(By.ID, "admission_study_permit_number").send_keys(locators.student_permit_number)
    driver.find_element(By.ID, "admission_first_language").send_keys(locators.first_language)
    driver.find_element(By.XPATH, '//input[@id="admission_date_of_admission"]').clear()
    sleep(l)
    # driver.find_element(By.XPATH, '//input[@id="admission_date_of_admission"]').send_keys('05-01-2010')
    driver.find_element(By.XPATH, '//input[@id="admission_date_of_admission"]').click()
    sleep(l)
    i = 1
    while i <= 3:
        driver.find_element(By.XPATH, '//th[@class="next"]').click()
        # driver.find_element(By.XPATH,'//body[1]/div[4]/div[1]/table[1]/thead[1]/tr[1]/th[1]').click()
        i += 1
    sleep(l)
    driver.find_element(By.XPATH, '//div[@class="datepicker-days"]').click()
    sleep(l)
    driver.find_element(By.XPATH, "//input[@id='admission_gender_male']").click()
    driver.find_element(By.XPATH, "//input[@id='admission_stay_type_private_residence']").click()
    driver.find_element(By.XPATH, "//input[@value='Save']").click()


def tearDown():
    if driver is not None:
        print(f'_________________Test finished successfully at {datetime.datetime.now()}_________________')
        sleep(2)
        driver.close()
        driver.quit()

        # logger('delleted')


# def logger(action: object):
#     old_instance = sys.stdout
#     log_file = open('message.log', 'a')
#     sys.stdout = log_file
#     print(f'{locators.email}\t'
#           f'{locators.username}\t'
#           f'{locators.password}\t'
#           f'{datetime.datetime.now()}\t'
#           f'{action}')
#     sys.stdout = old_instance
#     log_file.close()

setUp()
login()
create_application()
log_out()
tearDown()
