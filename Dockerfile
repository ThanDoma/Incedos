FROM python:3.10-alpine

WORKDIR /app
COPY requirements.txt requirements.txt
RUN /usr/local/bin/python -m pip install --upgrade pip
#Изменим строчку ниже, добавив --no-cache-dir
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . . 
# перенес копи был перед WORKDIR /app
ENV FLASK_APP=app
ENV FLASK_DEBUG=1
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]