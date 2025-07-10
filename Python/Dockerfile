# Stage 1 - Build the application

FROM python:3.12-slim AS builder  

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install --prefix=/install -r requirements.txt


# Stage 2 - Create the final image

FROM python:3.12-slim

WORKDIR /app

COPY --from=builder /install /usr/local

COPY app.py .

EXPOSE 5000

ENTRYPOINT [ "python","app.py" ]