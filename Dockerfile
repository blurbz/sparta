FROM python:3.9.1
ADD . /python-flask
WORKDIR /python-flask
RUN pip install -r requirements.txt
RUN python -m flask db init
RUN python -m flask db migrate -m 'Initial'
RUN python -m flask db upgrade
ENTRYPOINT ["python"]
CMD ["-m", "flask", "run", "--host", "0.0.0.0"]