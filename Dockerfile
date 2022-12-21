FROM python:3.8-slim-buster
WORKDIR /app
ENV PYTHONUNBUFFERED=1
RUN python -m pip install --upgrade pip
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python","manage.py","runserver"]