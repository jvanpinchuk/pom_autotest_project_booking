from selenium.webdriver.common.by import By
from src.data import generate_weekend


#  ======================         Main Page / no sing in         =======================================
logo = (By.CSS_SELECTOR, "path[fill='#fff'][xpath='1']")
main_popup = (By.CSS_SELECTOR, ".dd5dccd82f")
close_main_popup = (By.CSS_SELECTOR, "button[aria-label='Dismiss sign in information.']")


#  currency
currency_btn = (By.CSS_SELECTOR, "button[data-testid='header-currency-picker-trigger']")
carrency_dashboard = (By.CSS_SELECTOR, "div.e9768bbaf2[bis_skin_checked='1']")
usd_currency_btn = (By.XPATH, "//button//div[contains(text(),'USD')]")
eur_currency_btn = (By.XPATH, "//button//div[contains(text(),'EUR')]")
byn_currency_btn = (By.XPATH, "//button//div[contains(text(),'BYN')]")
eur_currency_sign = (By.XPATH, "//span[contains(text(),'€ ')]")

#  language
language_btn = (By.CSS_SELECTOR, "button[data-testid='header-language-picker-trigger']")
language_dashboard = (By.CSS_SELECTOR, "div.bui-modal__header")
eng_language_btn = (By.CSS_SELECTOR, "a[data-lang='en-gb']")
ru_language_btn = (By.CSS_SELECTOR, "a[data-lang='ru']")
pl_language_btn = (By.XPATH, "//span[normalize-space()='Polski']")
pl_language_pres = (By.XPATH, "//span[normalize-space()='Szukaj']")

#  location
where_input = (By.CSS_SELECTOR, "input[name='ss']")
warsaw_rel_res_btn = (By.XPATH, "(//div[contains(text(),'Warsaw')])[1]")
first_rel_res = (By.XPATH, "//div[normalize-space()='Masovia, Poland']")  # WARSAW
first_rel_res_btn = (By.XPATH, "(//div[@class='e4b761c8b0'])[1]")

#  dates
dates_search = (By.CSS_SELECTOR, "div[data-testid='searchbox-dates-container']")
dates_popup = (By.CSS_SELECTOR, "nav[data-testid='datepicker-tabs']")
start_date_btn = (By.CSS_SELECTOR, f"span[aria-label='{generate_weekend(5)}']")
fin_date_btn = (By.CSS_SELECTOR, f"span[aria-label='{generate_weekend(12)}']")
switch_flex_dates_btn = (By.CSS_SELECTOR, "button[aria-controls='flexible-searchboxdatepicker']")
switch_cal_dates_btn = (By.CSS_SELECTOR, "button[aria-controls='calendar-searchboxdatepicker']")
flex_rb_weekend = (By.CSS_SELECTOR, "label[for=':r19:']")
flex_rb_week = (By.CSS_SELECTOR, "label[for=':r1a:']")
flex_rb_other = (By.CSS_SELECTOR, "label[for=':r1b:']")
flex_chb_month = (By.CSS_SELECTOR, "-------------------")


#  occupancy
occupancy_btn = (By.CSS_SELECTOR, "button[data-testid='occupancy-config']")
occupancy_popup = (By.CSS_SELECTOR, "div[data-testid='occupancy-popup']")
adult_plus_btn = (By.XPATH, "(//button[@type='button'])[8]")
adult_minus_btn = (By.XPATH, "(//button[@type='button'])[7]")
child_plus_btn = (By.XPATH, "(//button[@type='button'])[10]")
child_minus_btn = (By.XPATH, "(//button[@type='button'])[9]")
room_plus_btn = (By.XPATH, "(//button[@type='button'])[12]")
room_minus_btn = (By.XPATH, "(//button[@type='button'])[11]")
done_occupancy_btn = (By.CSS_SELECTOR, "button.d285d0ebe9")


# ---------- search
search_btn = (By.CSS_SELECTOR, "button[type='submit']")
stays_search_result = (By.CSS_SELECTOR, "div[data-testid='property-card']")

#  ======================         Main Page / sing in         =============================
your_account_btn = (By.CSS_SELECTOR, "button[aria-label='Your account menu Your account Genius Level 1']")
manage_account_btn = (By.XPATH, "//div[@id=':re:']//li[1]")
security_btn = (By.XPATH, "//a[@aria-labelledby='mysettings_security_title']")
del_btn = (By.XPATH, "(//button[@type='button'])[7]")
other_rb = (By.CSS_SELECTOR, "label[for='__bui-4'] span[class='XS31O4h6emqWFBtIOW4x']")
other_input = (By.CSS_SELECTOR, "#delete-account-html-elem")
del_account_btn = (By.XPATH, "//button[@data-ga-label='']")


#  ======================         register          =======================================
register_btn = (By.CSS_SELECTOR, "a[aria-label='Create an account']")
email_input = (By.CSS_SELECTOR, "#username")
continue_btn = (By.CSS_SELECTOR, "button[type='submit']")
new_pass_input = (By.CSS_SELECTOR, "#new_password")
confirm_pass_input = (By.CSS_SELECTOR, "#confirmed_password")
create_account_btn = (By.CSS_SELECTOR, "button[type='submit']")
sing_out_btn = (By.CSS_SELECTOR, "button[class='fc63351294 ea925ef36a c0c9498572 cddb75f1fd']]")



#  ======================         sing in         =========================================
sing_in_btn = (By.CSS_SELECTOR, "a[aria-label='Sign in']")
pass_input = (By.CSS_SELECTOR, "#password")
fin_sing_in_btn = (By.CSS_SELECTOR, "button[type='submit']")
your_account = (By.XPATH, "//div[normalize-space()='Your account']")
captcha_element = (By.CSS_SELECTOR, "#px-captcha")


#  ======================         Car rentals         =========================================
car_rentals_btn = (By.CSS_SELECTOR, "#cars")
location_input = (By.CSS_SELECTOR, "#searchbox-toolbox-fts-pickup")
loc_rel_res = (By.XPATH, "//span[contains(text(),'City')]")
pick_up_dates_btn = (By.CSS_SELECTOR, "#searchbox-toolbox-date-picker-pickup-date")
pick_up_date_from = (By.CSS_SELECTOR, f"span[aria-label='{generate_weekend(5)}']")
pick_up_date_to = (By.CSS_SELECTOR, f"span[aria-label='{generate_weekend(6)}']")
drop_off_date_btn = (By.CSS_SELECTOR, "#searchbox-toolbox-date-picker-dropoff-date")
drop_off_date = (By.CSS_SELECTOR, f"span[aria-label='{generate_weekend(12)}']")
car_search_btn = (By.CSS_SELECTOR, "button[data-testid='searchbox-toolbox-submit-button']")



#  ======================         Attractions         =========================================
attractions_btn = (By.CSS_SELECTOR, "#attractions")
where_attr_input = (By.CSS_SELECTOR, "input[placeholder='Where are you going?']")
attr_rel_res = (By.XPATH, "(//a[@country='pl'])[1]")
attr_dates_btn = (By.XPATH, "//div[@class='css-ck8kih']")
attr_date_from = (By.CSS_SELECTOR, f"span[aria-label='{generate_weekend(5)}']")
attr_date_to = (By.CSS_SELECTOR, f"span[aria-label='{generate_weekend(9)}']")
attr_search_btn = (By.CSS_SELECTOR, "button[type='submit']")
attr_search_result = (By.CSS_SELECTOR, "a[data-testid='card']")

