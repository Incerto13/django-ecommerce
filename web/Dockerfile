FROM python:3.6

RUN mkdir -p /usr/src/app

RUN mkdir -p /static
RUN chown -R root /static

COPY ./entrypoint.sh /

WORKDIR /usr/src/app # specifying the working dir inside the container

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

# copy current dir's content to container's WORKDIR root i.e. all the contents of the web app 
COPY . .
