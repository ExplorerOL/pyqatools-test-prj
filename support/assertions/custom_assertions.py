from typing import Any

from pyqatools.assertions.assert_step import assert_step
from pytest_assert_that import assert_that


class CustomAssertions:
    @staticmethod
    def verify_equal(actual_val: Any, expected_val: Any) -> None:
        """Пользовательская проверка."""
        assert actual_val == expected_val, 'Данные разные!'

    @staticmethod
    def verify_equal_pytest_assert_that(actual_val: Any, expected_val: Any) -> None:
        """Пользовательская проверка с использованием pytest_assert_that."""
        assert_that(actual_val).is_equal_to(expected_val)

    @staticmethod
    def verify_equal_pytest_assert_that_with_soft_assertions(actual_val: Any, expected_val: Any) -> None:
        """Пользовательская проверка с использованием pytest_assert_that и soft assertions."""
        with assert_step('check1'):
            assert_that(actual_val).is_equal_to(expected_val)

        with assert_step('check2'):
            assert_that(actual_val).is_equal_to(10)

        with assert_step('check3'):
            assert_that(actual_val).is_equal_to(actual_val)
