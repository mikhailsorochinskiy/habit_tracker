FROM python:3.13-slim AS python-app

WORKDIR /app

RUN apt-get update \
    && apt-get install -y gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root

COPY . .

# Собираем статику на этапе build
RUN python manage.py collectstatic --noinput

FROM nginx:latest AS nginx

# Удаляем дефолтную конфигурацию
RUN rm /etc/nginx/conf.d/default.conf

# Копируем только конфиг Nginx
COPY nginx.conf /etc/nginx/nginx.conf

# Копируем статику из python-образа
COPY --from=python-app /app/staticfiles /usr/share/nginx/static

# Копируем HTML файлы
COPY html/ /usr/share/nginx/html/

EXPOSE 80