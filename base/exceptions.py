from rest_framework.exceptions import APIException
from rest_framework import status


class BaseApiException(APIException):
    """Structure for base api exception
    """
    status_code = status.HTTP_400_BAD_REQUEST
    err_message = 'Exception Occurred',
    err_title = 'Exception Occurred'
    err_dev_message = err_message

    def construct_detail(self):
        self.default_detail = {
            'err_message': self.err_message,
            'err_title': self.err_title,
            'err_dev_message': self.err_dev_message,
        }

    def __init__(self, *args, **kwargs):
        self.construct_detail()
        super().__init__(*args, **kwargs)