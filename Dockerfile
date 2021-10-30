FROM python:3.9.1
ADD . /python-flask
WORKDIR /python-flask
RUN pip install -r requirements.txt
RUN flask db init
RUN flask db migrate -m 'Initial'
RUN flask db upgrade
ENTRYPOINT ["python"]
CMD ["-m", "flask", "run", "--host", "0.0.0.0"]