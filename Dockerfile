# install python
FROM python:3.12

WORKDIR ./app

# install dependencies from requirements
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

# expose port (no longer needed for Allure serve)
EXPOSE 8090

# run pytest and generate Allure results
CMD ["sh", "-c", "python3 -m pytest --alluredir=allure-results"]