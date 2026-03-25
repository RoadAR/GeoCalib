FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    TORCH_HOME=/root/.cache/torch \
    GRADIO_SERVER_NAME=0.0.0.0 \
    GRADIO_SERVER_PORT=7860

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./

RUN python -m pip install --upgrade pip && \
    python -m pip install --index-url https://download.pytorch.org/whl/cpu torch torchvision && \
    grep -vE '^(torch|torchvision)$' requirements.txt > /tmp/requirements-docker.txt && \
    python -m pip install -r /tmp/requirements-docker.txt && \
    python -m pip install gradio spaces

COPY . .

RUN python -m pip install -e .

EXPOSE 7860

CMD ["python", "gradio_app.py"]
