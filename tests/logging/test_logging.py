import datetime

import pytest

from services.service_one.steps.service_one_steps import service_one_steps
from support.testrunner.base_test import BaseTest


class TestLogging(BaseTest):
    # @pytest.mark.skip(reason='no')
    def test_logging_example_1(
        self,
        fixture_scope_function,
        fixture_generator_scope_session,
        fixture_generator_scope_function,
    ):
        """1. Тест с логированием шагов и фикстурами."""
        model1 = ['call_from_test']
        model2 = {'call_from_test2': str(datetime.datetime.now())}

        service_one_steps.service_one_step_one(model1)
        result_step2 = service_one_steps.service_one_step_two(model=model2)

        assert isinstance(result_step2, dict)
        assert result_step2.get('grpc_call_two_finished', None) is not None

    def test_logging_example_2(self):
        """2. Тест с логированием шагов."""
        service_one_steps.service_one_step_one(model=['call_from_test'])
        service_one_steps.service_one_step_two(model={'call_from_test': str(datetime.datetime.now())})

    def test_logging_example_3(self):
        """3. Тест с логированием шагов и шагом отчета."""
        service_one_steps.service_one_step_one(model=['call_from_test'])
        service_one_steps.service_one_step_two(model={'call_from_test': str(datetime.datetime.now())})
        with self.context.reporter.step('ошибка'):
            raise AssertionError()

    @pytest.mark.parametrize('param', [1, 2, 3])
    def test_logging_example_4_with_params(self, param: int):
        """4. Тест с логированием шагов и параметрами."""
        service_one_steps.service_one_step_one(model=[f'call_from_test param={param}'])
        service_one_steps.service_one_step_two(model={'call_from_test': str(datetime.datetime.now())})
