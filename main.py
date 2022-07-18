import json
from loguru import logger

from parser import Parser

if __name__ == '__main__':
    parser = Parser()
    logger.info("start getting ids")
    ids = parser.get_ids('https://pro.guap.ru/getDictionariesAndPeople/')
    logger.info("finish getting ids")
    with open('persons_id.json', 'w', encoding='utf8') as file:
        json.dump(ids, file, indent=2, ensure_ascii=False)

    logger.info("start getting teachers")
    teachers = parser.get_teachers(ids)
    logger.info("start getting ids")
    logger.info(f'total teachers = {len(ids)}')
    with open('teachers.json', 'w', encoding='utf8') as file:
        json.dump(ids, file, indent=2, ensure_ascii=False)
