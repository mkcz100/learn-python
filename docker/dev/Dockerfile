FROM python:3-alpine

ENV PYTHONUNBUFFERED 1
ENV APP_DIR /app
WORKDIR $APP_DIR

#COPY requirements.txt .
RUN ls -all
COPY ./ $APP_DIR

RUN ls -all
RUN pip install --no-cache-dir .

CMD python app.py

EXPOSE 8000

