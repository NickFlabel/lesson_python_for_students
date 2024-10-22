import time

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        # До обработки запроса
        start_time = time.time()
        method = request.method
        path = request.path
        self.__some_work()

        # Передаем объект запроса дальше по цепочке декораторов
        response = self.get_response(request, *args, **kwargs)

        duration = time.time() - start_time
        print(f"request with {method} {path} был завершен за {duration:.2f} секунд")

        return response

    def __some_work(self):
        pass
