"""Модуль описания тестового контекста."""

# from pyqaunicore.test_context import TestContext

from pyqatools.assertions.assert_step import assert_step

from config.config_general import config_general
from models.user_models import UserModel
from support.loggers.testrun_logger import logger
from support.reporters.testrun_reporter import reporter


class Users:
    """Класс данных пользователей."""

    user_admin = UserModel(id=1, name='admin', email='admin@example.com')


class Operations:
    """Класс операций."""


class DbSteps:
    def get_user_by_id(self, user_id):
        return []

    def create_user(self, user_data):
        return None


class FsSteps:
    pass


class LogsSteps:
    def find_record_by_text(self, text):
        return None


db_steps = DbSteps()
fs_steps = FsSteps()
logs_steps = LogsSteps()


class TestContext:
    """Класс тестового контекста."""

    logger = logger
    reporter = reporter
    сonfig = config_general
    db = db_steps
    fs = fs_steps
    logs_steps = logs_steps
    users_data = Users()
    ops = Operations()
    assert_step = assert_step
