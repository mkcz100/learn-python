from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError


class MongoManager(object):
    def __init__(self, db_name: str, db_host: str, db_user: str, db_password: str):
        self.client = MongoClient(
            "mongodb://{user}:{passwd}@{host}/{name}".format(
                name=db_name,
                host=db_host,
                user=db_user,
                passwd=db_password
            ),
            serverSelectionTimeoutMS=10,
            connectTimeoutMS=20000)

        try:
            self.server_info = self.client.server_info()
        except Exception:
            self.server_info = None

    @property
    def server_info(self):
        return self._server_info

    @server_info.setter
    def server_info(self, info):
        self._server_info = info
