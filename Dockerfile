FROM python:3.9-slim-buster

# set a directory for the app
WORKDIR /usr/src/app

# copy all the files to the container
COPY . .

# install dependencies
RUN pip install --no-cache-dir -r ./requirements.txt

ENV FLASK_APP= ./main.py
ENV FLASK_ENV=development

# tell the port number the container should expose
EXPOSE 5000

CMD [ "python3", "./application.py" , "-h", "0.0.0.0"]