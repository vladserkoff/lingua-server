FROM python:3

WORKDIR /tmp
ADD requirements.txt .

RUN pip install -r ./requirements.txt

WORKDIR /opt/lingua

ADD *.py .
ADD lingua ./lingua
ADD https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.ftz ./models/

ADD ./configs/server_settings.py ./

EXPOSE 8000

CMD ["gunicorn", "-c", "server_settings.py", "server:app"]
