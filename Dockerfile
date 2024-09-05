FROM python:3.12.4
RUN apt-get update && apt-get install -y netcat-openbsd
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["pytest", "--run", "--executor", "--browser", "--url"]

