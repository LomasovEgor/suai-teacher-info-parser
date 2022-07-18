import requests
from loguru import logger


class HttpRequestMaker:
    @staticmethod
    def send_post_request(url) -> requests.Response:
        try:
            request = requests.post(url)
            if request.status_code == 200:
                return request
            else:
                logger.error(f'connection error {request.status_code=} in send_post_request')
        except Exception as _ex:
            logger.warning(f"Connection error, cant  requests.get({url})", _ex)

    @staticmethod
    def send_get_request(url) -> requests.Response:
        try:
            request = requests.get(url)
            if request.status_code == 200:
                return request
            else:
                logger.error(f'connection error {request.status_code=} in send_get_request')
        except Exception as _ex:
            logger.warning(f"Connection error, cant  requests.get({url})", _ex)
