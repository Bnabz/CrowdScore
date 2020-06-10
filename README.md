![license](https://img.shields.io/github/license/mashape/apistatus.svg)


# CrowdScore
#### Version 1.0, 9/6/2020
#### By Brian Nabiswa

## Description
CrowdScore is a website that provides a platform for users to post their websites, and have them reviewed by registered users on defined criteria
## Features
* Users can create their profiles.
* Users can view other user's profiles..
* Users can post thier projects
* Users can score projects, and view a project's score.
* Users can search for a particular project.

## Prerequisite

- [Python3.6](https://www.python.org/downloads/release/python-365/)
- [Virtual Environment](https://virtualenv.pypa.io/en/stable/installation/)

## Technologies & Languages
* Django3.0.6
* Python 3.8
* Bootstrap
* Postgresql
* Heroku
**Version control (Git)** [https://git-scm.com/](url)

# Installation and Setup

Clone the repository below

```
git clone https://github.com/Bnabz/CrowdScore.git
```

### Create and activate a virtual environment

    virtualenv venv --python=python3.6

    source venv/bin/activate

### Install required Dependencies

    pip install -r requirements.txt

### Copy environment variable

    cp env.sample .env

### Load/refresh .environment variables

    source .env

## Running the application

```
python manage.py server
```


## Endpoints Available
 
| Method | Endpoint                        | Description                           | Roles         |
| ------ | ------------------------------- | ------------------------------------- | ------------  |
| GET    |        /api/profiles            | view all profiles                     | users         |
| GET    |        /api/projects            | view all projects                     | users         |



## License

MIT