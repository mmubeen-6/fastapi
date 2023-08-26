# FastAPI Learning

## Setup

Following packages is required to run this project: -

- Docker [Ubuntu Setup](https://docs.docker.com/get-docker/) [Mac OS Setup](https://docs.docker.com/desktop/install/mac-install/)
- Docker Compose [Setup](https://docs.docker.com/compose/install/)

To setup the project, you need to create postgres volume: -

```bash
docker volume create --name=postgress_data
docker-compose pull
docker-compose up -d
```

To generate a authorization token, you need to run the following command: -

```bash
openssl rand -hex 32
```

## Environment Variables

| Variable Name         | Allowed Value Type | Default Value | Explained                                    |
| --------------------- | ------------------ | ------------- | -------------------------------------------- |
| POSTGRES_HOSTNAME     | str                | postgres      | postgresql service hostname                  |
| POSTSSERVICE_HOSTNAME | str                | config        | posts service hostname                       |
| POSTGRES_USER         | str                | fastapi       | postgresql database user                     |
| POSTGRES_PASSWORD     | str                | fastapi       | postgresql database password                 |
| POSTGRES_PORT         | int                | 5432          | postgresql database port                     |
| POSTGRES_DB           | str                | fastapi       | postgresql database name                     |
| POSTSSERVICE_PORT     | int                | 8000          | posts service port                           |
| SECRET_KEY            | str                | ""            | secret key to be used for jwt authentication |

- .env file example

```bash
# hostnames
POSTGRES_HOSTNAME=postgres
POSTSSERVICE_HOSTNAME=postsservice

# postgres
POSTGRES_USER=fastapi
POSTGRES_PASSWORD=fastapi
POSTGRES_PORT=5432
POSTGRES_DB=fastapi

# backend
POSTSSERVICE_PORT=8000
SECRET_KEY=
```
