import pytest
from _pytest.fixtures import SubRequest


@pytest.mark.parametrize('number', [1, -2, 3, -1])
def test_numbers(number: int):
    assert number > 0


@pytest.mark.parametrize('number, expected', [
    (1, 1),
    (2, 4),
    (3, 9)
])
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected


@pytest.mark.parametrize('browser', ['chromium', 'firefox', 'webkit'])
@pytest.mark.parametrize('os', ['windows', 'linux', 'debian', 'mac os'])
def test_multiplication_of_numbers(browser: str, os: str):
    assert len(browser + os) > 0


import pytest


@pytest.fixture(params=['chromium', 'firefox', 'webkit'])
def browser(request: SubRequest) -> str:
    return request.param


def test_browser(browser: str):
    print(f'Running in browser: {browser}')


@pytest.mark.parametrize('user', ['Alice', 'Sara'])
class TestOperations:
    @pytest.mark.parametrize('account', ['Credit card', 'Debit card'])
    def test_user_with_operations(self, user: str, account: str):
        print(f'User with operations {user}: {account}')

    def test_user_without_operations(self, user: str):
        print(f'User without operations {user}')


users = {
    '+70000000011': 'User with money on bank account',
    '+70000000022': 'User without money on bank account',
    '+70000000033': 'User with operations on bank account'
}

def format_phone_number(phone_number: str) -> str:
    return f'{phone_number}: {users[phone_number]}'

@pytest.mark.parametrize(
    'phone_number',
    users.keys(),
    ids=format_phone_number
    #ids=lambda phone_number: f'{phone_number}: {users[phone_number]}'
)
def test_identifiers(phone_number: str):
    print(phone_number)
