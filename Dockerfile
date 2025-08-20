# Base python image
FROM python:3.12-slim-bookworm AS base

# Install uv CLI tool if not already in image
RUN pip install uv

WORKDIR /app

# Copy only dependency specification files first
COPY pyproject.toml uv.lock /app/

# Install dependencies using uv sync, frozen to use existing uv.lock strictly
RUN uv sync --frozen --no-install-project --no-dev

# Now copy source code
COPY . /app

# Final install including the project itself
RUN uv sync --frozen --no-dev

# Start your app with uvicorn or your chosen command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
