FROM python:3.9.10-slim-buster
RUN apt-get update && apt-get install python-tk python3-tk tk-dev -y
RUN pip install --upgrade pip setuptools
COPY ./requirements.txt /usr/local/src/myscripts/requirements.txt
WORKDIR /usr/local/src/myscripts
RUN pip install setuptools_rust
RUN pip install rust
RUN pip install -r requirements.txt
COPY . /usr/local/src/myscripts
EXPOSE 8501
CMD ["streamlit", "run", "Home.py", "--server.port", "80", "--server.enableXsrfProtection", "false"]

# FROM python:3.9.10-slim-buster
# EXPOSE 8501
# CMD mkdir -p /app
# WORKDIR /app
# COPY requirements.txt ./requirements.txt
# RUN pip3 install -r requirements.txt
# COPY . .
# ENTRYPOINT [ "streamlit","run" ]
# CMD [ "Home.py" ]