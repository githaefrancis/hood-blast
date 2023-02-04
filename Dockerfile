FROM python:3.9-alpine3.15

WORKDIR /usr/src/hood_blast

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
RUN pip install pipenv
COPY ./Pipfile .
COPY ./Pipfile.lock .
RUN pipenv install --system --deploy --ignore-pipfile

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/hood_blast/entrypoint.sh
RUN ["chmod", "+x", "/usr/src/hood_blast/entrypoint.sh"]

COPY . .

ENTRYPOINT ["sh","/usr/src/hood_blast/entrypoint.sh"]