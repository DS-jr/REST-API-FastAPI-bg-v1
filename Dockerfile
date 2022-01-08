FROM python:3.9 

COPY . /app5 
COPY requirements.txt /app5

WORKDIR /app5 

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app5", "--host=0.0.0.0", "--reload"]
