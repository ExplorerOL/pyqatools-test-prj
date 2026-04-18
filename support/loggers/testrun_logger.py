"""Модуль логгера."""

from pathlib import Path

from pyqatools.loggers.log_levels import LogLevels
from pyqatools.loggers.logger_logging import LoggerLogging as TestrunLogger

from config.config_general import config_general


logger = TestrunLogger(log_file_path=Path(config_general.LOG_FILE_PATH_STRING), log_level=LogLevels.DEEP_TRACE)
