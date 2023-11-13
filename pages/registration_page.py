import time

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pages.BasePage import BasePage
from utilities.settings import BASE_URL


class RegistrationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = BASE_URL

    def open_url(self):
        self.driver.get(self.url)

    lang_switcher_xpath = '//*[@id="index"]/div/div[1]/div/div'
    list_of_langs_xpath = '//*[@id="index"]/div/div[1]/div[2]/div/div'
    english_button_class_name = 'lang_switcher__flag lang_switcher__flag-en '
    eng_lang_xpath = '//*[@id="index"]/div/div[1]/div[2]/div/div/div[2]/div'
    russian_button_class_name = ''
    translated_page_text_xpath = '//*[@id="index"]/div/div[2]/div[4]/div/div/div[1]/div/span/p'

    translated_link_text = 'Your personal data'
    lust_name_xpath = '//*[@id="index"]/div/div[2]/div[4]/div/div/div[2]/label/div[2]/input'
    first_name_xpath = '//*[@id="index"]/div/div[2]/div[4]/div/div/div[3]/label/div[2]/input'
    patronymic_xpath = '//*[@id="index"]/div/div[2]/div[4]/div/div/div[4]/label/div[2]/input'
    date_xpath = '//*[@id="index"]/div/div[2]/div[4]/div/div/div[5]/label/div[2]/div/div/div/input'

    email_xpath = '/html/body/section/div/div[2]/div[4]/div/div/div[6]/label/div[2]/input'
    incorrect_email_xpath = '//*[@id="index"]/div/div[2]/div[4]/div/div/div[6]/div'

    seam_login_xpath = '//*[@id="index"]/div/div[2]/div[4]/div/div/div[7]/label/div[2]/input'
    incorrect_seam_login_xpath = '//*[@id="index"]/div/div[2]/div[4]/div/div/div[7]/div'

    phone_xpath = '//*[@id="index"]/div/div[2]/div[4]/div/div/div[8]/label/div[2]/input'

    insurance_snils_xpath = '//*[@id="index"]/div/div[2]/div[4]/div/div/div[9]/label/div[2]/input'
    snils_eleven_digits_link_text = 'СНИЛС должен состоять ровно из 11 цифр'
    snils_does_not_match_link_text = 'Контрольная сумма СНИЛС не совпадает'
    snils_only_digits_link_text = 'СНИЛС должен содержать только цифры'

    profession_xpath = '//*[@id="index"]/div/div[2]/div[4]/div/div/div[10]/label/div[2]/input'

    country_field_xpath = '//*[@id="index"]/div/div[2]/div[4]/div/div/div[11]/div/div[2]/label/div[2]'
    country_dropdown_list_xpath = '//*[@id="index"]/div/div[2]/div[4]/div/div/div[11]/div/div[2]/label/div[2]/select'

    city_xpath = '//*[@id="index"]/div/div[2]/div[4]/div/div/div[11]/div/div[3]/label/div[2]/input'
    company_name_xpath = '//*[@id="index"]/div/div[2]/div[4]/div/div/div[11]/div/div[4]/label/div[2]/input'
    school_xpath = '//*[@id="index"]/div/div[2]/div[4]/div/div/div[11]/div/div[5]/label/div[2]/input'
    class_xpath = '//*[@id="index"]/div/div[2]/div[4]/div/div/div[11]/div/div[6]/label/div[2]/input'
    main_olympic_xpath = '//*[@id="index"]/div/div[2]/div[4]/div/div/div[12]/ul/li[1]'
    additional_olympic_xpath = '//*[@id="index"]/div/div[2]/div[4]/div/div/div[12]/ul/li[2]'
    data_correctness_agreement_xpath = '//*[@id="index"]/div/div[2]/div[4]/div/div/div[13]/div/label/input'
    user_agreement_personal_data_xpath = '//*[@id="index"]/div/div[2]/div[4]/div/div/div[14]/div/label/input'
    read_rules_xpath = '//*[@id="index"]/div/div[2]/div[4]/div/div/div[15]/div/label/input'
    go_to_testing_xpath = '//*[@id="index"]/div/div[2]/div[4]/button'

    confirm_message_main_olympic_link_text = 'Автостесты. Основная олимпиада'
    confirm_message_additional_olympic_link_text = 'Автостесты. Дополнительная олимпиада'
    confirm_page_back_button_class_name = 'ui-button__content '


# Lang Switcher
    def select_lang_switcher_button(self):
        self.click_on_element('lang_switcher_xpath', self.lang_switcher_xpath)

    def choose_eng_lang(self):
        self.click_on_element('lang_switcher_xpath', self.lang_switcher_xpath)
        time.sleep(5)

        eng_lang_element = self.get_element('eng_lang_xpath', self.eng_lang_xpath)
        eng_lang_element.click()

    def translated_page_text_is_displayed(self):
        time.sleep(5)
        self.display_status('translated_page_text_xpath', self.translated_page_text_xpath)

# Last Name
    def select_lust_name(self):
        self.click_on_element('lust_name_xpath', self.lust_name_xpath)

    def lust_name_field_is_displayed(self):
        self.display_status('lust_name_xpath', self.lust_name_xpath)

    def input_text_into_luts_name_field(self, lust_name):
        self.type_into_element('lust_name_xpath', self.lust_name_xpath, lust_name)

