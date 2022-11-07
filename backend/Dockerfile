FROM python

ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/

COPY . /usr/src/

RUN pip install -r /usr/src/restapi/requirements.txt


EXPOSE 8000

# CMD ["python","manage.py","runserver","0.0.0.0:8000"]