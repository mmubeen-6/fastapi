#!/bin/bash

docker run -it --network fastapi_default \
    --env-file .env -p 8000:8000 \
    -v /Users/mubeen/Workspace/fastapi/services/config/app:/app \
    config:latest bash;