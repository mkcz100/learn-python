from dotenv import load_dotenv
import os
import common.constant as constant


def get_mongo_credentials():
    load_dotenv()

    return {
        constant.ENV_MONGO_HOST: os.environ.get(constant.ENV_MONGO_HOST),
        constant.ENV_MONGO_DB_NAME: os.environ.get(constant.ENV_MONGO_DB_NAME),
        constant.ENV_MONGO_USER: os.environ.get(constant.ENV_MONGO_USER),
        constant.ENV_MONGO_PASSWORD: os.environ.get(
            constant.ENV_MONGO_PASSWORD)
    }
