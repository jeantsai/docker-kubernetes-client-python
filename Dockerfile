FROM python:3-alpine

RUN pip install --no-cache-dir -U \
                kubernetes==17.14.0a1
COPY list_pods.py .
CMD ["python", "list_pods.py"]
