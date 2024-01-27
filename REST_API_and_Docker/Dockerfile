FROM python:3.7

RUN pip install --upgrade pip

WORKDIR /app

COPY requirements.txt /app
RUN pip --no-cache-dir install -r /app/requirements.txt

COPY . /app

CMD ["python", "flask_raper_code.py"]