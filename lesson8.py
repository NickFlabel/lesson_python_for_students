# Принцип 4: открытости-закрытости (Open/Close Principle)
# Классы должны быть открыты для расширения, но закрыты для модификации


request = {"method": "GET"}


class AuthenticationMiddleware:

    def __init__(self, next):
        self.next = next

    def __call__(self, request):
        # каким-то образом проверяет пользователя
        user = {"name": "user"}
        request['user'] = user
        if user:
            return self.next(request)
        else:
            raise Exception


def request_handler(request):
    print(request)
    return {"answer": f"Your {request['method']} request has been handled!"}


middleware = AuthenticationMiddleware(request_handler)
next_middleware = AuthenticationMiddleware(middleware)
next_next_middleware = AuthenticationMiddleware(next_middleware)
# print(next_next_middleware(request))




