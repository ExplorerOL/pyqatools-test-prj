import pytest
from pytest_assert_that import assert_that

# from pyqatools.testrunner.pytest.base_test_class import BaseTestClass
from models.user_models import UserModel
from support.testrunner.base_test import BaseTest


class RestClient:
    def get_user_by_id(self, user_id):
        return UserModel(id=user_id, name='user1', email='user1@example.com')

    def update_user(self, user_data):
        return None


@pytest.fixture
def rest_client():
    return RestClient()


class TestTestContext(BaseTest):
    def test_using_context_example_1(self, rest_client):
        """1. Тест использования контекста."""
        with self.ARRANGE('подготовка тестовых данных'):
            user = self.context.users_data.user_admin
            self.context.db.create_user(user_data=user)
        with self.ACT('создание пользователя по API'):
            user.name = 'new_name'
            rest_client.update_user(user_data=user)
        with self.ASSERT('проверка результатов по API'):
            actual_db_user_data = rest_client.get_user_by_id(user_id=user.id)
            assert_that(actual_db_user_data).is_equal_to(user)
        with self.ASSERT('проверка результатов в БД'):
            actual_db_user_data = self.context.db.get_user_by_id(user_id=user.id)
            assert_that(actual_db_user_data).is_equal_to(user)
        with self.ASSERT('проверка записи в логе'):
            actual_db_user_data = self.context.logs.find_record_by_text(text=user.name)
            assert_that(actual_db_user_data).is_not_none()
