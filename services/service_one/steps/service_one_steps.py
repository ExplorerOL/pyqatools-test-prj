import datetime

from pyqatools.exceptions.general_exceptions import UnexpectedValueError
from pyqatools.testrunner.pytest.steps_base import StepsBase
from pytest_assert_that import assert_that

from services.service_one.client.grpc.service_one_grpc_client import service_one_grpc_client
from support.retryers.testrun_retryer import RetryConfigs, Retryer


class ServiceOneSteps(StepsBase):
    def service_one_step_one(self, model: list[str]) -> list[str]:
        """Докстрока шага 1."""
        model.append('service_one_step_started')
        request = model
        response = service_one_grpc_client.grpc_call_one(request=request)
        response.append('service_one_step_finished')
        return response

    def service_one_step_two(self, model: dict) -> dict:
        """Докстрока шага 2."""
        model.update({'service_one_step_two_started': str(datetime.datetime.now())})
        request = model
        response = service_one_grpc_client.grpc_call_two(request=request)
        response.update({'service_one_step_two_finished': str(datetime.datetime.now())})
        return response

    def verify_soft_service_one_step_one_is_successful(self) -> None:
        """Проверка успешности шага 1."""
        result = self.service_one_step_one(model=['service_one_step_one'])
        assert_that(result).contains(('Hi'))

    def verify_soft_service_one_step_two_is_successful(self) -> None:
        """Проверка успешности шага 2."""
        result = self.service_one_step_two(model={'key1': 'value1'})
        assert_that(result).contains_key('key1')

    @Retryer.retry(config=RetryConfigs.T1000_I100.value)
    def service_one_step_three_with_exception(self) -> None:
        """Метод повторами при возможных ошибках."""
        # действия и проверка условий
        raise TimeoutError('Превышено время!')

    def confirm_action(self, start_ts: datetime.datetime, target_dt: datetime.timedelta) -> bool:
        """Подтвердение выполнения."""
        dt = datetime.datetime.now() - start_ts
        if dt < target_dt:
            raise ValueError('Значение не получено!')
        return True

    def get_data_with_auto_retry(self, start_ts: datetime.datetime, target_dt: datetime.timedelta) -> str:
        """Получение данных с авто повторами."""
        dt = datetime.datetime.now() - start_ts
        if dt < target_dt:
            raise UnexpectedValueError('Данные не получены!')
        return 'success'

    def wait_auto_for_service_one_step_four(self, start_ts: datetime.datetime, target_dt: datetime.timedelta) -> None:
        """Шаг с автоматическими повторами выполнения."""
        dt = datetime.datetime.now() - start_ts
        self.service_one_step_one(model=['service_one_step_one'])
        if dt < target_dt:
            raise TimeoutError('Время вышло!')

    def wait_auto_for_service_one_step_one_is_successful(self) -> None:
        """Шаг с автоматическими повторами выполнения при неуспехе."""
        result = self.service_one_step_one(model=['service_one_step_one'])
        if 'Hi' in result:
            raise ValueError('Шаг 1 не выполнен!')


service_one_steps = ServiceOneSteps()
