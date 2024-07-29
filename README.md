# Flask clean architecture

This is a reusable Python Flask template. The project is based on Flask in combination with SQLAlchemy ORM.

## Getting started

### Requirements

#### ¡IMPORTANT! Get python installed > 3.0

Install virtual environment in python system

```shell
pip install virtualenv
```

Create a new virtual environment in the project root folder and activate it

```shell
virtualenv -p python venv
.\venv\Scripts\activate
```

Update pip

```shell
python.exe -m pip install --upgrade pip
```

Install requirements.txt

```shell
pip install -r requirements.txt
```

### Considerations

Configure the development IDE to recognize the newly created virtual environment.

### Running the application locally

You can then run the application with flask:

```bash
flask --app src/app run 
```

or with gunicorn:

```bash
gunicorn wsgi:app -b  0.0.0.0:7000 --workers=1 --preload
```