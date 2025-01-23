from behave import when, given, then
import requests


@given('I send a GET request')
# sends request to URL
def send_request(context):
    context.response = requests.get(url='https://api.coindesk.com/v1/bpi/currentprice.json')


@then('The response status code should be (?P<apistatus_code>.*)')
# Validate status code
def verify_status_code(context, apistatus_code):
    response_status_code = context.response.status_code
    assert response_status_code == int(
        apistatus_code), f"Expected status code {apistatus_code}, but got {response_status_code}"


@when('I should get response for 3 BPIs and validate the Description')
def get_bpi_response(context):
    # Validate the response of 3 BPIs and validate the description.
    response_json = context.response.json()
    bpi = response_json['bpi']

    for key, value in bpi.items():
        assert key in ['USD', 'GBP', 'EUR'], f" Wrong bpi {key}"
        if key == 'GBP':
            assert 'British Pound Sterling' in value['description'], f"Wrong Description"
