from httprequestmaker import HttpRequestMaker
from loguru import logger
from exceptions import RequestError


class Parser:
    @staticmethod
    def get_ids(url: str) -> list:
        req_dict = dict(HttpRequestMaker.send_post_request(url).json())
        ids = []
        for people in req_dict['dictionaries']['people']:
            ids.append(people['id'])
        return ids[1:]

    @staticmethod
    def get_teachers(teacher_ids: list) -> tuple[list[dict], list]:
        """
        Get dict with teachers info
        :param teacher_ids: list
        :return: teachers_list: list[dict], failed_ids: list
        """
        teachers_list = []
        failed_ids = []
        amount = len(teacher_ids)
        for index, teacher_id in enumerate(teacher_ids):
            try:
                teacher_dict = dict(HttpRequestMaker.send_get_request(f'https://pro.guap.ru/getuserprofile/{teacher_id}').json())
                teachers_list.append(teacher_dict)
                logger.debug(f'complete {index}/{amount}')
            except RequestError as _ex:
                logger.warning(f"RequestError on {teacher_id=}", _ex)
                failed_ids.append(teacher_id)
        return teachers_list, failed_ids
