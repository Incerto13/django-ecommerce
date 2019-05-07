FROM python:3.6

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /static
RUN chown -R root /static
ENV DJANGO_ENV production

# copy current dir's content to container's WORKDIR root i.e. all the contents of the web app
COPY . .

# inital migration, import dump, and static files
RUN chmod +x entrypoint.sh