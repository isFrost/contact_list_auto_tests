# Contact List API Test Automation Pet Project

This repository contains a python test framework for automated testing of API of https://thinking-tester-contact-list.herokuapp.com

API documentation: https://documenter.getpostman.com/view/4012288/TzK2bEa8

The framework is built with Python, uses DOcker to manage test environment and Jenkins to build and execute test pipeline.

The purpose of the project is to improve personal test automation skills.

Auto tests are based on the manual tests listed in the following spreadsheet: [Link](https://docs.google.com/spreadsheets/d/1UmUKwhbycd5BiASBKpRuZVkyLLaz3FsHDr9khmF_iUE/edit?usp=drive_link)

## Table of Contents

- [Prerequisites](#Prerequisites)
- [Installation](#Installation)
- [Continuous Integration](#Continuous-Integration)
- [Project Structure](#Project-Structure)
- [Running Tests from command line](#Running-Tests-from-command-line)
- [Notes](#Notes)
- [Contributing](#Contributing)
- [License](#License)

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Docker Desktop

To run outside docker container:
- Python 3.x
- Pip

## Installation

1. Clone the repository:
```commandline
git clone https://github.com/isFrost/contact_list_auto_tests.git
```
2. Navigate to the project's folder:
```commandline
cd contact_list_auto_tests
```
3. Build the Docker container:
```commandline
docker build -t contact-list .
```
4. Run the container:
```commandline
docker container run -d -p 8090:8090 --name contact-list contact-list
```
5. Serve allure report from the executed tests:
```commandline
docker container exec -it contact-list allure serve allure-results --host 0.0.0.0 --port 8080
```

## Continuous Integration
This project uses Jenkins for continuous integration. The Jenkins pipeline is defined in the Jenkinsfile.

### Set up a Jenkins job and configure it to use the repository.

Jenkins installed in the system is required. Generally Jenkins can be accessed by tht following url:
```commandline
localhost/8080
```

Also Allure Plugin should be installed in Jenkins and Allure Command Line enabled.

### Install Allure Plugin (required to run reports)
1. At dashboard screen click Manage Jenkins.
2. At Manage Jenkins screen click Plugins button. 
3. At Plugins page click on Available plugins list. Use Search input to find Allure plugin.
4. Check flag against Allure plugin and click Install button.
5. Click on Installed plugins and confirm Allure plugin is in the list with Enabled flag.

### Install Allure Command Line (required to run reports)
1. Open Manage Jenkins page. 
2. Click on Tools item. 
3. At Tools screen under Allure Commandline installations click Add Allure Commandline button.
4. Populate Name field.
5. Click Apply and Save buttons.

### Create new pipeline
1. Click New Item button.
2. Populate item name.
3. Select Pipeline item and click OK 
4. At configuration screen in Pipeline section set Definition option to Pipeline script from SCM. 
5. Set SCM option to Git. 
6. Populate Repository URL filed: https://github.com/isFrost/contact_list_auto_tests.git
7. In Branch Specifier field enter */main. 
8. Click Save button. 
9. Click Build Now to build the pipeline.

## Project Structure
```commandline
├── data
│   ├── __init__.py
│   ├── new_contact_asia.json
│   ├── new_contact_canada.json
│   ├── new_contact_eu.json
│   ├── new_contact_usa.json
│   ├── new_user.json
│   ├── updated_user.json
│   └── variables.json
├── tests
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_add_contact.py
│   ├── test_add_user.py
│   ├── test_delete_contact.py
│   ├── test_delete_user.py
│   ├── test_get_contact_info.py
│   ├── test_get_user_info.py
│   ├── test_login_user.py
│   ├── test_logout_user.py
│   ├── test_update_contact_via_patch.py
│   ├── test_update_contact_via_put.py
│   └── test_update_user.py
├── utils
│   ├── __init__.py
│   └── data_helper.py
├── venv
├── Dockerfile
├── Jenkinsfile
├── README.MD
└── requirements.txt
```
## Running Tests from command line

To run the test from command line:

1) Make sure python and pip are installed in the system.
```commandline
python3 --version
```
```commandline
pip3 --version
```
2. Install dependencies from requirements.txt file. Navigate to project folder and enter command:
```commandline
pip install -r requirements.txt
```
3. create and activate virtual Python environment for your project. For example, the commands to create and activate a venv
```commandline
python -m venv .venv
```
```
source .venv/bin/activate
```
3. To run the test enter command:
```commandline
python3 -m pytest tests/ --alluredir reports
```
4. To open generate allure report enter:
```commandline
allure serve reports
```
*Note: You many need to install Allure in venv to open generated reports in browser. Below is the example how to do it:*

## Download and set up Allure command-line tool
```commandline

VERSION=2.13.9  # Replace with the latest version

wget https://github.com/allure-framework/allure2/releases/download/${VERSION}/allure-${VERSION}.tgz

tar -zxvf allure-${VERSION}.tgz -C venv/

mv venv/allure-${VERSION} venv/allure

# Add Allure to PATH
echo 'export PATH="$VIRTUAL_ENV/allure/bin:$PATH"' >> venv/bin/activate

# Reload environment
source venv/bin/activate
```
*Also note that allure will require Java Runtime to be installed in the system*
## Notes
Although Dockerfile is composed to detect CPU architecture and use proper browser it looks like webdrivers curently do not support linux/aarch64 combination. Workaround is not yet added to this project.

## Contributing

This is a test project build to improve knowledge of python automation skills. No contribution is required.

## License

This project is licensed under the [MIT License](https://mit-license.org/). See the LICENSE file for details.
