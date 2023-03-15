from base.exceptions import BaseApiException

class FileformatNotSupported(BaseApiException):
    err_message = 'The file type is not supported',
    err_title = 'The file type is not supported'
    err_dev_message = err_message