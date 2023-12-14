import re
from src.posts.utils.parser import parser
from loguru import logger


new_year = 'https://www.wildberries.by/catalog?category=130421&page=1&sort=popular&xsubject=260'
# https://www.wildberries.by/catalog?category=8137&f23796=31136%3B31142&fcolor=16777215&page=1&sort=popular

# https://www.wildberries.by/catalog?category=9990&page=1&sort=popular&xsubject=5858
# 'https://catalog.wb.ru/catalog/clothes_accessories2/v1/catalog?cat=9990&limit=100&sort=popular&page=1&appType=128&curr=byn&lang=ru&dest=-59208&spp=27&xsubject=5858&TestGroup=no_test&TestID=no_test' \


if __name__ == '__main__':
    parser.curl = "https://catalog.wb.ru/catalog/dresses/v1/catalog?cat=8137&limit=100&sort=popular&page=1&appType=128&curr=byn&lang=ru&dest=-59208&spp=27&f23796=31136&fcolor=16777215&TestGroup=no_test&TestID=no_test"
    data = parser.get_responce(how_much_page=1)
    # print(data)
