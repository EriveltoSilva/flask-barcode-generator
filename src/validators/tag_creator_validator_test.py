from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError
from .tag_creator_validator import tag_creator_validator

class MockRequest:
    def __init__(self, json) -> None:
        self.json = json

def test_tag_creator_validator():
    req = MockRequest(json={"product_code":"12345"})
    resp = tag_creator_validator(req)
    assert resp is None

def test_tag_creator_validator_with_error():
    req = MockRequest(json={"product_code":12345})
    try:
        tag_creator_validator(req)
        assert False
    except Exception as exception:
        assert isinstance(exception, HttpUnprocessableEntityError)
