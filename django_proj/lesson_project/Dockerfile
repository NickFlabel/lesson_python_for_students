# Шаг 1 - выбор образа, на основе которого будет строится контейнер
FROM python:3.13.0-slim-bookworm
ARG BUILD_VERSION=0.9
RUN echo "Version is ${BUILD_VERSION}"

# Шаг 2 - выбор рабочей директории внутри контейнера
WORKDIR /app

# Шаг 3 - копирование файлов в контейнер
COPY . ./

# Шаг 4 - установка зависимостей
RUN pip install -r requirements.txt && \
    rm -rf /root/.cache/pip

# Шаг 5 - открываем порт
EXPOSE 8000

# Переменные окружения
ENV DJANGO_SECRET_KEY=django-insecure-0b5mlk$d!+@!#3yjs6kr!s(6u!0=6#)g-*=r5!-x+_rrxh7$c)

# Volume - тома то есть директории, которые будут доступны как во время сборки так и при выполнении контейнера


# Шаг 6 - указываем команду для запуска приложения
# CMD - команда при запуске контейнера, которая может быть перезаписана в docker run
# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
# ENTRYPOINT - команда при запуске контейнера, которая не может быть перезаписана в docker run

