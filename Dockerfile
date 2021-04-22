FROM python:3-alpine

RUN pip install --no-cache-dir -U \
                kubernetes==12.0.1 \
    && rm -rf /root/.cache

