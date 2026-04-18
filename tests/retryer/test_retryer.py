import datetime

from services.service_one.steps.service_one_steps import service_one_steps
from support.retryers.testrun_retryer import RetryConfigs, Retryer
from support.testrunner.base_test import BaseTest


class TestRetryer(BaseTest):
    def test_retry_using_decorator_example(self):
        """1. Повтор метода с помощью декоратора."""
        with self.ACT('выполнение действий'):
            service_one_steps.service_one_step_three_with_exception()

    def test_retry_using_decorator_and_settings_change_example(self):
        """1. Повтор метода с помощью декоратора и переопределения настроек повтора при вызове."""
        with self.ACT('выполнение действий'):
            with Retryer.with_config(config=RetryConfigs.T2000_I500.value):
                service_one_steps.service_one_step_three_with_exception()

    def test_retry_using_code_block_retry_example(self):
        """1. Повтор блока кода."""
        with self.ARRANGE('Подготовка данных'):
            model1 = ['1']
            start_ts = datetime.datetime.now()
            target_dt = datetime.timedelta(seconds=3)
            result = None

        with self.ACT('Несколько попыток действия'):
            for attempt in Retryer(config=RetryConfigs.T5000_I2000.value):
                with attempt:
                    service_one_steps.service_one_step_one(model=model1)
                    result = service_one_steps.confirm_action(
                        start_ts=start_ts,
                        target_dt=target_dt,
                    )

        with self.ACT('Проверка результов'):
            assert result is True

    def test_wait_using_retrying_from_metaclass(self):
        """Ожидание с помощью метакласса."""
        with self.ARRANGE('Подготовка данных'):
            start_ts = datetime.datetime.now()
            target_dt = datetime.timedelta(seconds=3)
        with self.ACT('Ожидание события'):
            service_one_steps.wait_auto_for_service_one_step_four(
                start_ts=start_ts,
                target_dt=target_dt,
            )
        with self.ACT('Проверка результов'):
            ...

    def test_steps_with_retrying_using_metaclass(self):
        """Повтор с помощью метакласса."""
        with self.ARRANGE('Подготовка данных'):
            start_ts = datetime.datetime.now()
            target_dt = datetime.timedelta(seconds=2)
        with self.ACT('Ожидание события'):
            result = service_one_steps.get_data_with_auto_retry(
                start_ts=start_ts,
                target_dt=target_dt,
            )
        with self.ASSERT('Проверка результов'):
            self.assert_that(result).is_not_none()
