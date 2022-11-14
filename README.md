# Django SMS - Africas Talking

> Send SMS Programmatically using Africas Talking Python SDK

1. [Requirements](#requirements)
2. [Setup](#setup)
3. [Documentation](#documentation)
4. [Usage](#usage)
5. [Development](#development)

## Requirements

1. Python 3.9+ installed
2. Text editor such as [vs code](https://code.visualstudio.com/) or sublime text
3. Git - preferrably use terminal like [gitbash](https://gitforwindows.org/)

## Setup

1. Clone the repository.
2. Change directory to the location of this repository.
3. Create a `.env` file using the included `.env.example` as an example.
4. Generate a secret key for your app and paste into the SECRET_KEY section of .env file
you can find generate the key from [here](https://djecrety.ir/)
5. Create and start your preferred Python virtual environment. For
more information on how to set up a virtual environment, check the instructions on [this link](https://tutorial.djangogirls.org/en/django_installation/). Install the required libraries by running the commands below, by changing to
the project directory.

        poetry install

6. After installation, run the following command:

       poetry run python manage.py migrate

7. A local ```dbsqlite``` file will be generate at the root of the project.
8. Create a superuser by running the ``python manage.py createsuperuser`` and fill in the details.
9. After creating superuser run ``python manage.py runserver`` open the browser and run  ``127.0.0.1:8000/admin`` , login with the credentials created.
10. For details of how to get started with django, check out [this link](https://www.djangoproject.com/start/)
11. In order to work with a virtual environment, check out [this link](https://tutorial.djangogirls.org/en/installation/#pythonanywhere)

## Documentation

Visit the base url and go to the docs url

    <domain>/docs/

For more detailed documentation, navigate to the `core/apiv1/README.md` file.

## Usage

To run locally:

    python manage.py runserver

## Development

Pull the latest main version:

    git pull origin main

Create local development branch and switch to it:

    git branch {feature_branch_name}
    git checkout {feature_branch_name}

Make desired changes then commit the branch.

    git add .
    git commit -m "changes to{feature_branch_name}"
    git push origin {feature_branch_name}
