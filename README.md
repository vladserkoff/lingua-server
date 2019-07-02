# Lingua

Web app that identifies the language of the text.

## Installation

You need docker and docker-compose installed.

```bash
docker-compose build
docker-compose up
```

## Usage

```python
In [1]: import requests

In [2]: r = requests.get('http://localhost:8000/identify-language', data='Питон'.encode())

In [3]: r.text
Out[3]: 'ru'
```
