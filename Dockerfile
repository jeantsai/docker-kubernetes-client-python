FROM python:3-alpine

RUN pip install --no-cache-dir -U \
                kubernetes \
    && rm -rf /root/.cache

