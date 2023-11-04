import pytest
from conftest import driver, open_url, registration_page


@pytest.mark.parametrize('last_name, first_name, patronymic, aros, country', [('Ерохин', 'Илья', 'Александрович', 'v00.000.000', 'RU')])
def test_positive_fill_field_with_valid_data(registration_page, last_name, first_name, patronymic, aros, country):
    registration_page.input_text_into_luts_name_field(last_name)
    registration_page.input_text_into_first_name_field(first_name)
    registration_page.input_text_into_patronymic_field(patronymic)
    registration_page.input_text_into_seam_login_field(aros)
    registration_page.input_digits_into_date_field('31052001')
    registration_page.input_text_into_email_field('example@yandex.ru')
    registration_page.input_text_into_seam_login_field(aros)
    registration_page.input_text_into_phone_field('+79114093611')
    registration_page.input_text_into_snils_field('16520472650')
    registration_page.input_text_into_profession_field('QA Engineer')
    registration_page.select_and_choose_country_from_dropdown(country)
    registration_page.input_text_into_city_field('Санкт-Петербург')
    registration_page.input_text_into_name_of_company_field('Sirius')
    registration_page.input_text_into_school_field('Лицей №1')
    registration_page.input_text_into_class_field('1A')
    registration_page.click_confirm_checkbox()
    registration_page.click_user_agreement_personal_data()
    registration_page.click_read_rules()
    registration_page.check_enabled_button()
    registration_page.click_button_go_to_testing()
    registration_page.confirm_page_is_displayed()

def test_all_field_are_requirement(registration_page):
    registration_page.check_disabled_button()


def test_check_email_field_validation(registration_page):
    registration_page.input_text_into_email_field('email')
    registration_page.check_message_incorrect_email()


def test_check_snils_field_doesnt_match(registration_page):
    registration_page.input_digits_into_date_field('31052001')
    registration_page.input_text_into_seam_login_field('12345678910')
    registration_page.snils_error_message_doesnt_match()

def test_check_snils_field_other_error_messages(registration_page):
    registration_page.input_digits_into_date_field('31052001')
    registration_page.input_text_into_snils_field('123456789')
    registration_page.snils_error_message_eleven_digits()
    registration_page.input_text_into_snils_field('Ilia')
    registration_page.snils_error_message_only_digits()

def test_digits_into_phone_field(registration_page):
    registration_page.input_text_into_phone_field('Телефон')

def test_choose_main_and_additional_olympic(registration_page):
    registration_page.select_main_olympic()
    registration_page.select_additional_olympic()

@pytest.mark.parametrize('lust_name, first_name, patronymic, aros, country', [('Ерохин', 'Илья', 'Александрович', 'v00.000.000', 'RU')])
def test_whether_all_checkboxes_are_required(registration_page, lust_name, first_name, patronymic, aros, country):
    registration_page.input_text_into_luts_name_field(lust_name)
    registration_page.input_text_into_first_name_field(first_name)
    registration_page.input_text_into_patronymic_field(patronymic)
    registration_page.input_text_into_seam_login_field(aros)
    registration_page.input_digits_into_date_field('31052001')
    registration_page.input_text_into_email_field('example@yandex.ru')
    registration_page.input_text_into_seam_login_field(aros)
    registration_page.input_text_into_phone_field('+79114093611')
    registration_page.input_text_into_snils_field('16520472650')
    registration_page.input_text_into_profession_field('QA Engineer')
    registration_page.select_and_choose_country_from_dropdown(country)
    registration_page.input_text_into_city_field('Санкт-Петербург')
    registration_page.input_text_into_name_of_company_field('Sirius')
    registration_page.input_text_into_school_field('Лицей №1')
    registration_page.input_text_into_class_field('1A')
    registration_page.check_disabled_button()

def test_change_language(registration_page):
    registration_page.select_lang_switcher_button()
    registration_page.choose_eng_lang()
    registration_page.translated_page_text_is_displayed()