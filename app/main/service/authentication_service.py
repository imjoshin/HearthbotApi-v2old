from app.main.model.credential import Credential


class AuthenticationService:

    @staticmethod
    def get_token(data):
        try:
            # fetch the user data
            creds = Credential.query.filter_by(client=data.get('client')).first()
            if creds and creds.check_secret(data.get('secret')):
                token = Credential.encode_token(creds.id)
                if token:
                    response_object = {
                        'status': 'success',
                        'token': token.decode()
                    }
                    return response_object, 200
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'Invalid credentials'
                }
                return response_object, 401

        except Exception as e:
            import traceback
            traceback.print_exc()
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Try again'
            }
            return response_object, 500

    @staticmethod
    def get_credentials(new_request):
        # get the auth token
        token = new_request.headers.get('Authorization')
        if token:
            resp = Credential.decode_token(token)
            if not isinstance(resp, str):
                creds = Credential.query.filter_by(id=resp).first()
                return creds

        return None
