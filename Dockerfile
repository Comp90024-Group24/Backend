FROM python:3.11.3-alpine3.16

WORKDIR /backend

COPY . /backend

RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python3", "app.py"]