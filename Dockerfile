FROM python:3.12.4
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENTRYPOINT ["pytest", "--run=remote"]
CMD ["--executor", "--browser"]
