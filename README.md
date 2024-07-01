# Flask clean architecture

This is a reusable Python Flask template. The project is based on Flask in combination with SQLAlchemy ORM.

## Getting started

### Requirements

Create a new virtual environment and activate it

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

Activate

### Running the application locally

You can then run the application with flask:

```bash
flask --app src/app run 
```

or with gunicorn:

```bash
gunicorn wsgi:app -b  0.0.0.0:7000 --workers=1 --preload
```