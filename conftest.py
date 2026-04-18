from pyqatools.config.config_pyqatools import config_pyqatools

from pyqatools.testrunner.pytest.pytest_hooks import (  # noqa F401
    pytest_configure,
    pytest_exception_interact,
    pytest_fixture_setup,
    pytest_runtest_logfinish,
    pytest_runtest_logreport,
    pytest_runtest_logstart,
    pytest_runtest_teardown,
)

from support.assertions.assert_soft import assert_soft
from support.loggers.testrun_logger import logger
from support.reporters.testrun_reporter import reporter
from support.retryers.testrun_retryer import Retryer


config_pyqatools.logger = logger
config_pyqatools.reporter = reporter
reporter.report_methods = True
config_pyqatools.assert_soft = assert_soft
config_pyqatools.retryer = Retryer


pytest_plugins = 'fixtures.fixtures_examples'
