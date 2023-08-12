import os

from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.environ.get("PG_DB_HOST")

if __name__ == '__main__':
    print(DB_HOST)
