import pytest
import common.constant as constant
from common.util import get_mongo_credentials
from mongodb.mongo_manager import MongoManager


def test_connection():
    credentials = get_mongo_credentials()

    manager = MongoManager(credentials[constant.ENV_MONGO_DB_NAME],
                           credentials[constant.ENV_MONGO_HOST],
                           credentials[constant.ENV_MONGO_USER],
                           credentials[constant.ENV_MONGO_PASSWORD])

    assert manager.server_info != None
