from support.loggers.testrun_logger import logger
from support.reporters.testrun_reporter import reporter


def _mark_test_section(section_info: str):
    logger.info(section_info)
    return reporter.step(section_info)


def ARRANGE(msg: str = ''):  # noqa N802
    """Подготовка данных."""
    return _mark_test_section(f'ARRANGE: {msg}')


def ACT(msg: str = ''):  # noqa N802
    """Выполниение действия."""
    return _mark_test_section(f'ACT: {msg}')


def ASSERT(msg: str = ''):  # noqa N802
    """Проверка."""
    return _mark_test_section(f'ASSERT: {msg}')
