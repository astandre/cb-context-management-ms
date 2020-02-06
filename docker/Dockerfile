FROM python:3.7

RUN pip install gunicorn

COPY docker/settings.ini /app/kbsbot/context_management/settings.ini

COPY . /app

RUN pip install -r /app/requirements.txt
RUN pip install /app/


WORKDIR /app/kbsbot/context_management
EXPOSE 8006
CMD ["gunicorn", "-b", "0.0.0.0:8006", "run:app"]


