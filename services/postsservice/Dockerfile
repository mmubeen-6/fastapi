FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

RUN pip3 install --upgrade pip

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir && \
    rm requirements.txt

COPY ./app /app/