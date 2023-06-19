FROM python:3

RUN apt-get update && apt-get install -y python3-tk

WORKDIR /app

COPY calculator.py .

CMD ["python", "calculator.py"] 
