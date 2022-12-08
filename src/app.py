from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

class Hello(object):
    def __init__(self, msg):
        self._msg = msg

    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, v):
        self._msg = v

    def database(self):
        self.db_client = MongoClient("", serverSelectionTimeoutMS=10, connectTimeoutMS=20000)

        try:
            return self.db_client.server_info() # Forces a call.
        except ServerSelectionTimeoutError:
            return 'Connection error';


def main():
    hello = Hello("Hello World")
    print(hello.msg)


if __name__ == '__main__':
    main()
