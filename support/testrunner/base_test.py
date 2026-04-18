from pyqatools.assertions.assert_step import assert_step
from pyqatools.testrunner.pytest.base_test_template import BaseTestTemplate
from pytest_assert_that import assert_that

from support.test_context.test_context import TestContext


class BaseTest(BaseTestTemplate):
    context = TestContext()
    assert_step = assert_step
    assert_that = assert_that
