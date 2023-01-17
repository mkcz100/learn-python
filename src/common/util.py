import os
import common.constant as constant
from dotenv import load_dotenv
from typing import (
    Dict
)


def get_mongo_credentials() -> Dict:
    load_dotenv()

    return {
        constant.ENV_MONGO_HOST: os.environ.get(constant.ENV_MONGO_HOST),
        constant.ENV_MONGO_DB_NAME: os.environ.get(constant.ENV_MONGO_DB_NAME),
        constant.ENV_MONGO_USER: os.environ.get(constant.ENV_MONGO_USER),
        constant.ENV_MONGO_PASSWORD: os.environ.get(
            constant.ENV_MONGO_PASSWORD)
    }


def build_path(relative_path) -> str:
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), relative_path)
