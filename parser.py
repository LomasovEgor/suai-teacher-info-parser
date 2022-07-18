from httprequestmaker import HttpRequestMaker
from loguru import logger


class Parser(HttpRequestMaker):
    def get_ids(self, url: str) -> list:
        req_dict = dict(self.send_post_request(url).json())
        ids = []
        for people in req_dict['dictionaries']['people']:
            ids.append(people['id'])
        return ids[1:]

    def get_teachers(self, teacher_ids: list) -> list:
        teachers_list = []
        amount = len(teacher_ids)
        for index, teacher_id in enumerate(teacher_ids):
            logger.debug(f'complete {index}/{amount}')
            teacher_dict = dict(self.send_get_request(f'https://pro.guap.ru/getuserprofile/{teacher_id}').json())
            teachers_list.append(teacher_dict)
        return teachers_list
