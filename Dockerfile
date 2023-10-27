FROM python:3.11.0

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements_dev.txt

EXPOSE 9080

CMD ["uvicorn", "main:api", "--host", "0.0.0.0", "--port", "9080"]