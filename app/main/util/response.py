from http import HTTPStatus

class Response:
    def __init__(self, body, code=HTTPStatus.OK):
        self.body = body
        self.code = code

    @property
    def flask(self):
        response = {'code': self.code}

        if self.code >= 400:
            response['status'] = 'failed'
            response['error'] = self.body if self.body else "Unknown error"
        else:
            response['status'] = 'ok'
            if self.body:
                response['result'] = self.body

        return response, self.code
