# PUT / PATCH - Request
# URL
# Path - Booking ID
# Token - Auth
# Payload
# Headers

import allure  # pip install allure
import pytest  # pip instal pytest
import requests  # pip install requests

@pytest.fixture
def create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=url, headers=headers, json=json_payload)
    token = response.json()["token"]
    return token

@pytest.fixture
def create_booking():
    URL = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "firstname": "Amit",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=URL, headers=headers, json=json_payload)
    assert response.status_code == 200
    data = response.json()
    booking_id = data["bookingid"]
    return booking_id

class Test_put_patch_request():
    def test_put_request(self, create_token, create_booking):
        base_url = "https://restful-booker.herokuapp.com"
        base_path = "/booking/" + str(create_booking)
        PUT_URL = base_url + base_path
        cookie = "token=" + create_token
        headers = {
            "Content-Type": "application/json",
            "Cookie": cookie
        }

        json_payload = {
            "firstname": "Dhir",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }

        response = requests.put(url=PUT_URL, headers=headers, json=json_payload)
        assert response.status_code == 200
        data = response.json()
        print(data)
        assert data["firstname"] == "Dhir"

    def test_patch_request(self, create_token, create_booking):
        base_url = "https://restful-booker.herokuapp.com"
        base_path = "/booking/" + str(create_booking)
        PUT_URL = base_url + base_path
        cookie = "token=" + create_token
        headers = {
            "Content-Type": "application/json",
            "Cookie": cookie
        }

        json_payload = {
            "firstname": "Dhir",
            "lastname": "Brown",
              }

        response = requests.patch(url=PUT_URL, headers=headers, json=json_payload)
        assert response.status_code == 200
        data = response.json()
        print(data)
        assert data["firstname"] == "Dhir"
        assert data["lastname"] == "Brown"
