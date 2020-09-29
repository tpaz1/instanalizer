FROM python:3.6.9-slim-buster
WORKDIR /usr/src/app
COPY ./ .
RUN pip install -r requirements.txt
CMD [ "python3" , "app.py" ]
