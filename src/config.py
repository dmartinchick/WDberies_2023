from dotenv import dotenv_values
from loguru import logger


class DatabaseURL:

    def __init__(self, env_path: str):
        self.__env_path = env_path
        self.__env = dotenv_values(self.__env_path)
        self.__MODE = self.__env.get("MODE")
        self.__DB_USER = self.__env.get("DB_USER")
        self.__DB_PASSWORD = self.__env.get("DB_PASSWORD")
        self.__DB_HOST = self.__env.get("DB_HOST")
        self.__DB_PORT = int(self.__env.get("DB_PORT"))
        self.__DB_NAME = self.__env.get("DB_NAME")

    @property
    def url(self):
        return f"postgresql+psycopg2://" \
               f"{self.__DB_USER}:" \
               f"{self.__DB_PASSWORD}@" \
               f"{self.__DB_HOST}:" \
               f"{self.__DB_PORT}/" \
               f"{self.__DB_NAME}"

    @property
    def mode(self):
        return self.__MODE


class Proxies:
    def __init__(self, env_path: str):
        self.__env_path = env_path
        self.__env = dotenv_values(self.__env_path)
        self.__proxies_http = self.__env.get("PROXIES")

    @property
    def proxies(self) -> dict:
        return {"http": self.__proxies_http}


class Config:

    def __init__(self, dev_db: DatabaseURL, test_db: DatabaseURL | None = None, proxies: dict | None = None):
        self.__db = dev_db
        self.__test_db = test_db
        self.__proxies = proxies

    @property
    def db(self) -> DatabaseURL:
        return self.__db

    @property
    def test_db(self) -> DatabaseURL:
        return self.__test_db

    @property
    def proxies(self) -> dict:
        return {"http": self.__proxies}


development_db = DatabaseURL('.env')
tets_db = DatabaseURL('.test.env')
proxi = Proxies('.env')

config = Config(dev_db=development_db, test_db=tets_db, proxies=proxi.proxies)
