# use a lightweight python image
FROM python:3.12-slim

# install uv package manager
RUN pip install --no-cache-dir uv

# set working directory inside container
WORKDIR /app

# copy dependency files first for caching
COPY pyproject.toml uv.lock ./

# install dependencies exactly as locked
RUN uv sync --frozen --no-dev

# copy the application code
COPY app.py ./

# expose fastapi port
EXPOSE 8000

# start fastapi app with uvicorn
CMD ["uv", "run", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
