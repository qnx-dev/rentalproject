### Steps to run:

Create env"
```py -m venv env```

Activate env:
```source env/Scripts/activate```

Install dependencies:
```pip install -r requirements.txt```

Make migrations:
```python manage.py makemigrations```

Migrate:
```python manage.py migrate --run-syncdb && python manage.py migrate```

Run Server:
```python manage.py runserver```

cURL Request:
```
curl --request GET \
  --url http://localhost:8000/reservations/
```



