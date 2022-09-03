FROM python:3.10.1-buster
MAINTAINER Lukasz Admin

EXPOSE 80
EXPOSE 8000
EXPOSE 8080
EXPOSE 8002

ENV PYTHONUNBUFFERED 1
ENV LISTEN_PORT=8000
ENV PATH="/scripts:${PATH}"

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get install gcc
RUN apt-get update
RUN apt-get install -y texlive
RUN apt-get install -y latexmk
RUN apt-get install -y texlive-latex-extra
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql17
RUN ACCEPT_EULA=Y apt-get install -y mssql-tools
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
RUN apt-get install -y g++ unixodbc-dev
RUN pip install pyodbc
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
RUN useradd -ms /bin/bash admin
RUN mkdir /app

COPY ./app/ /app
WORKDIR /app
RUN chown -R admin:admin /app
RUN chmod 755 /app
USER admin

EXPOSE 80

CMD ["gunicorn", "portal.wsgi", "--bind=0.0.0.0:80"]
