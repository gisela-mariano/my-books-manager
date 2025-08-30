# Build
FROM python:3.9 as builder

WORKDIR /install

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .

RUN pip wheel --no-cache-dir --wheel-dir=/install/wheels -r requirements.txt


# Final
FROM python:3.9-slim

# Define um arg (parametro) que, nesse caso, o docker-compose irá passar
ARG APP_PORT

# Transfere o valor do ARG para uma variável de ambiente para que o CMD possa utilizá-la em tempo de execução
ENV APP_PORT=${APP_PORT}

WORKDIR /app

COPY --from=builder /install /usr/local

COPY . .

EXPOSE ${APP_PORT}

CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "${APP_PORT}"]