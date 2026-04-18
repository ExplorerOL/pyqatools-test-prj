# from assertpy import assert_that
# import allure

from pyqatools.assertions import assert_soft_pytest_check as assert_soft
from pyqatools.assertions.assert_step import assert_step
from pytest_assert_that import assert_that
from pytest_check.check_raises import raises

from services.service_one.steps.service_one_steps import service_one_steps
from support.assertions.custom_assertions import CustomAssertions
from support.testrunner.base_test import BaseTest

ACTUAL_DICT = {
    'key1': 'value11',
    'key2': 'value2',
    'key3': 'value3',
    'key4': 'value4',
    'key5': 'value5',
}
EXPECTED_DICT = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value33',
    # 'key4': 'value44',
    # 'key5': 'value55',
    # 'key1': 'value11',
    # 'key2': 'value22',
    # 'key3': 'value33',
    # 'key44': 'value4',
    # 'key55': 'value5',
}


class Person(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def say_hello(self):
        return 'Hello, %s!' % self.first_name


class TestAssertions(BaseTest):
    def test_assert_example_1(self):
        """Тест с assert."""
        assert ACTUAL_DICT == EXPECTED_DICT

    def test_assert_example_2(self):
        """Тест с assert и дополнительным сообщением."""
        assert ACTUAL_DICT == EXPECTED_DICT, 'Фактический словарь не совпадает с ожидаемым!'

    def test_assert_example_3(self):
        """Тест с assert и разметкой шагов."""
        with self.ASSERT('словари одинаковые'):
            assert ACTUAL_DICT == EXPECTED_DICT

    def test_assert_example_4(self):
        """Тест с assert_that и разметкой шагов."""
        with self.ARRANGE('подготовка тестовых данных'):
            actual_dict = {
                'key1': {
                    'key2': 'value2',
                    'key3': 'value3',
                },
            }
            expected_dict = {
                'key1': 'value11',
                'key2': 'value22',
                'key3': 'value33',
            }
        with self.ASSERT('словари одинаковые'):
            assert_that(actual_dict).is_equal_to(expected_dict)

    def test_assert_example_4_1(self):
        """Тест с assert_that и разметкой шагов."""
        with self.ARRANGE('подготовка тестовых данных'):
            actial_list = [1, 2, 3, 4, 5]
            expected_list = [1, 2, 3, 'a', 5]
        with self.ASSERT('словари одинаковые'):
            assert_that(actial_list).is_equal_to(expected_list)

    def test_assert_example_5(self):
        """5. Тест с пользовательской проверкой."""
        with self.ARRANGE('подготовка тестовых данных'):
            actual_list = [1, 2, 3, 4, 5]
            expected_list = [1, 2, 3, 'a', 5]
        with self.ASSERT('словари одинаковые'):
            CustomAssertions.verify_equal(actual_val=actual_list, expected_val=expected_list)

    def test_assert_example_6(self):
        """Тест с группировкой проверок."""
        with self.ARRANGE('подготовка данных'):
            lst = [1, 2, 3, 4]
            orig_lst_len = len(lst)
        with self.ACT('добавление нового элемента в список'):
            new_elem = 5
            lst.append(new_elem)
        with self.ASSERT('элемент добавлен в список'):
            assert len(lst) == orig_lst_len + 1
            assert new_elem in lst

    def test_assert_example_7(self):
        """Тест с группировкой проверок с использованием assertpy."""
        with self.ARRANGE('подготовка списка данных'):
            lst = [1, 2, 3, 4]
            orig_lst_len = len(lst)
        with self.ACT('добавление нового элемента в список'):
            new_elem = 5
            lst.append(new_elem)
        with self.ASSERT('элемент добавлен в список'):
            assert_that(lst).is_length(orig_lst_len + 1).contains(new_elem)

    def test_assert_example_8(self):
        """Тест с очень длинной цепочкой проверок assertpy."""
        with self.ARRANGE('подготовка списка данных'):
            lst = [1, 2, 3, 4]
            orig_lst_len = len(lst)
        with self.ACT('добавление нового элемента в список'):
            new_elem = 5
            lst.append(new_elem)
        with self.ASSERT('очень длинная цепочка проверок'):
            assert_that(lst).is_length(orig_lst_len + 1).starts_with(1).ends_with(5).contains(
                new_elem
            ).does_not_contain('x', 'y').is_sorted()

    def test_assert_example_9(self):
        """Тест со сложной проверкой assertpy."""
        with self.ARRANGE('подготовка списка данных'):
            users = [
                {'user': 'Fred', 'age': 36, 'active': True},
                {'user': 'Bob', 'age': 40, 'active': False},
                {'user': 'Johnny', 'age': 13, 'active': True},
            ]
        with self.ASSERT('сложная проверка'):
            assert_that(users).extracting('user', filter=lambda x: x['age'] > 20, sort='age').is_equal_to(
                ['Fred', 'Bob']
            )

    def test_assert_example_10(self):
        """Тест сравнение словарей не по всем ключам."""
        with self.ASSERT('проверка равенства словарей'):
            assert_that(ACTUAL_DICT).is_equal_to(EXPECTED_DICT, ignore=['key3', 'key4', 'key5'])

    def test_assert_example_11(self):
        """Тест много блокирующих проверок."""
        with self.ASSERT('выполнение нескольких проверок'):
            assert_that(ACTUAL_DICT['key1']).is_equal_to(EXPECTED_DICT['key1'])
            assert_that(ACTUAL_DICT['key2']).is_equal_to(EXPECTED_DICT['key2'])
            assert_that(ACTUAL_DICT['key3']).is_equal_to(EXPECTED_DICT['key3'])

    def test_assert_example_12(self):
        """12 Тест с неблокирующими проверками."""
        with self.ASSERT('выполнение нескольких проверок'):
            with assert_soft():
                assert_that(ACTUAL_DICT['key1']).is_equal_to(EXPECTED_DICT['key1'])
            with assert_soft():
                assert_that(ACTUAL_DICT['key2']).is_equal_to(EXPECTED_DICT['key2'])
            with assert_soft():
                assert_that(ACTUAL_DICT['key3']).is_equal_to(EXPECTED_DICT['key3'])

    def test_assert_example_13(self):
        """13. Тест с неблокирующими проверками."""
        with self.ASSERT('проверка 1'):
            assert_that(ACTUAL_DICT['key1']).is_equal_to(EXPECTED_DICT['key1'])
        with self.ASSERT('проверка 2'):
            assert_that(ACTUAL_DICT['key3']).is_equal_to(EXPECTED_DICT['key3'])
        with self.ASSERT('проверка 3'):
            assert_that(ACTUAL_DICT['key2']).is_equal_to(EXPECTED_DICT['key2'])

    def test_assert_example_14(self):
        """14 Тест с неблокирующими проверками."""
        with self.ASSERT('проверка 1'):
            assert_that(ACTUAL_DICT['key1']).is_equal_to(EXPECTED_DICT['key1'])
            with assert_step('проверка 1-1'):
                assert 1
        with self.ASSERT('проверка 2'):
            assert_that(ACTUAL_DICT['key2']).is_equal_to(EXPECTED_DICT['key2'])
        with self.ASSERT('проверка 3'):
            assert_that(ACTUAL_DICT['key3']).is_equal_to(EXPECTED_DICT['key3'])

    def test_assert_example_15(self):
        """15. Тест с неблокирующими проверками примененными в метаклассе."""
        with self.ASSERT('Проверка результатов 1'):
            service_one_steps.verify_soft_service_one_step_one_is_successful()
            service_one_steps.verify_soft_service_one_step_two_is_successful()
        with self.ASSERT('Проверка результатов 2'):
            assert True

    def test_assert_example_16(self):
        """16. Тест неблокирующие проверки с разными исключениями."""
        with self.ASSERT('Проверка разных исключений'):
            with assert_step('Ошибка AssertionError'):
                raise AssertionError('Не прошла проверка!')

            with assert_step('Ошибка TimeoutError'):
                raise TimeoutError('Вышел таймаут!')

            with assert_step('Ошибка ValueError'):
                raise ValueError('Неверное значение!')

            with assert_step('Нет ошибки'):
                assert 1

        with self.ASSERT('Проверка 2'):
            pass
