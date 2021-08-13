FROM python:3.9-buster

WORKDIR /app

RUN pip install pipenv

COPY Pipfile.lock .
COPY Pipfile .

RUN pipenv install

COPY . ./

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host=0.0.0.0"]