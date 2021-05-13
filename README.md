# dw-backend

## Environment

Install dependencies

```
pip3 install -r requirements.txt
```

Environment variable

On Linux

```
export DJANGO_CONFIG_SECRETKEY="ihateyou"
```

On Windows

Go to Search -> type "env" -> Edit the system environment variables -> Environment Variables... -> New... -> Add the variable above.

## Run

```
python manage.py runserver
```

## Usage

- Swagger UI at `http://localhost:8000/swagger/`
- Redoc UI at `http://localhost:8000/redoc/`