FROM python:3.11

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8000

CMD python db_creation.py && python -m uvicorn main:app --host 0.0.0.0