import datetime

from pyqatools.reporters.reporter_base_classes import ClassWithMethodLoggingAndReporting


class ServiceOneGrpcClient(ClassWithMethodLoggingAndReporting):
    def grpc_call_one(self, request: list[str]) -> list[str]:
        """Докстрока вызова grpc 1."""
        request.append('grpc_call_one_started')
        request.append('grpc_call_one_finished')
        return request

    def grpc_call_two(self, request: dict) -> dict:
        """Докстрока вызова grpc 2."""
        request.update({'grpc_call_two_started': str(datetime.datetime.now())})
        request.update({'grpc_call_two_finished': str(datetime.datetime.now())})
        return request


service_one_grpc_client = ServiceOneGrpcClient()
