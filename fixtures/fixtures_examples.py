from typing import Generator

import pytest
from pyqatools.generators.strings_generator import StringsGenerator


@pytest.fixture()
def fixture_random_string() -> 'str':
    """Фикстура возвращает случайную строку."""
    return StringsGenerator.generate_random_string()


@pytest.fixture()
def fixture_scope_function(fixture_random_string: str) -> str:
    """Фикстура добавляет к аргументу свое имя."""
    return f'{fixture_random_string} fixture_scope_functiontion'


@pytest.fixture()
def fixture_generator_scope_function(fixture_random_string: str) -> Generator[str, None, None]:
    """Фикстура-генератор добавляет к аргументу свое имя."""
    yield f'{fixture_random_string} fixture_generator_scope_function setup'

    f'{fixture_random_string} fixture_generator_scope_function teardown'


@pytest.fixture(scope='session')
def fixture_generator_scope_session() -> Generator[str, None, None]:
    """Фикстура-генератор добавляет к аргументу свое имя."""
    yield 'fixture_generator_scope_session setup'

    'fixture_generator_scope_session teardown'
