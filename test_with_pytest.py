import httpx
from pytest_httpx import HTTPXMock
from contextlib import nullcontext as does_not_raise
import pytest
from pytest import raises


def send_get_with_json():
    with httpx.Client() as client:
        assert client.get("https://google.com", params={"key1": "value1", "key2": "value2"})


def send_post_with_json():
    with httpx.Client() as client:
        assert client.post("https://google.com", json={"key1": "value1", "key2": "value2"})


# def test_get_json(httpx_mock: HTTPXMock):
#     httpx_mock.add_response(json={"key1": "value1", "key2": "value2"})
#
#     with httpx.Client() as client:
#         assert client.get("https://test_url").json() == [{"key1": "value1", "key2": "value2"}]
#
#
# def test_post_json(httpx_mock: HTTPXMock):
#     httpx_mock.add_response(json=[{"data": {'number': 512, 'person': 'Alex', 'list': ['a','b','c']}}])
#
#     with httpx.Client() as client:
#         data = {'number': 512, 'person': 'Alex', 'list': ['a','b','c']}
#         assert client.post("https://test_url", json=data).json() == [{"data": {'number': 512, 'person': 'Alex', 'list': ['a','b','c']}}]


print(send_get_with_json())
print(send_post_with_json())


@pytest.mark.parametrize(
    ["x", "y", "expectation"],
    [
        (3, 2, does_not_raise()),
        (0, 1, does_not_raise()),
        (1, 0, raises(ZeroDivisionError)),
        (1, "0", raises(TypeError)),
    ],
)
def test_division(x, y, expectation):
    with expectation:
        x / y
