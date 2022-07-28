import json
from loguru import logger

from parser import Parser

if __name__ == '__main__':
    logger.info("start getting ids")
    ids = Parser.get_ids('https://pro.guap.ru/getDictionariesAndPeople/')
    logger.info("finish getting ids")

    with open('persons_id.json', 'w', encoding='utf8') as file:
        json.dump(ids, file, indent=2, ensure_ascii=False)

    logger.info(f'total teachers = {len(ids)}')
    logger.info("start getting teachers")
    teachers, failed_ids = Parser.get_teachers(ids)
    logger.info("finish getting teachers")
    logger.warning(f'{failed_ids=}')

    with open('teachers.json', 'w', encoding='utf8') as file:
        json.dump(teachers, file, indent=2, ensure_ascii=False)
