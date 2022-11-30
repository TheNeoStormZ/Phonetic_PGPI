from python:3.8-alpine

RUN apk add --no-cache git gcc libc-dev
RUN apk add --no-cache gcc g++ make libffi-dev python3-dev build-base

RUN pip install gunicorn
RUN pip install ipdb
RUN pip install ipython

WORKDIR /app

RUN git clone https://github.com/TheNeoStormZ/Phonetic_PGPI.git .
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
