import datetime

import allure
import pytest

from services.service_one.steps.service_one_steps import service_one_steps
from support.testrunner.base_test import BaseTest


# @allure.suite('Reporting')
# @allure.feature('Reporting examples')
class TestReporting(BaseTest):
    # @pytest.mark.skip(reason='no')
    def test_reporting_example_1(
        self,
        fixture_scope_function,
        fixture_generator_scope_session,
    ):
        """1. Тест с фикстурами в отчете."""
        model1 = ['call_from_test']
        model2 = {'call_from_test2': str(datetime.datetime.now())}

        service_one_steps.service_one_step_one(model1)
        result_step2 = service_one_steps.service_one_step_two(model=model2)

        assert isinstance(result_step2, dict)
        assert result_step2.get('grpc_call_two_finished', None) is not None

    def test_reporting_example_2(self) -> None:
        """2. Тест с кастомными шагами в отчете."""
        service_one_steps.service_one_step_one(model=['call_from_test'])
        service_one_steps.service_one_step_two(model={'call_from_test': str(datetime.datetime.now())})

    def test_reporting_example_3_failed(self):
        """3. Тест с кастомными шагами в отчете с ошибкой."""
        service_one_steps.service_one_step_one(model=['call_from_test'])
        service_one_steps.service_one_step_two(model={'call_from_test': str(datetime.datetime.now())})
        with allure.step('ошибка'):
            raise AssertionError()

    @pytest.mark.parametrize('param', [1, 2, 3])
    def test_reporting_example_4_with_params(self, param: int):
        """4. Тест с кастомными шагами в отчете с параметрами."""
        service_one_steps.service_one_step_one(model=[f'call_from_test param={param}'])
        service_one_steps.service_one_step_two(model={'call_from_test': str(datetime.datetime.now())})

    @allure.story('Positive')
    @allure.title('Тест с декораторами Allure')
    @allure.description('Применение декораторв Allure для теста и отображение в отчете')
    def test_reporting_example_5_manual_labels(self):
        """5. Тест с ручным проставлением меток."""
        service_one_steps.service_one_step_one(model=['call_from_test'])
        service_one_steps.service_one_step_two(model={'call_from_test': str(datetime.datetime.now())})

    @allure.story('Negative')
    @allure.title('Тест с декораторами Allure (негативный)')
    @allure.description('Применение декораторв Allure для теста (негативный тест)')
    def test_try_reporting_example_6_manual_labels(self):
        """6. Тест с ручным проставлением меток негативный."""
        service_one_steps.service_one_step_one(model=['call_from_test'])
        service_one_steps.service_one_step_two(model={'call_from_test': str(datetime.datetime.now())})

    # @pytest.mark.skip(reason='no')
    def test_reporting_example_6_auto_labels(self):
        """6. Тест с декораторами Allure.

        Применение декораторв Allure для теста и отображение в отчете
        """
        service_one_steps.service_one_step_one(model=['call_from_test'])
        service_one_steps.service_one_step_two(model={'call_from_test': str(datetime.datetime.now())})

    def test_try_reporting_example_7_auto_labels(self):
        """7. Тест с декораторами Allure (негативный).

        Применение декораторв Allure для теста и отображение в отчете (негативный тест)
        """
        service_one_steps.service_one_step_one(model=['call_from_test'])
        service_one_steps.service_one_step_two(model={'call_from_test': str(datetime.datetime.now())})

    @pytest.mark.parametrize('param2', (4, 5, 6))
    @pytest.mark.parametrize('param1', (1, 2, 3))
    def test_reporting_example_8_auto_labels_with_patams(self, param1, param2):
        """8. Тест с декораторами Allure и параметрами.

        Применение декораторв Allure для теста и отображение в отчете
        """
        service_one_steps.service_one_step_one(model=['call_from_test'])
        service_one_steps.service_one_step_two(model={'call_from_test': str(datetime.datetime.now())})

    def test_reporting_example_9_with_params_in_step_in_test(self):
        """9. Тест с параметрами шага внутри теста."""
        with self.context.reporter.step('Шаг с кастомными параметрами', params={'values': 123}):
            self.context.logger.info('Hello!')
            assert 1
