from tests.api import TestRestAPI

client = TestRestAPI(address='https://reqbin.com')


def test_check_get_request():
    response = client.testapis.get_request()
    assert 'Simple echo interface for HTTP methods' in response.text, 'Something is wrong'


def test_check_post_request():
    body = {
        'key1': 'value1',
        'key2': 'value2',
    }
    response = client.testapis.post_request(body=body)
    assert 'Success' in response.text, 'Something is wrong'
