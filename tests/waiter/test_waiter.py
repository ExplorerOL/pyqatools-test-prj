import datetime
import time

from services.service_one.steps.service_one_steps import service_one_steps
from support.waiters.testrun_waiter import TimeWaiter


class TestWaiter:
    def test_waiter_example_1(self):
        """Тест с ожиданием из модуля time."""
        model1 = ['call_from_test']
        model2 = {'call_from_test2': str(datetime.datetime.now())}

        service_one_steps.service_one_step_one(model1)
        time.sleep(3)
        result_step2 = service_one_steps.service_one_step_two(model=model2)

        assert isinstance(result_step2, dict)
        assert result_step2.get('grpc_call_two_finished', None) is not None

    def test_waiter_example_2(self):
        """Тест с кастомным ожиданием."""
        model1 = ['call_from_test']
        model2 = {'call_from_test2': str(datetime.datetime.now())}

        service_one_steps.service_one_step_one(model1)
        TimeWaiter.wait(timeout_ms=3000, msg='Ожидание окончания блокировки пользователя')
        result_step2 = service_one_steps.service_one_step_two(model=model2)

        assert isinstance(result_step2, dict)
        assert result_step2.get('grpc_call_two_finished', None) is not None