# First Name
    def select_first_name(self):
        self.click_on_element('first_name_xpath', self.first_name_xpath)

    def input_text_into_first_name_field(self, text):
        self.type_into_element('first_name_xpath', self.first_name_xpath, text)

# Patronymic
    def select_patronymic_field(self):
        self.click_on_element('patronymic_xpath', self.patronymic_xpath)

    def input_text_into_patronymic_field(self, text):
        self.type_into_element('patronymic_xpath', self.patronymic_xpath, text)

# Date
    def select_date_field(self):
        self.click_on_element('date_xpath', self.date_xpath)

    def input_digits_into_date_field(self, digits):
        self.type_into_element('date_xpath', self.date_xpath, digits)
        time.sleep(5)

# Email
    def select_email_field(self):
        self.click_on_element('email_xpath', self.email_xpath)

    def input_text_into_email_field(self, text):
        self.type_into_element('email_xpath', self.email_xpath, text)

    def check_message_incorrect_email(self):
        self.display_status('incorrect_email_xpath', self.incorrect_email_xpath)

# Seam Login
    def select_seam_login_field(self):
        self.click_on_element('seam_login_xpath', self.seam_login_xpath)

    def input_text_into_seam_login_field(self, text):
        self.type_into_element('seam_login_xpath', self.seam_login_xpath, text)

    def message_incorrect_seam_login(self):
        self.display_status('incorrect_seam_login_xpath', self.incorrect_seam_login_xpath)

# Phone
    def select_phone_field(self):
        self.click_on_element('phone_xpath', self.phone_xpath)

    def input_text_into_phone_field(self, text):
        self.type_into_element('phone_xpath', self.phone_xpath, text)

# Insurance SNILS
    def select_snils_field(self):
        self.click_on_element('insurance_snils_xpath', self.insurance_snils_xpath)

    def snils_error_message_doesnt_match(self):
        self.display_status_error_message('snils_does_not_match_link_text', self.snils_does_not_match_link_text)

    def input_text_into_snils_field(self, text):
        self.type_into_element('insurance_snils_xpath', self.insurance_snils_xpath, text)

    def snils_error_message_eleven_digits(self):
        self.display_status_error_message('snils_eleven_digits_link_text', self.snils_eleven_digits_link_text)

    def snils_error_message_only_digits(self):
        self.display_status_error_message('snils_only_digits_link_text', self.snils_only_digits_link_text)

# Profession
    def select_profession_field(self):
        self.click_on_element('profession_xpath', self.profession_xpath)

    def input_text_into_profession_field(self, text):
        self.type_into_element('profession_xpath', self.profession_xpath, text)

# Country
    def select_country_field(self):
        self.click_on_element('country_field_xpath', self.country_field_xpath)

    def list_country_is_displayed(self):
        self.click_on_element('country_field_xpath', self.country_field_xpath)
        self.display_status('country_dropdown_list_xpath', self.country_dropdown_list_xpath)

    def select_and_choose_country_from_dropdown(self, country):
        self.click_on_element('country_field_xpath', self.country_field_xpath)
        time.sleep(5)

        country_select_element = self.get_element('country_dropdown_list_xpath', self.country_dropdown_list_xpath)

        select = Select(country_select_element)
        select.select_by_value(country)

# City
    def select_city_field(self):
        self.click_on_element('city_xpath', self.city_xpath)

    def input_text_into_city_field(self, text):
        self.type_into_element('city_xpath', self.city_xpath, text)

# Name Of Company
    def select_name_of_company_field(self):
        self.click_on_element('company_name_xpath', self.company_name_xpath)

    def input_text_into_name_of_company_field(self, text):
        self.type_into_element('company_name_xpath', self.company_name_xpath, text)

# School
    def select_school_field(self):
        self.click_on_element('school_xpath', self.school_xpath)

    def input_text_into_school_field(self, text):
        self.type_into_element('school_xpath', self.school_xpath, text)

# Class
    def select_class_field(self):
        self.click_on_element('class_xpath', self.class_xpath)

    def input_text_into_class_field(self, text):
        self.type_into_element('class_xpath', self.class_xpath, text)

# Chose Mail Olympic
    def select_main_olympic(self):
        self.click_on_element('main_olympic_xpath', self.main_olympic_xpath)

# Chose Additional Olympic
    def select_additional_olympic(self):
        self.click_on_element('additional_olympic_xpath', self.additional_olympic_xpath)

# Check-Boxes
    def click_confirm_checkbox(self):
        self.click_on_element('data_correctness_agreement_xpath', self.data_correctness_agreement_xpath)

    def click_user_agreement_personal_data(self):
        self.click_on_element('user_agreement_personal_data_xpath', self.user_agreement_personal_data_xpath)

    def click_read_rules(self):
        self.click_on_element('read_rules_xpath', self.read_rules_xpath)

# Button Go to Testing
    def check_enabled_button(self):
        button = self.get_element('go_to_testing_xpath', self.go_to_testing_xpath)
        return button.is_enabled()

    def check_disabled_button(self):
        button = self.get_element('go_to_testing_xpath', self.go_to_testing_xpath)
        return not button.is_enabled()


    def click_button_go_to_testing(self):
        self.click_on_element('go_to_testing_xpath', self.go_to_testing_xpath)
        time.sleep(5)

# Confirm Message/page
    def confirm_page_is_displayed(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, self.confirm_page_back_button_class_name))
            )
            self.display_status('confirmation_success_message_text', self.confirm_page_back_button_class_name)
        except Exception:
            pass