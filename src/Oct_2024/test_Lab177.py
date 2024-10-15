# Create Booking Testcase
# Verify that booking id is not Null
# Status Code
# Booking Id should not be null
# Headers
# Request Module

# URL, Authorization, Payload, Content, Query Param, Path - Request
# Response -> Body verify Assert, Status Codes --> Verify , Time, Header we can verify, JSON Schema

import pytest
import allure
import requests


@allure.title("Test Get Request - Restful Booker Project #1-1")
@allure.description("TC#1 -> Verify that GET Request with ID works")
@allure.tag("regression", "p0", "smoke")
@allure.label("owner", "Dhir Kothari")
@allure.testcase("TC#1")
@pytest.mark.smoke
def test_get_single_request_by_id_positive():
    url = "https://restful-booker.herokuapp.com/booking/1"
    response_data = requests.get(url)
    if response_data.headers.get("Content-Type") == "application/json":
        print(response_data.json())
    else:
        print("Non-JSON response received:", response_data.text, response_data.status_code)
    #print(response_data.text)
    #print(response_data.json())
    #print(response_data.headers)
    #assert response_data.status_code == 200

    print("***********************")

    assert response_data.status_code == 200
    print(response_data.text)
    try:
        print(response_data.json())
    except requests.exceptions.JSONDecodeError:
        print("Response is not in JSON format")

@allure.title("Test Get Request - Restful Booker Project #1-2")
@allure.description("TC#2 -> Verify that GET Request with Invalid Booking ID")
@allure.tag("regression", "p0", "smoke")
@allure.label("owner", "Dhir Kothari")
@allure.testcase("TC#2")
@pytest.mark.smoke
def test_get_single_request_by_id_negative():
    url = "https://restful-booker.herokuapp.com/booking/-1"
    response_data = requests.get(url)
    if response_data.headers.get("Content-Type") == "application/json":
        print(response_data.json())
    else:
        print("Non-JSON response received:", response_data.text, response_data.status_code)
    #print(response_data.text)
    #print(response_data.json())
    #print(response_data.headers)
    #assert response_data.status_code == 200

    print("***********************")

    assert response_data.status_code == 404
    print(response_data.text)
    try:
        print(response_data.json())
    except requests.exceptions.JSONDecodeError:
        print("Response is not in JSON format")

@allure.title("Test Get Request - Restful Booker Project #1-3")
@allure.description("TC#3 -> Verify that GET Request with Invalid Booking ID with 404 output")
@allure.tag("regression", "p0", "smoke")
@allure.label("owner", "Dhir Kothari")
@allure.testcase("TC#3")
@pytest.mark.smoke
def test_get_single_request_by_id_negative2():
    url = "https://restful-booker.herokuapp.com/booking/invalid"
    response_data = requests.get(url)
    if response_data.headers.get("Content-Type") == "application/json":
        print(response_data.json())
    else:
        print("Non-JSON response received:", response_data.text, response_data.status_code)
    #print(response_data.text)
    #print(response_data.json())
    #print(response_data.headers)
    #assert response_data.status_code == 200

    print("***********************")

    assert response_data.status_code == 404
    print(response_data.text)
    try:
        print(response_data.json())
    except requests.exceptions.JSONDecodeError:
        print("Response is not in JSON format")