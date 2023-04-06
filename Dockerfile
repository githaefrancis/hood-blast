FROM python:3.10-alpine3.16

WORKDIR /usr/src/hood_blast

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN python -m pip install --upgrade pip
RUN pip install pipenv
COPY ./Pipfile .
COPY ./Pipfile.lock .
RUN pipenv install --dev --system --deploy

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/hood_blast/entrypoint.sh
RUN ["chmod", "+x", "/usr/src/hood_blast/entrypoint.sh"]

COPY . .

ENTRYPOINT ["sh","/usr/src/hood_blast/entrypoint.sh"]