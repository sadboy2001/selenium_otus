FROM selenium/standalone-chrome

WORKDIR /app

COPY requirements.txt .

USER root

RUN apt-get update && apt-get install -y python3-pip
RUN pip install -U pip
RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "-m", "pytest"]
