FROM python:3.7

COPY main.py /

RUN pip install flask

CMD ["python", "main.py"]