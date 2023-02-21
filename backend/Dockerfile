FROM python:3.9

WORKDIR /index

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "index.py"]
