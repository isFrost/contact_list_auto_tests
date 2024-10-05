# install python
FROM python:3.12

WORKDIR ./app

# install dependancies from requirements
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Install Java (required by Allure)
RUN apt-get update && \
    apt-get install -y openjdk-17-jdk

# Install Allure
RUN curl -sL https://github.com/allure-framework/allure2/releases/download/2.21.0/allure-2.21.0.tgz | tar -xz -C /opt/ && \
    ln -s /opt/allure-2.21.0/bin/allure /usr/bin/allure

# copy the source code
COPY data ./data
COPY tests ./tests
COPY utils ./utils

# expose port
EXPOSE 8080

# run pytest, generate Allure results, and then serve the report
CMD ["sh", "-c", "python3 -m pytest --alluredir=allure-results && allure serve allure-results --host 0.0.0.0 --port 8080"]