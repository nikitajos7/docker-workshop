FROM python:3.9.21

WORKDIR /wic_workshop

COPY . /wic_workshop

RUN pip install -r requirements.txt

CMD ["python", "app.py"]