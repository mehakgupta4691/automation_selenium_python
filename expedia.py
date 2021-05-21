import expedia.constants as const
import os
from selenium import webdriver


class Expedia(webdriver.Chrome):
    def __init__(self, driver_path=r":/Users/mehakgupta4691/Desktop/SeleniumDrivers",teardown=False):
                
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Expedia, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    ''' 
    def select_place_to_go(self, place_to_go):
        search_field = self.find_element_by_class('uitk-field-label')
        print(search_field)
        search_field.clear()
        search_field.send_keys(place_to_go)

        first_result = self.find_element_by_class_name('truncate')
            
        first_result.click()
    '''

    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element_by_css_selector(
            f'td[data-day ="{check_in_date}"]'
        )

        check_in_element.click()

        check_out_element = self.find_element_by_css_selector(
             f'td[data-day="{check_out_date}"]'
         )
        check_out_element.click()
    

