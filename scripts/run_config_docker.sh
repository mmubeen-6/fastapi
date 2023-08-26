#!/bin/bash

docker run -it --network fastapi_default \
    --env-file .env -p 8000:8000 \
    -v /Users/mubeen/Workspace/fastapi/services/postsservice/app:/app \
    postsservice:latest uvicorn main:app --host 0.0.0.0 --reload;