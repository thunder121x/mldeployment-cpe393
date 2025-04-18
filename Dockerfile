FROM python:3.9-slim

WORKDIR /app

COPY app/ app/
COPY train.py .
COPY Housing.csv .

RUN pip install --no-cache-dir -r app/requirements.txt
RUN python train.py

EXPOSE 9000

CMD ["python", "app/main.py"]
