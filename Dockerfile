FROM python:3.9-slim-buster

RUN apt-get update && apt-get upgrade -y

ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv $VIRTUAL_ENV
# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir

COPY . ./

CMD ["gunicorn", "-w", "1", "-k", "gthread", "--threads", "3", "--timeout", "180", "-b", "0.0.0.0:8080", "--max-requests", "200", "--max-requests-jitter", "10", "--worker-tmp-dir", "/dev/shm", "api:APP"]
EXPOSE 8080
