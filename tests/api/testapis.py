from http import HTTPStatus


class TestAPIs:
    def __init__(self, client):
        self.client = client
        self.client.add_headers({
            "Accept": "*/*",
            "Content-Type": "application/json",
        })

    def get_request(self):
        response = self.client.get('/echo')
        assert response.status_code == HTTPStatus.OK, 'Invalid request'
        return response

    def post_request(self, body: dict):
        response = self.client.post('/echo/post/form', json=body)
        assert response.status_code == HTTPStatus.OK, 'Invalid request'
        return response
