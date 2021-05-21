FROM python:3.8
COPY ./ /
RUN pip install -r /requirements.txt
WORKDIR /infra_project/
CMD python manage.py runserver 0:5000