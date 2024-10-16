# API Request - HTTP Request

import allure
import pytest
import requests

@allure.title("Test #1 - Create Booking CRUD Positive")
@allure.description("TC#1 -> Verify the create booking")
@allure.tag("regression", "p0", "smoke")
@allure.label("owner", "Dhir Kothari")
@allure.testcase("TC#1")
@pytest.mark.crud
def test_create_booking_positive_tc1():
    # To Make Request
    # URL
    # Method - POST
    # Headers - Content-Type=Application/json
    # Payload / Data / Body - Dict / JSON
    # Auth (No)
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "Sally",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
        "checkin": "2013-02-23",
        "checkout": "2014-10-23"
    },
    "additionalneeds": "Breakfast"
    }

    # Status Code
    response = requests.post(url=URL, headers=headers, json=payload)
    assert response.status_code == 200
    response_Data = response.json()

    bookingid = response_Data["bookingid"]
    assert bookingid is not None
    assert bookingid > 0
    assert type(bookingid) == int

    firstname = response_Data["booking"]["firstname"]
    lastname = response_Data["booking"]["lastname"]
    totalprice = response_Data["booking"]["totalprice"]
    depositpaid = response_Data["booking"]["depositpaid"]
    checkin = response_Data["booking"]["bookingdates"]["checkin"]
    checkout = response_Data["booking"]["bookingdates"]["checkout"]

    assert firstname == "Sally"
    assert lastname == "Brown"
    assert totalprice == 111
    assert depositpaid == True
    assert checkin == "2013-02-23"
    assert checkout == "2014-10-23"

    # JSON Schema Validation
    # Time Response

@allure.title("Test #2 - Create Booking CRUD Negative")
@allure.description("TC#2 -> Verify booking is not created with {} data")
@allure.tag("regression", "p0", "smoke")
@allure.label("owner", "Dhir Kothari")
@allure.testcase("TC#2")
@pytest.mark.crud
def test_create_booking_negative_tc2():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    payload = {} # 500 Error

    # Status Code
    response = requests.post(url=URL, headers=headers, json=payload)
    print(type(URL))
    print(type(headers))
    print(type(payload))

    # Assertions
    assert response.status_code == 500


@allure.title("Test #3 - Create Booking CRUD with string totalprice")
@allure.description("TC#3 -> Verify booking is not created with string total price")
@allure.tag("regression", "p0", "smoke")
@allure.label("owner", "Dhir Kothari")
@allure.testcase("TC#3")
@pytest.mark.crud
def test_create_booking_negative_tc3(): # Raise a Bug to Client or Dev
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "Sally",
        "lastname": "Brown",
        "totalprice": "Dhir",
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2013-02-23",
            "checkout": "2014-10-23"
        },
        "additionalneeds": "Breakfast"
    }

    # Status Code
    response = requests.post(url=URL, headers=headers, json=payload)
    print(type(URL))
    print(type(headers))
    print(type(payload))

    # Assertions
    assert response.status_code == 200


@allure.title("Test #4 - Create Booking CRUD with negative totalprice")
@allure.description("TC#4 -> Verify booking is not created with negative total price")
@allure.tag("regression", "p0", "smoke")
@allure.label("owner", "Dhir Kothari")
@allure.testcase("TC#4")
@pytest.mark.crud
def test_create_booking_negative_tc4(): # Raise a Bug to Client or Dev
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "Sally",
        "lastname": "Brown",
        "totalprice": "-1",
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2013-02-23",
            "checkout": "2014-10-23"
        },
        "additionalneeds": "Breakfast"
    }

    # Status Code
    response = requests.post(url=URL, headers=headers, json=payload)
    print(type(URL))
    print(type(headers))
    print(type(payload))

    # Assertions
    
    assert response.status_code == 500

