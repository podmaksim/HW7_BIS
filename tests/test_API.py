from pages.api_def_page import create_user
from pages.api_def_page import choice_user
from pages.api_def_page import update_user
from pages.api_def_page import choice_new_user
from pages.api_def_page import delete_user

import random
import pytest
import json
import requests
from pydantic import BaseModel


class User(BaseModel):
    id: str
    username: str
    password: int
    user_new_name: str


input_json = """
{
    "id": "147789",
    "username": "podmaksim",
    "password": 1111,
    "user_new_name": "PODMAX"
}
"""

user_new = User.parse_raw(input_json)

id = user_new.id
user_name = user_new.username
password = user_new.password
new_user_name = user_new.user_new_name


def test_POST():
    assert create_user(id, user_name, password) == {'code': 200, 'type': 'unknown', 'message': id}


def test_GET_positive_1():
    assert choice_user(user_name) == 200


@pytest.mark.xfail
def test_GET_negative():
    assert choice_user('') == 200


def test_PUT_positive():
    assert update_user(id, user_name, new_user_name) == \
           {'code': 200, 'type': 'unknown', 'message': id}


@pytest.mark.xfail
def test_PUT_negative():
    assert update_user(id, '', new_user_name) == \
           {'code': 200, 'type': 'unknown', 'message': id}


def test_GET_new_user_positive():
    assert choice_new_user(new_user_name) == 200


@pytest.mark.xfail
def test_GET_new_user_negative():
    assert choice_new_user('IlonMask') == 200


def test_DELETE_user_positive():
    assert delete_user(new_user_name) == 200


@pytest.mark.xfail
def test_DELETE_user_negative():
    assert delete_user(user_name) == 200
