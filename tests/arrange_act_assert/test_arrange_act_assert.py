import datetime

from services.service_one.steps.service_one_steps import service_one_steps
from support.reporters.testrun_reporter import reporter
from support.test_sections.test_sections import ACT, ARRANGE, ASSERT
from support.testrunner.base_test import BaseTest


class TestArrangeActAssert(BaseTest):
    def test_arrange_act_assert_example_1(self):
        """Arrange Act Assert в виде комментариев."""
        # arrange
        model1 = ['call_from_test']
        model2 = {'call_from_test2': str(datetime.datetime.now())}
        # act
        service_one_steps.service_one_step_one(model1)
        result_step2 = service_one_steps.service_one_step_two(model=model2)
        # assert
        assert isinstance(result_step2, dict)
        assert result_step2.get('grpc_call_two_finished', None) is not None

    def test_arrange_act_assert_example_2(self):
        """Arrange Act Assert в виде явного вызова шагов."""
        with reporter.step('ARRANGE: подготовка тестовых данных'):
            model1 = ['call_from_test']
            model2 = {'call_from_test2': str(datetime.datetime.now())}
        with reporter.step('ACT: выполнение действий'):
            service_one_steps.service_one_step_one(model1)
            result_step2 = service_one_steps.service_one_step_two(model=model2)
        with reporter.step('ASSERT: проверка результатов'):
            assert isinstance(result_step2, dict)
            assert result_step2.get('grpc_call_two_finished', None) is not None

    def test_arrange_act_assert_example_3(self):
        """Arrange Act Assert в виде шаблона разметки."""
        with ARRANGE('подготовка тестовых данных'):
            model1 = ['call_from_test']
            model2 = {'call_from_test2': str(datetime.datetime.now())}
        with ACT('выполнение действий'):
            service_one_steps.service_one_step_one(model1)
            result_step2 = service_one_steps.service_one_step_two(model=model2)
        with ASSERT('проверка результатов'):
            assert isinstance(result_step2, dict)
            assert result_step2.get('grpc_call_two_finished', None) is not None

    def test_arrange_act_assert_example_4(self):
        """Arrange Act Assert в виде шаблона разметки из базового класса."""
        with self.ARRANGE('подготовка тестовых данных'):
            model1 = ['call_from_test']
            model2 = {'call_from_test2': str(datetime.datetime.now())}
        with self.ACT('выполнение действий'):
            service_one_steps.service_one_step_one(model1)
            result_step2 = service_one_steps.service_one_step_two(model=model2)
        with self.ASSERT('проверка типа'):
            assert isinstance(result_step2, dict)
        with self.ASSERT('проверка атрибута'):
            assert result_step2.get('grpc_call_two_finished', None) is not None
