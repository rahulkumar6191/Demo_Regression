import json

from selenium.webdriver.support.wait import WebDriverWait

from DemoUIFeatureFiles.DemoStepDefinition import *
from behave import when, given, then
from selenium import webdriver
from DemoUIFeatureFiles.utils.ui_utils import *
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC


# Load json data
def load_json():
    file = open('json_data/locators.json', 'r')
    loc = json.load(file)
    return loc


@given('I open the browser and navigate to ebay')
def open_browser(context):
    try:
        context.driver = get_driver()
        # Navigate to Ebay Website
        context.driver.get("https://www.ebay.com")
    except Exception as e:
        print("Found Exception while opening website", e)


@when('I search for (?P<product>.*) in the search bar')
def search_product_searchbar(context, product):
    # Here we send the product name to search bar and click on Search button
    context.driver.find_element(By.XPATH, load_json()['search_bar']['value']).send_keys(product)
    context.driver.find_element(By.XPATH, load_json()['search_button']['value']).click()


@when('I click on the first item in the search results')
def click_item(context):
    context.driver.find_element(By.XPATH, load_json()['first_item']['value']).click()


@when('I click on Add to cart on the item listing page')
def click_add_to_cart(context):
    # Wait for the "Add to cart" button to become visible and then click it
    add_to_cart_button = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, load_json()['add_to_cart_button']['value']))
    )
    add_to_cart_button.click()


@then('I should see the cart updated with correct number of items.')
def verify_item_in_cart(context):
    # Check if count of cart elements
    cart_count_value = context.driver.find_element(By.ID, load_json()['cart_count']['value'])
    cart_count = cart_count_value.text
    assert cart_count == '1', f"Expected cart count to be 1, but got {cart_count}"
